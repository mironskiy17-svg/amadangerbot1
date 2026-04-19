from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"

async def answer(update, context):
    await update.message.reply_text("Привет! Я твой бот 🤖")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, answer))
app.run_polling()
