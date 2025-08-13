💳 Banking System

A simple yet functional Python-based Banking System that lets you create accounts, manage balances, and track transactions — all stored locally using JSON and CSV.

📌 Features

Create & Manage Accounts – Add new customers with secure account details.

Deposit & Withdraw – Update balances instantly with validation checks.

Transaction History – Keep track of every transaction in a CSV log.

Persistent Data – Uses JSON for accounts & CSV for transactions.

Error Handling – Handles invalid inputs and edge cases gracefully.

🛠️ Tech Stack

Language: Python 3.x

Libraries:

os (file handling)

json (account storage)

csv (transaction logs)

datetime (timestamping)

📂 Project Structure
banking-system/
│
├── bank.py              # Core banking logic
├── app.py               # Main script to run the application
├── data/
│   ├── accounts.json    # Stores account details
│   └── transactions.csv # Stores transaction records
└── README.md            # Documentation

🚀 Installation & Usage

Clone the repository

git clone https://github.com/your-username/banking-system.git
cd banking-system


Run the program

python app.py

🖥️ Example Output
=== Welcome to the Banking System ===
1. Create Account
2. Deposit
3. Withdraw
4. View Transaction History
5. Exit
Enter your choice:

📌 Future Enhancements

🔒 Password-protected accounts

📊 GUI using Tkinter / Streamlit

🌐 Online database integration

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.
