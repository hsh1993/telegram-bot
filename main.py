from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# جایگزین کردن با توکن ربات تلگرام
TOKEN = "7930892288:AAGwN_1zpzvDEvsiIPQRmPesNR-zZEGU0ms"

# این تابع برای پاسخ به دستور /start استفاده می‌شود
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من ربات تلگرام هستم.")

# این تابع برای پاسخ به تمام پیام‌ها استفاده می‌شود
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(f"شما گفتید: {update.message.text}")

# اصلی‌ترین تابع برای تنظیمات ربات
def main():
    # ایجاد اپدیت کننده برای ربات
    updater = Updater(TOKEN, use_context=True)
    
    # گرفتن دیسپاچر برای اضافه کردن هندلرها
    dispatcher = updater.dispatcher
    
    # اضافه کردن هندلر برای دستور /start
    dispatcher.add_handler(CommandHandler("start", start))
    
    # اضافه کردن هندلر برای پیام‌های متنی
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    # شروع ربات
    updater.start_polling()
    
    # منتظر ماندن تا ربات متوقف شود
    updater.idle()

# اجرای تابع اصلی
if __name__ == '__main__':
    main()