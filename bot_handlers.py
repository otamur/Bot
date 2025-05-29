from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from messages import (
    WELCOME_MESSAGE,
    RANK_PRICES,
    KIT_PRICES,
    KEYS_PRICES,
    ADMIN_MESSAGE
)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    keyboard = [
        [KeyboardButton("💎RANK"), KeyboardButton("🛡 KIT")],
        [KeyboardButton("🗝 KEYS"), KeyboardButton("🛠 ADMIN")]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular text messages."""
    text = update.message.text
    
    # Create main menu keyboard
    keyboard = [
        [KeyboardButton("💎RANK"), KeyboardButton("🛡 KIT")],
        [KeyboardButton("🗝 KEYS"), KeyboardButton("🛠 ADMIN")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    if text == "💎RANK":
        await update.message.reply_text(
            text=RANK_PRICES,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    
    elif text == "🛡 KIT":
        await update.message.reply_text(
            text=KIT_PRICES,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    
    elif text == "🗝 KEYS":
        await update.message.reply_text(
            text=KEYS_PRICES,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    
    elif text == "🛠 ADMIN":
        await update.message.reply_text(
            text=ADMIN_MESSAGE,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )