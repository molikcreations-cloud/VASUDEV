# Telegram TXT-to-Video/PDF Bot Repository

This repository contains the code for a Telegram bot that converts `.txt` files into **PDF** and **video** formats, now with added support for **thumbnails** and **captions**.

## 🧠 Features
- Convert uploaded `.txt` files to **PDF**.
- Convert `.txt` files to **videos** using text-to-speech (TTS).
- Add **custom thumbnails** and **captions** via `/setthumb` and `/setcaption` commands.
- Commands to clear them (`/clearthumb`, `/clearcaption`).
- Secure configuration using environment variables.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/telegram-txt2media-bot.git
cd telegram-txt2media-bot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔒 4. Add Your Bot Token Securely

Create a file named `.env` in the project’s root folder:
```bash
echo BOT_TOKEN=123456789:AAE-abcdefghijklmnoPQRSTUVWXYZ > .env
```
*(Replace with your actual token from @BotFather)*

Ensure `.env` is **not** uploaded to GitHub by adding this to `.gitignore`:
```
.env
```

---

## 🚀 5. Run the Bot
```bash
python bot.py
```

You should see a log message like:
```
Bot started successfully as @YourBotName
```

---

## 🧩 6. Available Commands
- `/start` → Welcome message.
- `/setcaption` → Set a custom caption for converted files.
- `/setthumb` → Upload a custom thumbnail for videos.
- `/clearthumb` → Remove your current thumbnail.
- `/clearcaption` → Remove your current caption.
- `/help` → Show command list.

---

## ☁️ Deployment Options
You can deploy this bot 24/7 using:
- [Render.com](https://render.com/)
- [Railway.app](https://railway.app/)
- [Replit](https://replit.com/)
- VPS or EC2 Instance

A sample `Dockerfile` is included for containerized deployment.

---

## 🧾 License
MIT License — free for personal and commercial use.
