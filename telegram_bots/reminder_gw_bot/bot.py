from telegram.ext import Updater, CommandHandler
import os
from dotenv import load_dotenv, find_dotenv
from command_handlers import (
    help_command_handler,
)

load_dotenv(find_dotenv())

def get_text_from_callback(update):
    return update.callback_query.data


def main():
    updater = Updater(os.environ.get("TELEGRAM_TOKEN", ""), use_context=True)
    dp = updater.dispatcher
    # command handlers
    dp.add_handler(CommandHandler("help", help_command_handler))
    dp.add_handler(CommandHandler("start", help_command_handler))

    # send chat
    dp.bot.send_message(os.environ.get("MY_CHAT_ID", ""), "Hello World!")
    print("DONE!")

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    main()
