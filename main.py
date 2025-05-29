#!/usr/bin/env python3
import os
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot_handlers import start_handler, message_handler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Get bot token from environment variable with fallback
    bot_token = os.getenv("BOT_TOKEN", "7844826848:AAGvV8ZKdZ3fsa1Amy3NRln_11L7yVCDxT4")
    
    # Create the Application
    application = Application.builder().token(bot_token).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    # Start the bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    main()
