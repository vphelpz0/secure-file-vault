from cryptography.fernet import Fernet
import os

# --- Generate a key and save it to a file ---
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# --- Load the saved key ---
def load_key():
    return open("secret.key", "rb").read()

# --- Encrypt a file ---
def decrypt_file(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            data = file.read()
        decrypted = f.decrypt(data)
        new_filename = filename.replace(".enc", "")
        with open(new_filename, "wb") as file:
            file.write(decrypted)
        print(f"🔓 Decrypted: {filename} ➜ {new_filename}")
    except Exception as e:
        print(f"❌ Failed to decrypt {filename}. Make sure it's a valid encrypted file.\nDetails: {e}")
# --- Decrypt a file ---
def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    new_filename = filename.replace(".enc", "")
    with open(new_filename, "wb") as file:
        file.write(decrypted)
    print(f"🔓 Decrypted: {filename} ➜ {new_filename}")

# --- Main Menu ---
def main():
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()

    while True:
        print("\n🔐 Secure File Vault Menu")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            filename = input("Enter the file name to encrypt: ")
            if os.path.exists(filename):
                encrypt_file(filename, key)
            else:
                print("❌ File not found.")
        elif choice == "2":
            filename = input("Enter the file name to decrypt: ")
            if os.path.exists(filename):
                decrypt_file(filename, key)
            else:
                print("❌ File not found.")
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
