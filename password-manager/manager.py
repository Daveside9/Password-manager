from cryptography.fernet import Fernet
import os
import getpass

# Generate an encryption key and save it to a file
def generate_key():
    """Generate and save a new encryption key to 'key.key'."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'key.key'.")

# Load the encryption key from a file
def load_key():
    """Load the encryption key from 'key.key'."""
    return open("key.key", "rb").read()

# Encrypt data
def encrypt_data(data):
    """Encrypt data using the encryption key."""
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

# Decrypt data
def decrypt_data(data):
    """Decrypt data using the encryption key."""
    key = load_key()
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()

# Set master password
def set_master_password():
    """Set and save the master password."""
    master_password = getpass.getpass("Enter a master password: ")
    encrypted_password = encrypt_data(master_password)
    with open("master_password.txt", "w") as file:
        file.write(encrypted_password)
    print("Master password set successfully.")

# Verify master password
def verify_master_password():
    """Verify the master password entered by the user."""
    try:
        with open("master_password.txt", "r") as file:
            encrypted_password = file.read()
        master_password = getpass.getpass("Enter the master password: ")
        return decrypt_data(encrypted_password) == master_password
    except FileNotFoundError:
        print("Master password not set. Please set it first.")
        return False

# Save credentials
def save_credential():
    """Save a new credential."""
    if not verify_master_password():
        print("Incorrect master password.")
        return
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    encrypted_password = encrypt_data(password)
    with open("credentials.txt", "a") as file:
        file.write(f"{service},{username},{encrypted_password}\n")
    print("Credential saved successfully.")

# View saved credentials
def view_credentials():
    """View saved credentials."""
    if not verify_master_password():
        print("Incorrect master password.")
        return
    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                service, username, encrypted_password = line.strip().split(",")
                password = decrypt_data(encrypted_password)
                print(f"Service: {service}, Username: {username}, Password: {password}")
    except FileNotFoundError:
        print("No credentials found.")

# Main menu logic
if __name__ == "__main__":
    while True:
        print("""
        1. Set Master Password
        2. Login
        3. Save Credential
        4. View Credentials
        5. Exit
        """)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_master_password()
        elif choice == "2":
            if verify_master_password():
                print("Login successful!")
            else:
                print("Login failed!")
        elif choice == "3":
            save_credential()
        elif choice == "4":
            view_credentials()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
