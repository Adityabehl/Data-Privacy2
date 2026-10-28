# Practical 07 - Privacy-Enhancing Technologies

Practical 07: Privacy-Enhancing Technologies (PETs)

## Aim

To study Privacy-Enhancing Technologies (PETs) and understand how they help protect personal information while allowing digital systems to perform their required functions.

⸻

## Objectives

* To understand the concept of Privacy-Enhancing Technologies.
* To study different PETs.
* To understand how PETs reduce privacy risks.
* To analyze the use of PETs in real-world applications.
* To understand the advantages and limitations of privacy technologies.

⸻

 What are Privacy-Enhancing Technologies?

Privacy-Enhancing Technologies (PETs) are technologies, techniques, and systems designed to reduce unnecessary exposure of personal information while allowing data to be processed or services to be provided.

PETs can help organizations follow the principle of data minimization and reduce privacy risks.

⸻

## Major Privacy-Enhancing Technologies

1. Encryption

Encryption converts readable information called plaintext into an unreadable form called ciphertext.

Only an authorized party with the appropriate key can decrypt the information.

Example

Plaintext
    ↓
Encryption + Key
    ↓
Ciphertext
    ↓
Decryption + Key
    ↓
Plaintext

Applications

* Online banking
* Messaging applications
* HTTPS websites
* Cloud storage
* File protection

⸻

2. Anonymization

Anonymization removes or transforms identifying information so that individuals cannot reasonably be identified from the resulting dataset.

Example

Original:

Name: Rahul
Age: 21
City: Delhi

After anonymization:

Person ID: 001
Age Group: 20–25
Region: Delhi NCR

Anonymization can reduce the risk of identifying individuals, although the effectiveness depends on the method and the possibility of combining the dataset with other information.

⸻

3. Pseudonymization

Pseudonymization replaces direct identifiers with artificial identifiers.

Example:

Original:
Rahul Sharma → Student ID 45892
Pseudonymized:
Rahul Sharma → User_1024

Unlike strong anonymization, pseudonymized data may still be linked back to an individual when additional information is available.

⸻

4. Differential Privacy

Differential privacy provides a mathematical framework for limiting what can be learned about an individual from statistical results.

Instead of directly publishing exact individual information, carefully controlled noise can be introduced into the results.

Basic Concept

Private Dataset
      ↓
Differential Privacy Mechanism
      ↓
Statistical Result + Controlled Noise
      ↓
Published Result

Applications

* Statistical databases
* Research
* Population analytics
* Large-scale data analysis

⸻

5. Data Masking

Data masking hides sensitive parts of information.

Example:

Credit Card:
4532 7812 9876 1234
Masked:
**** **** **** 1234

It is commonly used in:

* Software testing
* Customer support
* Database environments
* Demonstration systems

⸻

6. Tokenization

Tokenization replaces sensitive data with a randomly generated token.

Example:

Original Card Number
        ↓
Tokenization
        ↓
TOKEN-839274

The token itself does not contain the original sensitive information.

Tokenization is commonly used in payment systems and other applications involving sensitive identifiers.

⸻

7. Secure Multi-Party Computation

Secure Multi-Party Computation (MPC) allows multiple parties to jointly calculate a result without directly revealing their private inputs to one another.

Example

Two organizations want to calculate a combined statistic:

Organization A
Private Data
      \
       \
        → Secure Computation → Result
       /
      /
Organization B
Private Data

The parties can obtain the required result while reducing direct disclosure of their inputs.

⸻

8. Federated Learning

Federated learning allows machine-learning models to be trained across multiple devices or organizations without requiring all raw training data to be centralized.

Basic Flow

          Central Server
               ↓
       Global ML Model
        ↙     ↓      ↘
   Device A Device B Device C
      ↓        ↓        ↓
 Local Data Local Data Local Data
      ↓        ↓        ↓
 Local Training
      ↓        ↓        ↓
 Model Updates
        ↘      ↓      ↙
          Server

The raw training data can remain on the participating devices or organizations.

⸻

9. Trusted Execution Environments

A Trusted Execution Environment (TEE) is a protected computing environment designed to isolate sensitive operations from the normal operating environment.

It can help protect sensitive data and computations while they are being processed.

⸻

## Real-World Applications

Technology	Example Application
Encryption	Online banking
Anonymization	Public statistical datasets
Pseudonymization	Healthcare research
Differential Privacy	Statistical analysis
Data Masking	Software testing
Tokenization	Payment systems
MPC	Joint analytics
Federated Learning	Distributed machine learning
TEE	Secure processing

⸻

## Advantages of PETs

* Reduce exposure of personal information.
* Support data minimization.
* Improve user privacy.
* Reduce privacy risks.
* Can support regulatory compliance.
* Allow useful data analysis with reduced disclosure.
* Increase user trust.

⸻

## Limitations

PETs are not a complete solution to every privacy problem.

Some limitations include:

* Additional implementation cost.
* Increased system complexity.
* Possible performance overhead.
* Some methods can reduce data accuracy.
* Incorrect configuration can weaken protection.
* Privacy protection depends on the overall system design.

⸻

## Conclusion

Privacy-Enhancing Technologies provide important technical methods for reducing privacy risks. Technologies such as encryption, anonymization, differential privacy, tokenization, secure multi-party computation, and federated learning can allow organizations to use data while reducing unnecessary exposure of personal information.

However, PETs should be combined with appropriate security controls, privacy policies, governance, and user awareness.

⸻

 ## References

* NIST Privacy Framework
* NIST publications on privacy-enhancing technologies
* GDPR principles
* OECD Privacy Guidelines
* Research literature on Differential Privacy and Federated Learning
