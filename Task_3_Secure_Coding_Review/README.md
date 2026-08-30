CodeAlpha Secure Coding Review

Project Overview

This project performs a security review of a simple Python login application.

The purpose is to identify common security vulnerabilities and demonstrate how they can be remediated using secure coding practices.

Project Files

Task_3_Secure_Coding_Review/
├── vulnerable_app.py
├── secure_app.py
├── security_report.md
└── README.md

Vulnerabilities Identified

1. SQL Injection

The vulnerable application constructs an SQL query by directly concatenating user input.

Risk: Malicious input may alter the intended SQL query.

Solution: Use parameterized SQL queries.

2. Insecure Password Handling

The vulnerable version directly uses the supplied password in the database query.

Risk: Plaintext password handling can expose credentials if the database is compromised.

Solution: Use secure password hashing and never store plaintext passwords.

3. Missing Input Validation

The application does not validate username input.

Risk: Unexpected or malicious input may be supplied.

Solution: Validate input according to expected format and length.

Technologies Used

* Python
* SQLite
* Secure coding principles
* OWASP security concepts

How to Run

Run the vulnerable version:

python vulnerable_app.py

Run the improved version:

python secure_app.py

A users.db SQLite database with appropriately prepared test data is required for a successful login demonstration.

Security Improvements

The secure version demonstrates:

* Parameterized SQL queries.
* Password hashing.
* Improved handling of authentication data.
* Separation of SQL commands from user input.

Security Notice

The vulnerable application is intentionally insecure and is included only for educational security-review purposes.

It should not be deployed as a production authentication system.

The network and security techniques demonstrated in this project should only be used for authorized and educational purposes.

Learning Outcomes

This project provides practical understanding of:

* SQL injection.
* Secure database queries.
* Password security.
* Input validation.
* Vulnerability identification.
* Security remediation.
* Secure coding practices.

Conclusion

The project demonstrates the importance of identifying vulnerabilities during software development and applying secure coding practices to reduce security risks.
