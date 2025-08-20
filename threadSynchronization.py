# using locks

import threading
import time

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.lock = threading.Lock()
    
    def deposit(self, amount):
        with self.lock:  # Acquire lock automatically
            print(f"Depositing {amount}")
            new_balance = self.balance + amount
            time.sleep(0.1)  # Simulate processing time
            self.balance = new_balance
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                new_balance = self.balance - amount
                time.sleep(0.1)
                self.balance = new_balance
            else:
                print(f"Insufficient funds for withdrawal of {amount}")
    
    def get_balance(self):
        with self.lock:
            return self.balance

def perform_transactions(account, operations):
    for op, amount in operations:
        if op == 'deposit':
            account.deposit(amount)
        elif op == 'withdraw':
            account.withdraw(amount)

# Create shared account
account = BankAccount(1000)

# Define transactions for different threads
thread1_ops = [('deposit', 100), ('withdraw', 200), ('deposit', 50)]
thread2_ops = [('withdraw', 300), ('deposit', 150), ('withdraw', 100)]

# Create threads
thread1 = threading.Thread(target=perform_transactions, args=(account, thread1_ops))
thread2 = threading.Thread(target=perform_transactions, args=(account, thread2_ops))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final balance: {account.get_balance()}")