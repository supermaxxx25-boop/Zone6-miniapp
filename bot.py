import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛒 Ouvrir la mini-app",
                web_app=WebAppInfo(url="https://TON-PROJET.up.railway.app")
            )
        ]
    ]

    await update.message.reply_text(
        "👋 Bienvenue dans la Zone6 👽\nClique ci-dessous 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(
        f"📦 Données reçues depuis la mini-app :\n{data}"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data)
    )

    print("🤖 Bot lancé")
    app.run_polling()

if __name__ == "__main__":
    main()
