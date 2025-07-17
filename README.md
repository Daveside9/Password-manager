🔐 Password Manager
A simple yet secure command-line password manager that helps users store and manage multiple credentials behind a single master password.

✨ Features
Master Password Protection – Access to your credentials is locked with a master password known only to you.

Fernet Encryption – All data is encrypted using secure cryptographic methods.

Credential Management – Easily save and retrieve encrypted login credentials.

Simple CLI Interface – Minimal and intuitive command-line interface.

Offline Storage – Everything is stored locally and securely in text files.

🛠️ Installation
Prerequisites
Python 3.6 or higher

Clone the Repository
bash
Copy
Edit
git clone https://github.com/Daveside9/password-manager.git
cd password-manager
Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
1. Generate an Encryption Key & Set Master Password (Run Once)
bash
Copy
Edit
python manager.py
Choose option 1 to set your master password.

This will also generate the encryption key (key.key) automatically.

2. Run the Password Manager
bash
Copy
Edit
python manager.py
Choose from the following menu options:

1 – Set Master Password (only once if not yet set)

2 – Login with your master password

3 – Save a new credential (e.g., Gmail, Facebook, etc.)

4 – View saved credentials

5 – Exit

📁 File Structure
pgsql
Copy
Edit
password-manager/
│
├── manager.py              # Main script to run the app
├── key.key                 # Encryption key (auto-generated)
├── master_password.txt     # Encrypted master password
├── credentials.txt         # Encrypted credentials storage
└── requirements.txt        # Project dependencies
🔒 Security Notes
Never share your key.key file – it's critical for decrypting your data.

The master password and all saved credentials are encrypted.

Keep your project directory secure and backed up if needed.

📦 Dependencies
This project uses the following Python packages:

bcrypt==4.2.1

cffi==1.17.1

cryptography==44.0.0

pycparser==2.22

Install them with:

bash
Copy
Edit
pip install -r requirements.txt
🧑‍💻 Author
Joel David
GitHub: @Daveside9

📄 License
This project is licensed under the MIT License.

