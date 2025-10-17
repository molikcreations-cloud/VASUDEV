import os
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client('txt2media_bot', bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("👋 Welcome! Send me a .txt file to convert into PDF or Video.")

if __name__ == "__main__":
    app.run()
