Password Manager

A simple command-line-based password manager that encrypts and stores credentials securely using the cryptography library.

Features

Master Password: Secure access using a master password.

Encryption: Uses Fernet encryption to store credentials safely.

Credential Storage: Saves encrypted credentials in a text file.

Credential Retrieval: Allows viewing of stored credentials after authentication.

Simple CLI Interface: Easy-to-use command-line interface for managing passwords.

Installation

Prerequisites

Python 3.6 or later

Clone the Repository

git clone https://github.com/yourusername/password-manager.git
cd password-manager

Install Dependencies

pip install -r requirements.txt

Usage

1. Generate an Encryption Key (Run Once)

python manager.py

Select option 1 to set the master password (this also generates an encryption key).

2. Running the Password Manager

python manager.py

Select the appropriate options from the menu:

Set Master Password (Run once if not already set)

Login

Save Credential

View Credentials

Exit

File Structure

password-manager/
│── manager.py          # Main script with encryption and credential management
│── key.key             # Encryption key file (Generated automatically)
│── master_password.txt # Encrypted master password
│── credentials.txt     # Encrypted stored credentials
│── requirements.txt    # Required dependencies

Security Notes

The master password is encrypted and stored in master_password.txt.

Credentials are encrypted before being saved in credentials.txt.

Never share your key.key file, as it is required for decryption.

Dependencies

The project requires the following Python packages:

bcrypt==4.2.1
cffi==1.17.1
cryptography==44.0.0
pycparser==2.22

Install them using:

pip install -r requirements.txt

License

This project is licensed under the MIT License.

Author

joel david

GitHub: https://github.com/Daveside9

