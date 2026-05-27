# 📸 HDR Telegram Bot

A Telegram bot that applies HDR enhancement to any image you send it.

## How it works

Send a photo to the bot → it applies an HDR detail enhancement effect → sends back the transformed image.

## Tech Stack

- **Python** — `python-telegram-bot`, `opencv-python`
- **dotenv** — for secure token management
- Deployable via **Heroku** (Procfile included)

## Getting Started

```bash
git clone https://github.com/rudy002/HDRTelegramBot.git
cd HDRTelegramBot
pip install -r requirements.txt
```

Create a `.env` file:
```env
BOT_TOKEN=your_telegram_bot_token
```

```bash
python bot.py
```

## Usage

1. Start the bot with `/start`
2. Send any photo
3. Receive your HDR-enhanced image instantly
