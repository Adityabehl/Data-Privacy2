### Practical-04: Cryptography

Implementation of Cryptographic Techniques and Tools

⸻

## Aim

To understand and implement different cryptographic techniques used for protecting data privacy and security, including:

* Symmetric Encryption
* Asymmetric Encryption
* Hashing
* Digital Signatures
* Encryption and Decryption

⸻

 ## Objectives

The objectives of this practical are:

1. To understand the basic concepts of cryptography.
2. To understand plaintext and ciphertext.
3. To implement symmetric encryption using AES.
4. To implement asymmetric encryption using RSA.
5. To generate cryptographic hashes using SHA-256.
6. To generate and verify digital signatures.
7. To understand the practical importance of cryptography in data privacy.

⸻

##1. Introduction to Cryptography

Cryptography is the technique of protecting information by transforming readable data into an unreadable form so that unauthorized users cannot understand it.

The original readable information is called plaintext, while the encrypted information is called ciphertext.

Basic Process

Plaintext
    ↓
Encryption + Key
    ↓
Ciphertext
    ↓
Decryption + Key
    ↓
Plaintext

Cryptography is widely used in:

* Online banking
* UPI and digital payments
* Password protection
* Secure messaging
* HTTPS
* Digital signatures
* Secure file storage
* Authentication systems

⸻

##2. Important Cryptographic Terms

Term	Meaning
Plaintext	Original readable message
Ciphertext	Encrypted unreadable message
Encryption	Converting plaintext into ciphertext
Decryption	Converting ciphertext back into plaintext
Key	Secret value used by a cryptographic algorithm
Hash	Fixed-length representation of data
Digital Signature	Mechanism used to verify authenticity and integrity

⸻

##3. Types of Cryptography

Cryptography can broadly be divided into:

1. Symmetric Cryptography

The same secret key is used for encryption and decryption.

Plaintext
    ↓
AES + Secret Key
    ↓
Ciphertext
    ↓
AES + Same Key
    ↓
Plaintext

Examples:

* AES
* DES
* 3DES

AES is commonly used for efficient encryption of data.

⸻

2. Asymmetric Cryptography

Two different keys are used:

* Public Key
* Private Key

The public key can be shared, while the private key must be kept secret.

Examples:

* RSA
* ECC
* Diffie-Hellman

⸻

3. Hashing

Hashing converts data into a fixed-length value.

Input Data
    ↓
Hash Function
    ↓
Hash Value

Unlike encryption, hashing is designed to be a one-way operation.

Examples:

* SHA-256
* SHA-512
* SHA-3

⸻

4. Digital Signature

A digital signature provides:

* Authentication
* Integrity
* Non-repudiation

A private key is used to create the signature and the corresponding public key is used for verification.

⸻

##4. Cryptographic Techniques Implemented

This practical implements:

Technique	Algorithm
Symmetric Encryption	AES
Asymmetric Encryption	RSA
Hashing	SHA-256
Digital Signature	RSA + SHA-256

⸻

##5. Software Requirements

Software

* Python 3.x
* Google Colab / Jupyter Notebook
* GitHub

Python Libraries

cryptography
hashlib

hashlib is included with Python, while the cryptography package can be installed using pip.

⸻

##6. Installation

Run the following command in Google Colab:

!pip install cryptography

⸻

##7. Implementation

7.1 Import Required Libraries

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    PublicFormat,
    NoEncryption
)
import hashlib

⸻

##8. Symmetric Encryption using Fernet

Fernet provides authenticated symmetric encryption.

Code

from cryptography.fernet import Fernet
# Generate secret key
key = Fernet.generate_key()
print("Generated Key:")
print(key.decode())
# Create Fernet object
cipher = Fernet(key)
# Original message
message = "This is confidential data."
# Convert message into bytes
message_bytes = message.encode()
# Encryption
encrypted_message = cipher.encrypt(message_bytes)
print("\nOriginal Message:")
print(message)
print("\nEncrypted Message:")
print(encrypted_message)
# Decryption
decrypted_message = cipher.decrypt(encrypted_message)
print("\nDecrypted Message:")
print(decrypted_message.decode())

⸻

Expected Output

Generated Key:
<generated secret key>
Original Message:
This is confidential data.
Encrypted Message:
<encrypted ciphertext>
Decrypted Message:
This is confidential data.

The exact key and ciphertext will be different each time because a new key and encryption randomness are generated.

⸻

##9. AES Encryption Example

AES is a symmetric-key encryption algorithm.

For practical demonstration, Fernet is used because it provides encryption together with integrity protection.

from cryptography.fernet import Fernet
# Generate AES-compatible secret key through Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
data = "Sensitive student information"
# Encrypt
ciphertext = cipher.encrypt(data.encode())
# Decrypt
plaintext = cipher.decrypt(ciphertext).decode()
print("Original Data:", data)
print("Encrypted Data:", ciphertext)
print("Decrypted Data:", plaintext)

⸻

##10. Hashing using SHA-256

Hashing is used to generate a fixed-length digest from data.

SHA-256 produces a 256-bit hash, represented as a hexadecimal string.

Code

import hashlib
message = "Data Privacy Practical"
hash_object = hashlib.sha256(message.encode())
hash_value = hash_object.hexdigest()
print("Original Message:")
print(message)
print("\nSHA-256 Hash:")
print(hash_value)

⸻

Expected Output

Original Message:
Data Privacy Practical
SHA-256 Hash:
<64-character hexadecimal hash>

The hash will always be the same for the same input.

For example:

SHA-256("Hello")

will produce the same hash whenever the exact same input is provided.

⸻

##11. Demonstrating Hash Sensitivity

Even a small change in the input produces a completely different hash.

import hashlib
message1 = "Hello World"
message2 = "Hello world"
hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()
print("Message 1:", message1)
print("Hash 1:", hash1)
print("\nMessage 2:", message2)
print("Hash 2:", hash2)
print("\nHashes are equal:", hash1 == hash2)

Expected Result

Hashes are equal: False

This property is known as the avalanche effect.

⸻

##12. RSA Asymmetric Encryption

RSA is an asymmetric cryptographic algorithm.

It uses:

Public Key
Private Key

The public key can be shared, while the private key should remain secret.

⸻

Code

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
# Generate public key
public_key = private_key.public_key()
message = b"Confidential RSA Message"
# Encryption using public key
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Encrypted Message:")
print(ciphertext)
# Decryption using private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\nDecrypted Message:")
print(plaintext.decode())

⸻

Expected Output

Encrypted Message:
<binary encrypted data>
Decrypted Message:
Confidential RSA Message

⸻

##13. Digital Signature

A digital signature is used to verify:

* Who created the message
* Whether the message was modified

The sender signs the message using a private key.

The receiver verifies the signature using the corresponding public key.

⸻

Code

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
# Obtain public key
public_key = private_key.public_key()
message = b"This message is digitally signed."
# Create digital signature
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("Digital Signature:")
print(signature)
# Verify signature
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("\nSignature Verification: SUCCESS")
    print("The message is authentic and has not been modified.")
except Exception:
    print("\nSignature Verification: FAILED")

⸻

##14. Digital Signature Tampering Test

We can check what happens if the message is modified after signing.

tampered_message = b"This message has been modified."
try:
    public_key.verify(
        signature,
        tampered_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verification: SUCCESS")
except Exception:
    print("Signature Verification: FAILED")
    print("The message has been modified.")

⸻

Expected Output

Signature Verification: FAILED
The message has been modified.

This demonstrates how digital signatures help detect data tampering.

⸻

##15. Complete Cryptography Program

The following program demonstrates hashing, symmetric encryption, RSA encryption and digital signatures together.

import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
message = "Data Privacy protects sensitive information."
print("=" * 60)
print("          CRYPTOGRAPHY PRACTICAL")
print("=" * 60)
# ------------------------------------------------
# 1. HASHING
# ------------------------------------------------
hash_value = hashlib.sha256(message.encode()).hexdigest()
print("\n1. SHA-256 HASHING")
print("-------------------------")
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
# ------------------------------------------------
# 2. SYMMETRIC ENCRYPTION
# ------------------------------------------------
key = Fernet.generate_key()
cipher = Fernet(key)
encrypted_data = cipher.encrypt(message.encode())
decrypted_data = cipher.decrypt(encrypted_data).decode()
print("\n2. SYMMETRIC ENCRYPTION")
print("-------------------------")
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypted_data)
# ------------------------------------------------
# 3. RSA ENCRYPTION
# ------------------------------------------------
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()
rsa_message = b"RSA protects confidential information."
encrypted_rsa = public_key.encrypt(
    rsa_message,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
decrypted_rsa = private_key.decrypt(
    encrypted_rsa,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("\n3. RSA ASYMMETRIC ENCRYPTION")
print("-------------------------")
print("Encrypted RSA Data:", encrypted_rsa)
print("Decrypted RSA Data:", decrypted_rsa.decode())
# ------------------------------------------------
# 4. DIGITAL SIGNATURE
# ------------------------------------------------
signature = private_key.sign(
    message.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("\n4. DIGITAL SIGNATURE")
print("-------------------------")
print("Digital Signature Generated Successfully.")
try:
    public_key.verify(
        signature,
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verification: SUCCESS")
except Exception:
    print("Signature Verification: FAILED")
print("\n" + "=" * 60)
print("             PRACTICAL COMPLETED")
print("=" * 60)

⸻

## 16. Comparison of Cryptographic Techniques

Feature	Symmetric Encryption	Asymmetric Encryption	Hashing	Digital Signature
Keys	One key	Public + Private	No encryption key required	Private + Public
Reversible	Yes	Yes	No	Verification only
Main Purpose	Confidentiality	Confidentiality / Key exchange	Integrity	Authentication & Integrity
Example	AES	RSA	SHA-256	RSA-PSS
Speed	Fast	Slower	Very Fast	Slower than hashing

⸻

## 17. Real-World Applications

🔐 Online Banking

Encryption protects financial information during transmission.

💳 Digital Payments

Cryptographic techniques help protect payment information and authenticate transactions.

🌐 HTTPS

Cryptographic protocols help establish secure communication between browsers and servers.

🔑 Password Storage

Secure password systems store password-derived hashes rather than plaintext passwords.

📄 Digital Documents

Digital signatures can verify the authenticity and integrity of electronically signed documents.

📱 Secure Messaging

Modern messaging systems use cryptographic mechanisms to protect messages from unauthorized access.

⸻

## 18. Advantages of Cryptography

1. Protects confidential information.
2. Prevents unauthorized access.
3. Provides data integrity.
4. Supports authentication.
5. Enables secure communication.
6. Helps protect financial transactions.
7. Provides mechanisms for digital signatures.

⸻

## 19. Limitations

1. Poor key management can compromise security.
2. Strong encryption can require additional computational resources.
3. Lost private keys can make encrypted information inaccessible.
4. Weak passwords can reduce the security of cryptographic systems.
5. Cryptographic algorithms must be implemented correctly.

⸻

## 20. Result

The practical successfully demonstrated different cryptographic techniques:

* Symmetric encryption using Fernet/AES-based authenticated encryption
* Asymmetric encryption using RSA
* SHA-256 hashing
* Digital signatures using RSA-PSS
* Signature verification
* Detection of message tampering

⸻

