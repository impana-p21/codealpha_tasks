Secure Coding Review

1. Project Overview

This project demonstrates a security review of a simple Python login application.

The original application contains security weaknesses that could expose the application to attacks. The vulnerable version was manually inspected and then improved using secure coding practices.

Two versions are included:

* vulnerable_app.py - intentionally insecure version.
* secure_app.py - improved version.

2. Objective

The main objectives of this project are:

* Identify security vulnerabilities in source code.
* Understand how insecure coding practices create security risks.
* Apply secure coding principles.
* Recommend appropriate remediation techniques.
* Compare vulnerable and improved implementations.

3. Vulnerability 1 - SQL Injection

Vulnerable Code

query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

The application directly combines user input with an SQL query.

Risk

An attacker may provide specially crafted input that changes the intended SQL statement.

This can potentially allow unauthorized database access or bypass application logic.

Severity

High

Recommendation

Use parameterized SQL queries instead of concatenating user input into SQL statements.

Remediation

The secure version uses:

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password_hash))

Parameterized queries separate SQL commands from user-supplied data.

⸻

4. Vulnerability 2 - Insecure Password Handling

Vulnerable Code

password = input("Enter password: ")

The original application directly uses the password as part of the database query.

Risk

Storing or handling passwords in plaintext can expose user credentials if the database is compromised.

Severity

High

Recommendation

Passwords should never be stored as plaintext.

A dedicated password hashing algorithm such as Argon2id, bcrypt, or scrypt should be used in production systems.

Remediation

The demonstration secure version hashes the password before database comparison:

password_hash = hash_password(password)

For production authentication systems, a dedicated password hashing algorithm should be used instead of SHA-256.

⸻

5. Vulnerability 3 - Lack of Input Validation

The vulnerable application accepts username input without validation.

Risk

Unexpected or malicious input may be supplied to the application.

Severity

Medium

Recommendation

Input should be validated according to the expected format and length.

Examples include:

* Restricting username length.
* Rejecting unexpected characters where appropriate.
* Validating input before processing.

⸻

6. Security Improvements

The improved application introduces:

* Parameterized SQL queries.
* Password hashing demonstration.
* Separation of user input from SQL commands.
* Improved handling of authentication data.

7. Secure Coding Best Practices

Developers should:

1. Validate user input.
2. Use parameterized database queries.
3. Never store plaintext passwords.
4. Use secure password hashing algorithms.
5. Follow the principle of least privilege.
6. Avoid exposing sensitive information in error messages.
7. Keep dependencies updated.
8. Perform regular security reviews.
9. Use static analysis tools where appropriate.
10. Test applications for common security vulnerabilities.

8. Tools and Methodology

The review was performed using:

* Manual source-code inspection.
* Python code comparison.
* Secure coding principles.
* OWASP security concepts.

9. Findings Summary

Vulnerability	Severity	Remediation
SQL Injection	High	Parameterized queries
Insecure password handling	High	Secure password hashing
Missing input validation	Medium	Validate and restrict input

10. Conclusion

The secure coding review demonstrates how seemingly simple programming practices can introduce serious security vulnerabilities.

The main security issue identified was SQL injection caused by direct SQL query construction using user input. This was addressed through parameterized queries.

Password handling was also improved by demonstrating password hashing. For a real-world application, a dedicated password hashing algorithm such as Argon2id, bcrypt, or scrypt should be used.

The project highlights the importance of secure coding practices throughout the software development lifecycle.
