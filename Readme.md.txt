# Secure Coding Review using Python

## 🔐 CodeAlpha Cyber Security Internship – Task 3

This project was developed as part of the CodeAlpha Cyber Security Internship Task 3: **Secure Coding Review**.

The project demonstrates identifying security vulnerabilities in a Python application, performing code analysis using Bandit, and applying secure coding best practices to remediate the issues.

---

## 📌 Project Overview
This project demonstrates a Secure Coding Review process using Python.  
A vulnerable login application was analyzed to identify common security vulnerabilities and then improved using secure coding practices.

---

## 🎯 Objective
- Identify security vulnerabilities in Python code
- Perform secure coding review
- Use security analysis tools
- Apply remediation techniques and best practices

---

## 🛠 Programming Language
- Python

---

## 🔍 Security Tool Used
- Bandit (Python Security Analyzer)

---

## 📂 Project Files

| File Name | Description |
|------------|-------------|
| vulnerable_app.py | Insecure login application |
| secure_app.py | Secure version of the application |
| review_report.md | Detailed security review report |
| requirements.txt | Required dependency |
| README.md | Project documentation |

---

## 🚨 Vulnerabilities Identified

### 1. Hardcoded Password
- Credentials were directly stored in source code.

### 2. SQL Injection
- Unsafe string-based SQL query construction was used.

---

## ✅ Security Improvements Implemented

- Removed hardcoded credentials
- Used parameterized SQL queries
- Implemented SHA-256 password hashing
- Improved secure coding practices

---

## ▶️ How to Run the Project

### Run Vulnerable Application
```bash
python vulnerable_app.py
```

### Run Secure Application
```bash
python secure_app.py
```

### Run Security Scan
```bash
bandit vulnerable_app.py
bandit secure_app.py
```

---

## 📊 Results

### Vulnerable Application
- Hardcoded password detected
- SQL Injection vulnerability detected

### Secure Application
- No issues identified by Bandit

---

## 📚 Learning Outcome
This project helped in understanding:
- Secure coding practices
- Common web vulnerabilities
- SQL Injection prevention
- Password hashing
- Static code analysis

---

## 👩‍💻 Developed By
Thatchayaini R