import os
from telethon import TelegramClient, events

# load environment variables from .env (install python-dotenv with pip if you haven't)
# pip install python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv()  # reads .env file in current directory
except ImportError:
    pass  # dotenv is optional; env vars can be set by the environment

# Credentials are sourced from environment variables for security
api_id = int(os.environ.get("API_ID", 0))          # set API_ID in env
api_hash = os.environ.get("API_HASH", "")        # set API_HASH in env
session_path = os.environ.get("SESSION_PATH", "session_name")

# client = TelegramClient(session_path, api_id, api_hash)
client = TelegramClient("railway_session", api_id, api_hash)

keywords = ["internship", "hiring", "vacancy"]

@client.on(events.NewMessage)
async def handler(event):
    try:
        message = event.raw_text.lower()
        chat = await event.get_chat()
        
        for word in keywords:
            if word in message:
                await client.send_message(
                    "me",  # sends message to yourself
                    f"\U0001F514 Keyword '{word}' found!\n"
                    f"\U0001F4E2 Channel/Group: {getattr(chat, 'title', 'Private Chat')}\n\n"
                    f"{event.raw_text}"
                )
                break
    except Exception as e:
        print("Error:", e)

client.start()
print("Bot is running...")
client.run_until_disconnected()

