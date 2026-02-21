# Secure-File-Transfer-Monitoring-System
A Python-based Secure File Transfer Monitoring System that detects unauthorized file movement, USB data exfiltration, and integrity violations using SHA256 hashing.
🔐 Secure File Transfer Monitoring System

A real-time file monitoring and integrity verification system developed using Python during my internship at Unified Mentor.

This project simulates a Security Operations Center (SOC) level monitoring tool designed to detect unauthorized file transfers, insider threats, and data exfiltration attempts.

🚀 Project Overview

The Secure File Transfer Monitoring System monitors file system activities and detects:

File creation

File deletion

File modification

File movement

Unauthorized sensitive file transfers

USB data exfiltration attempts

Bulk file transfer behavior

File integrity violations using SHA256 hashing

The system generates structured audit logs and real-time alerts.

🎯 Key Features

✔ Real-time file system monitoring
✔ Sensitive directory detection
✔ USB transfer detection
✔ SHA256-based file integrity verification
✔ Bulk transfer detection
✔ Security event logging
✔ Audit trail generation

🛠 Technologies Used

Python

Watchdog (file system monitoring)

Hashlib (SHA256 hashing)

Psutil (USB detection)

VS Code

Windows OS

🏗 System Workflow

Monitor file system events

Check if file belongs to sensitive directory

Generate file hash

Detect USB or external transfer

Log event

Trigger alert if suspicious

📊 Example Output

ALERT: Sensitive file moved to USB

File Deleted Warning

Bulk File Transfer Detected

Integrity Hash Logged

🔐 Security Concepts Implemented

File Integrity Monitoring (FIM)

Data Loss Prevention (DLP)

Insider Threat Detection

Security Logging & Auditing

Defensive Cybersecurity Monitoring

📈 Learning Outcomes

Real-time system monitoring

Hash-based integrity validation

Windows file system event handling

Log-based security auditing

Practical SOC-level defensive techniques

🔮 Future Enhancements

Email alert system

GUI dashboard

Machine Learning anomaly detection

Automated PDF audit reports

Cloud storage monitoring

👨‍💻 Developed By

MUNI SAI DIVITH
Cybersecurity Intern – Unified Mentor
