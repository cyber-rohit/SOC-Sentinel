# 🔐 SOC-Sentinel
![Python](https://img.shields.io/badge/Python-3.x-blue)
Real-Time Brute Force Detection Tool (SOC Project)

## 🚀 Overview
SOC-Sentinel is a Python-based real-time log monitoring tool that detects brute force login attempts from system logs.

## ⚙️ Features
- Real-time monitoring of /var/log/auth.log
- Detects multiple failed login attempts
- Extracts attacker IP address
- Triggers alert after threshold
- Colored terminal alerts for visibility

## 🧪 Lab Setup
- Attacker: Kali Linux (Hydra)
- Victim: Ubuntu (SSH enabled)
- Logs monitored: /var/log/auth.log

## ⚡ How It Works
1. Monitor auth.log in real-time
2. Detect "Failed password" entries
3. Extract IP using regex
4. Count attempts per IP
5. Trigger alert if attempts ≥ 5

## 🛠️ Usage
python3 monitor.py

## 📸 Output Screenshots

![Step 1](https://raw.githubusercontent.com/cyber-rohit/SOC-Sentinel/main/S1.PNG)


![Step 2](https://raw.githubusercontent.com/cyber-rohit/SOC-Sentinel/main/S2.PNG)


![Step 3](https://raw.githubusercontent.com/cyber-rohit/SOC-Sentinel/main/S3.PNG)

