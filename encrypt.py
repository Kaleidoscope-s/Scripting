#!/usr/bin/python3
# Nick Alderete



from cryptography.fernet import Fernet
import os 

# Functions to write and load key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

# Write key and load key
write_key()
key = load_key()

# Functions for encryption and decryption
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        original_data = file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(original_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message, key):
    plaintext = message.encode('utf-8')
    f = Fernet(key)
    encrypted = f.encrypt(plaintext)
    print("The encrypted message is:", encrypted.decode('utf-8'))

def decrypt_message(encrypted_message, key):
    ciphertext = encrypted_message.encode('utf-8')
    f = Fernet(key)
    decrypted = f.decrypt(ciphertext)
    print("The decrypted message is:", decrypted.decode('utf-8'))

def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
    print("Your folder has been encrypted")

def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)
    print("Your folder has been decrypted")

# Main program loop
while True:
    # Prompt user for mode selection
    choices = {
        "1": "Encrypt File",
        "2": "Decrypt File",
        "3": "Encrypt Message",
        "4": "Decrypt Message",
        "5": "Encrypt Folder",
        "6": "Decrypt Folder",
        "7": "Exit"
    }
    
    method_choice = input("Pick one of the following choices:\n 1) Encrypt file\n 2) Decrypt file\n 3) Encrypt message\n 4) Decrypt message\n 5) Encrypt folder\n 6) Decrypt folder\n 7) Exit\n")
    method = choices.get(method_choice)

    # Execute selected mode
    if method == "Encrypt File":
        file_path = input("Please type the file path you'd like to encrypt: ")
        encrypt_file(file_path, key)
        print("Your file has been encrypted")

    elif method == "Decrypt File":
        file_path = input("Please type the file path you'd like to decrypt: ")
        decrypt_file(file_path, key)
        print("Your file has been decrypted")

    elif method == "Encrypt Message":
        message = input("Please type the message you'd like to encrypt: ")
        encrypt_message(message, key)

    elif method == "Decrypt Message":
        encrypted_message = input("Please type the message you'd like to decrypt: ")
        decrypt_message(encrypted_message, key)

    elif method == "Encrypt Folder":
        folder_path = input("Please type the folder path you'd like to encrypt: ")
        encrypt_folder(folder_path, key)

    elif method == "Decrypt Folder":
        folder_path = input("Please type the folder path you'd like to decrypt: ")
        decrypt_folder(folder_path, key)

    elif method == "Exit":
        break

    else:
        print("Invalid choice. Please try again.")
