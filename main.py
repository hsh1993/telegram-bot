from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7930892288:AAGwN_1zpzvDEvsiIPQRmPesNR-zZEGU0ms"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من ربات تلگرام هستم.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"شما گفتید: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("ربات در حال اجرا است...")
    app.run_polling()

if __name__ == '__main__':
    main()
