# Simple Insta Downloader

A lightweight Telegram bot to download Instagram posts directly via chat.

## Features

* Download Instagram posts using a Telegram bot.
* Simple and minimal setup.

## Requirements

* Python 3.7+
* [Telegram Bot Token](https://core.telegram.org/bots#6-botfather)
* [Google Chrome](https://www.google.com/chrome/) and [ChromeDriver](https://chromedriver.chromium.org/downloads)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ParsaTB/Simple-Insta-Downloader.git
   cd Simple-Insta-Downloader
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Change the bot token in `.env`:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   ```

   Replace `your_telegram_bot_token` with your actual Telegram bot token.

5. **Ensure ChromeDriver is installed and added to your system's PATH.**

## Usage

Start the bot:

```bash
python bot.py
```

Once running, send an Instagram post URL to your Telegram bot, and it will respond with the downloaded content.

## License

This project is licensed under the MIT License.
