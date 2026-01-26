import threading
import random


# ----------------------------------------------------
# BankAccount Class (Thread-Safe + Deadlock Prevention)
# ----------------------------------------------------

class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self._account_number = str(account_number)
        self._balance = float(initial_balance)
        self._lock = threading.RLock()   # prevents self-deadlock

    def get_balance(self):
        with self._lock:
            return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        with self._lock:   # protects the shared balance
            self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        with self._lock:
            if self._balance < amount:
                raise ValueError("Insufficient funds.")
            self._balance -= amount

    def transfer_to(self, other, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self is other:
            raise ValueError("Cannot transfer to the same account.")

        # Deadlock prevention: always lock in consistent order
        first, second = (
            (self, other)
            if self._account_number < other._account_number
            else (other, self)
        )

        with first._lock:
            with second._lock:
                if self._balance < amount:
                    raise ValueError("Insufficient funds.")
                self._balance -= amount
                other._balance += amount


# ----------------------------------------------------
# Transaction Simulator (Random Concurrent Activity)
# ----------------------------------------------------

class TransactionSimulator:
    def __init__(self, accounts):
        self.accounts = accounts

    def _user_session(self, iterations, seed):
        rng = random.Random(seed)
        for _ in range(iterations):
            account = rng.choice(self.accounts)
            amount = rng.randint(1, 100)
            op = rng.random()

            if op < 0.4:                      # deposit
                account.deposit(amount)
            elif op < 0.8:                    # withdrawal
                try:
                    account.withdraw(amount)
                except ValueError:
                    pass
            else:                             # transfer
                other = rng.choice(self.accounts)
                if other is not account:
                    try:
                        account.transfer_to(other, amount)
                    except ValueError:
                        pass

    def run(self, users, iterations):
        threads = []
        for i in range(users):
            t = threading.Thread(target=self._user_session, args=(iterations, i))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()


# -------------------------------------------------------------------------
# Testing & Validation (Matches EXACTLY what your essay says)
# -------------------------------------------------------------------------

def simple_concurrent_deposit_test():
    """
    This test matches the essay:
    — multiple threads
    — same account
    — repeated deposit loop
    — expected vs actual check
    """

    account = BankAccount("TEST-1", 0.0)

    num_threads = 10
    loops = 1000

    def worker():
        for _ in range(loops):
            account.deposit(1)   # ← EXACT test loop described in essay

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    expected = num_threads * loops
    actual = account.get_balance()

    print("\n=== TEST: Concurrent Deposit Test ===")
    print("Expected final balance:", expected)
    print("Actual final balance:  ", actual)
    print("RESULT:", "PASS ✓" if actual == expected else "FAIL ✗")
    print()


# --------------------------------------------------------
# Full Demonstration Run (This shows everything working)
# --------------------------------------------------------

def main():
    # STEP 1 — Run the test from your essay
    simple_concurrent_deposit_test()

    # STEP 2 — Run a real simulation
    a1 = BankAccount("A100", 5000)
    a2 = BankAccount("A200", 5000)
    a3 = BankAccount("A300", 5000)
    accounts = [a1, a2, a3]

    print("=== Initial Balances ===")
    for acc in accounts:
        print(acc._account_number, acc.get_balance())

    sim = TransactionSimulator(accounts)
    sim.run(users=10, iterations=500)

    print("\n=== Final Balances After Simulation ===")
    for acc in accounts:
        print(acc._account_number, acc.get_balance())


if __name__ == "__main__":
    main()
