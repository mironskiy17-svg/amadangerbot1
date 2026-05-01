from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"
GROQ_API_KEY = "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"

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "Ты весёлый и добрый друг ребёнка 8 лет. Отвечай просто и с эмодзи."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
    try:
        r = requests.post(url, headers=headers, json=data, timeout=12)
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "Извини, я сейчас немного устал 😔 Попробуй ещё раз!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("😂 Мемы", callback_data="memes")],
        [InlineKeyboardButton("📺 Мультики", callback_data="cartoons")],
        [InlineKeyboardButton("😄 Шутки", callback_data="jokes")]
    ]
    await update.message.reply_text("Привет! 👋 Я твой бот-друг!\nНажми кнопку:", 
                                  reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("⏳ Думаю...")
    
    answer = ask_groq("Расскажи что-то весёлое для ребёнка 8 лет")
    await query.edit_message_text(answer)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = ask_groq(update.message.text)
    await update.message.reply_text(answer)

# Запуск бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("✅ Бот запущен успешно!")
app.run_polling()
