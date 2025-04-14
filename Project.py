from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Ganti dengan token yang Anda dapatkan dari BotFather
TOKEN = 'YOUR_BOT_TOKEN'

def start(update, context):
    update.message.reply_text('Hello, I am your bot!')

def main():
    # Membuat objek Updater dengan token Anda
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Mulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()