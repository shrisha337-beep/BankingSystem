import streamlit as st
import streamlit as st

# Hide Streamlit's default menu & footer
hide_github_footer = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_github_footer, unsafe_allow_html=True)
import pandas as pd
from bank import BankingSystem
# Initialize the Banking System
st.set_page_config(page_title="Banking System", layout="centered")
bs = BankingSystem()
# Title of the app
st.title("🏦 Simple Banking System (Streamlit)")
st.markdown("Local demo - CSV+JSON Storage. Use sidebar to pick an action")
action = st.sidebar.selectbox("Actions", ["Create Account", "Deposit", "Withdraw", "Check Balance", "Transaction History","All Accounts"])
if action == "Create Account":
    st.header("Create Account")
    name = st.text_input("Account Holder Name")
    initial_deposit = st.number_input("Initial Deposit (₹)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    if st.button("Create Account"):
        if not name.strip():
            st.error("Please enter a valid name")
        else:
            try:
                account = bs.create_account(name, initial_deposit)
                st.success(f"Account created successfully! Account Number: {account['Account Number']}")
                st.json(account)
            except Exception as e:
                st.error(f"Error creating account: {e}")
elif action == "Deposit":
    st.header("Deposit Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Deposit Amount (₹)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    remark = st.text_input("Remark(optional)", value="Deposit")
    if st.button("Deposit"):
        if not account_number.strip():
            st.error("Please enter a valid account number")
        elif amount <= 0:
            st.error("Deposit amount must be positive")
        else:
            try:
                account = bs.deposit(account_number, amount, remark)
                st.success(f"Deposit successful! New Balance: ₹{account['balance']:.2f}")
                st.json(account)
            except ValueError as e:
                st.error(str(e))
elif action == "Withdraw":
    st.header("Withdraw Money")
    account_number = st.text_input("Account Number")
    amount = st.number_input("Withdrawal Amount (₹)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    remark = st.text_input("Remark(optional)", value="Withdrawal")
    if st.button("Withdraw"):
        if not account_number.strip():
            st.error("Please enter a valid account number")
        elif amount <= 0:
            st.error("Withdrawal amount must be positive")
        else:
            try:
                account = bs.withdraw(account_number, amount, remark)
                st.success(f"Withdrawal successful! New Balance: ₹{account['balance']:.2f}")
                st.json(account)
            except ValueError as e:
                st.error(str(e))
elif action == "Check Balance":
    st.header("Check Account Balance")
    account_number = st.text_input("Account Number")
    if st.button("Check Balance"):
        if not account_number.strip():
            st.error("Please enter a valid account number")
        else:
            try:
                account = bs.get_account(account_number)
                if account:
                    st.success(f"Account Balance: ₹{account['balance']:.2f}")
                    st.json(account)
                else:
                    st.error(f"Account with number {account_number} does not exist")
            except ValueError as e:
                st.error(str(e))
                
elif action == "Transaction History":
    st.header("Transaction History")
    account_number = st.text_input("Account Number")
    if st.button("Get Transactions"):
        if not account_number.strip():
            st.error("Please enter a valid account number")
        else:
            try:
                transaction = bs.get_transaction(account_number)
                if transaction:
                    df = pd.DataFrame(transaction)
                    st.dataframe(df)
                else:
                    st.error(f"No transactions found for account numbr {account_number}")
            except ValueError as e:
                st.error(str(e))
elif action == "All Accounts":
    st.header("All Accounts")
    accounts = bs.load_accounts()
    if accounts:
        df = pd.DataFrame.from_dict(accounts, orient='index')
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'Account Number'}, inplace=True)
        st.dataframe(df)
    else:
        st.info("No accounts found. Please create an account first.")
