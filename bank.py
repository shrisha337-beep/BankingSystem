import os
import json
import csv
import datetime

class BankingSystem:
    def __init__(self, accounts_file='accounts.json', transactions_file='transactions.csv'):
        self.accounts_file = accounts_file
        self.transactions_file = transactions_file

        # Create empty files if they don't exist
        if not os.path.exists(self.accounts_file):
            with open(self.accounts_file, 'w') as f:
                json.dump({}, f)
        if not os.path.exists(self.transactions_file):
            with open(self.transactions_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Account Number", "Type", "Amount", "Balance", "Description"])

    def load_accounts(self):
        with open(self.accounts_file, 'r') as f:
            return json.load(f)

    def save_accounts(self, accounts):
        with open(self.accounts_file, 'w') as f:
            json.dump(accounts, f, indent=4)

    def next_account_number(self, accounts):
        if accounts:
            return max(map(int, accounts.keys())) + 1
        return 1001

    def create_account(self, name, initial_deposit=0.0):
        accounts = self.load_accounts()
        acc_no = self.next_account_number(accounts)

        account_data = {
            "Name": name,
            "Account Number": acc_no,
            "Balance": float(initial_deposit),
            "Created": datetime.datetime.now().isoformat()
        }

        accounts[str(acc_no)] = account_data
        self.save_accounts(accounts)

        if float(initial_deposit) > 0:
            self.add_account_tx(acc_no, "Deposit", initial_deposit, initial_deposit, "Initial Deposit")

        return account_data

    def add_account_tx(self, acc_no, tx_type, amount, balance, description=""):
        with open(self.transactions_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.datetime.now().isoformat(), acc_no, tx_type, amount, balance, description])

    def deposit(self, acc_no, amount, remark=""):
        accounts = self.load_accounts()
        acc_no = str(acc_no)

        if acc_no not in accounts:
            return {"error": "Account not found"}

        accounts[acc_no]["Balance"] += float(amount)
        self.save_accounts(accounts)
        self.add_account_tx(acc_no, "Deposit", amount, accounts[acc_no]["Balance"], "Cash deposit")
        return accounts[acc_no]

    def withdraw(self, acc_no, amount, remark=""):
        accounts = self.load_accounts()
        acc_no = str(acc_no)

        if acc_no not in accounts:
            return {"error": "Account not found"}

        if accounts[acc_no]["Balance"] < float(amount):
            return {"error": "Insufficient funds"}

        accounts[acc_no]["Balance"] -= float(amount)
        self.save_accounts(accounts)
        self.add_account_tx(acc_no, "Withdrawal", amount, accounts[acc_no]["Balance"], "Cash withdrawal")
        return accounts[acc_no]

    def get_account(self, acc_no):
        accounts = self.load_accounts()
        acc_no = str(acc_no)
        return accounts.get(acc_no, {"error": "Account not found"})

    def list_accounts(self):
        return self.load_accounts()

    def list_transactions(self, acc_no=None):
        transactions = []
        with open(self.transactions_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if acc_no is None or str(row["Account Number"]) == str(acc_no):
                    transactions.append(row)
        return transactions