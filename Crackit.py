import hashlib
import os
import pyfiglet

# Function to clear the screen
def clear_screen():
    """Clears the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to show the Crackit banner
def show_banner():
    """Displays the banner."""
    banner = pyfiglet.figlet_format("Crackit", font="slant")
    neon_blue = "\033[38;5;51m"  # Neon blue color code
    print(neon_blue + banner)
    print(neon_blue + "                       - By Mr.CodeX\n")

# Hash cracking function
def crack_hash(hash_value, hash_type, wordlist_file):
    """Attempts to crack the given hash using the specified hash type and wordlist."""
    print(f"Cracking Hash: {hash_value} ({hash_type})")
    try:
        with open(wordlist_file, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip()
                if hash_type == 'md5':
                    if hashlib.md5(word.encode()).hexdigest() == hash_value:
                        print(f"[Success] {word} -> {hash_value}")
                        return word
                elif hash_type == 'sha256':
                    if hashlib.sha256(word.encode()).hexdigest() == hash_value:
                        print(f"[Success] {word} -> {hash_value}")
                        return word
            print("[Error] Hash could not be cracked.")
            return None
    except FileNotFoundError:
        print(f"[Error] Wordlist file not found: {wordlist_file}")
        return None

# Encryption function (MD5 and SHA256)
def encrypt_text(text, hash_type):
    """Encrypts the given text using the specified hash type."""
    if hash_type == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        print("[Error] Unsupported hash type.")
        return None

# Main function
def main():
    clear_screen()
    show_banner()
    print("Welcome to Crackit!")

    while True:
        try:
            print("\nMake your choice:")
            print("1. Crack a hash")
            print("2. Encrypt text")
            print("3. Exit")
            
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                hash_value = input("Enter the hash you want to crack: ")
                hash_type = input("Select the hash type (md5/sha256): ").lower()
                wordlist_file = input("Enter the path to the wordlist file: ")
                result = crack_hash(hash_value, hash_type, wordlist_file)
                if result:
                    print(f"\n[Success] The hash was cracked: {result}")
                input("\nPress Enter to return to the menu...")

            elif choice == '2':
                text = input("Enter the text you want to encrypt: ")
                hash_type = input("Select the hash type (md5/sha256): ").lower()
                encrypted_text = encrypt_text(text, hash_type)
                if encrypted_text:
                    print(f"\n[Success] Encrypted text: {encrypted_text}")
                    input("\nPress Enter to exit...")
                    break

            elif choice == '3':
                print("Exiting...")
                break
            
            else:
                print("[Error] Invalid choice!")
        except KeyboardInterrupt:
            print("\n[INFO] Program exiting... Goodbye!")
            break

if __name__ == "__main__":
    main()
