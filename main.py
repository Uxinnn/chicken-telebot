from telegram.ext import Updater, CommandHandler
from chickens import chickens


BOT_TOKEN = "1717925286:AAG_xwawfM5F_etdT_sc-svWAA7Ads9kHS0"


def start(update, context):
    context.jobs_queue.run_once(send_chicken, 5)
    context.job_queue.run_repeating(send_chicken, 300, context=update.message.chat_id)
    return


def send_chicken(context):
    context.bot.send_photo(chat_id=context.job.context, photo=chickens[0])


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
