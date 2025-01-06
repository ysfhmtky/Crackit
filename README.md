# 🔐 **Crackit**

**Crackit** is a Python-based tool for hash cracking and encryption. It supports both **MD5** and **SHA256** hashing algorithms, allowing users to crack hashes using a wordlist or encrypt text into hashes.

## 🚀 Features

- 🛠️ **Hash Cracking**: Crack MD5 and SHA256 hashes using a wordlist.
- 🔐 **Text Encryption**: Encrypt any text into MD5 or SHA256 format.
- 🎨 **Interactive Menu**: User-friendly interface with a neon-styled banner.
- 🧰 **Supports Custom Wordlists**: Specify your own wordlist file for cracking.

## 📝 Prerequisites

To run **Crackit**, you'll need:

- Python 3.x
- `pyfiglet` library for banner display.

### Install Required Libraries

Run the following command to install the necessary Python library:

```bash
pip install pyfiglet
```
🔧 Usage
Clone this repository to your local machine:

```Copy code
git clone https://github.com/ysfhmtky/Crackit.git
cd crackit
```

Run the script:

```Copy code
python Crackit.py
```


Select one of the available options:
```
Option 1: Crack a hash by providing the hash value, type (MD5 or SHA256), and path to your wordlist.
Option 2: Encrypt text into MD5 or SHA256 format.
Option 3: Exit the program.
```
Example Usage
Crack a Hash

```Copy code
Enter your choice (1/2/3): 1
Enter the hash you want to crack: d41d8cd98f00b204e9800998ecf8427e
Select the hash type (md5/sha256): md5
Enter the path to the wordlist file: /path/to/wordlist.txt
[Success] The hash was cracked: password123
Encrypt Text
```

```Copy code
Enter your choice (1/2/3): 2
Enter the text you want to encrypt: hello
Select the hash type (md5/sha256): sha256
[Success] Encrypted text: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```
📄 File Structure

```Copy code
Crackit/
├── Crackit.py         # Main Python script
└── README.md          # Project documentation
```
🤝 Contributing
If you'd like to contribute to Crackit, follow these steps:
```
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes.
Commit your changes (git commit -am 'Add feature').
Push to the branch (git push origin feature-name).
Create a new Pull Request.
```
⚠️ Disclaimer
```
Crackit is intended for educational purposes only. Use it responsibly and only with explicit permission on systems you own or have permission to test. Unauthorized use is illegal and punishable by law.
```

### Key Points in the README:
- Includes detailed instructions for setup and usage.
- Provides examples for cracking hashes and encrypting text.
- Adds a file structure section for clarity.
- Includes a **Disclaimer** to ensure ethical usage. 

Let me know if you'd like any further tweaks! 🚀


