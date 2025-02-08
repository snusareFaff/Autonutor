import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import g4f
from pyrogram import Client, filters as pyro_filters
import subprocess
import sys

# Logging setting
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Replace 'your_telegram_bot_token' with your real token
TELEGRAM_BOT_TOKEN = 'if you have telegram bot, set token'

# Replace 'your_api_id' and 'your_api_hash' for your values ​​from my.telegram.org
API_ID = 'your-id'
API_HASH = 'your-hash'

# Replace 'your_Session_string' with your session line
SESSION_STRING = 'Read the installation guide'

# Replace 'your_user_id' with your real ID user Telegram
YOUR_USER_ID = 'your-id'

# Dictionary for storing the context of conversation
conversation_context = {}

# Examples of your messages for emulating the manner of speech
EXAMPLE_MESSAGES = [
    'Use this to give neural networks examples of your messages'
]

# Pyrogram client initialization
app = Client("my_account", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(pyro_filters.private & pyro_filters.incoming)
async def handle_private_message(client, message):
    user_id = message.from_user.id
    text = message.text
    logger.info(f"Received private message: {text} from {message.from_user.first_name}")

    # Add the user's message to the context of the conversation
    if user_id not in conversation_context:
        conversation_context[user_id] = []
    conversation_context[user_id].append(f"User: {text}")

    # We form the input text for the model
    messages = [
        {"role": "system", "content": "example prompt"},
        {"role": "system", "content": "\n".join(EXAMPLE_MESSAGES)}
    ] + [
        {"role": "user", "content": msg.split(": ")[1]} if "User:" in msg else {"role": "assistant", "content": msg.split(": ")[1]}
        for msg in conversation_context[user_id]
    ]

    try:
        # We generate the answer using the model
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=messages,
            stream=False
        )
        generated_text = response
        logger.info(f"Generated response: {generated_text}")

        # Add the answer to the model to the context of the conversation
        conversation_context[user_id].append(f"Bot: {generated_text}")

        # We send an answer to the user on your behalf
        await client.send_message(user_id, generated_text)
    except Exception as e:
        logger.error(f"Failed to generate response: {e}")
        await client.send_message(user_id, "There was an error when generating an answer.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    conversation_context[user_id] = []
    logger.info(f"Received /start command from {update.effective_user.first_name}")
    await update.message.reply_text('Hi')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    message = update.message.text
    logger.info(f"Received message: {message} from {update.effective_user.first_name}")

    if user_id not in conversation_context:
        conversation_context[user_id] = []
    conversation_context[user_id].append(f"User: {message}")

    messages = [
        {"role": "system", "content": "example prompt"},
        {"role": "system", "content": "\n".join(EXAMPLE_MESSAGES)}
    ] + [
        {"role": "user", "content": msg.split(": ")[1]} if "User:" in msg else {"role": "assistant", "content": msg.split(": ")[1]}
        for msg in conversation_context[user_id]
    ]

    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=messages,
            stream=False
        )
        generated_text = response
        logger.info(f"Generated response: {generated_text}")

        conversation_context[user_id].append(f"Bot: {generated_text}")

        await update.message.reply_text(generated_text)
    except Exception as e:
        logger.error(f"Failed to generate response: {e}")
        await update.message.reply_text("There was an error when generating an answer.")


def main() -> None:
    try:
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
        logger.info("Application built successfully.")
    except Exception as e:
        logger.error(f"Failed to build application: {e}")
        exit(1)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logger.info("Starting polling...")
    application.run_polling()

if __name__ == '__main__':
    # Launch a Pyrogram client
    app.start()
    # Launch the bot
    main()