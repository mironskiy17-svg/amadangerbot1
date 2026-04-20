import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"
GEMINI_KEY = os.environ.get("AIzaSyDOMhuvvK2fdqMCoF8msiBKu_VayOpivjE")

def ask_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, json=data)
    result = response.json()
    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    elif "error" in result:
        return f"Ошибка: {result['error']['message']}"
    else:
        return str(result)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("😂 Мемы", callback_data="memes"),
         InlineKeyboardButton("📺 Мультики", callback_data="cartoons")],
        [InlineKeyboardButton("😄 Шутки", callback_data="jokes"),
         InlineKeyboardButton("🎮 Игры", callback_data="games")],
        [InlineKeyboardButton("🎵 Музыка", callback_data="music"),
         InlineKeyboardButton("🧠 Развивашки", callback_data="edu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! 👋 Я твой умный бот!\nЧто хочешь найти?",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    prompts = {
        "memes": "Ты весёлый друг ребёнка 8 лет. Расскажи 3 смешные идеи для мемов для детей. Будь креативным и каждый раз разным!",
        "cartoons": "Ты эксперт по мультикам для детей 8 лет. Порекомендуй 3 классных мультика которые сейчас популярны. Каждый раз давай разные рекомендации!",
        "jokes": "Расскажи 3 смешные детские шутки для ребёнка 8 лет. Каждый раз новые и разные!",
        "games": "Посоветуй 3 классные игры для ребёнка 8 лет. Каждый раз разные советы!",
        "music": "Порекомендуй весёлую детскую музыку для ребёнка 8 лет. Каждый раз новые рекомендации!",
        "edu": "Предложи 3 интересные развивающие игры для ребёнка 8 лет. Каждый раз разные и творческие!",
    }
    prompt = prompts.get(query.data, "Расскажи что-то интересное для ребёнка 8 лет!")
    await query.edit_message_text(text="⏳ Думаю...")
    answer = ask_gemini(prompt)
    keyboard = [
        [InlineKeyboardButton("😂 Мемы", callback_data="memes"),
         InlineKeyboardButton("📺 Мультики", callback_data="cartoons")],
        [InlineKeyboardButton("😄 Шутки", callback_data="jokes"),
         InlineKeyboardButton("🎮 Игры", callback_data="games")],
        [InlineKeyboardButton("🎵 Музыка", callback_data="music"),
         InlineKeyboardButton("🧠 Развивашки", callback_data="edu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=answer, reply_markup=reply_markup)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    prompt = f"Ты весёлый и умный друг ребёнка 8 лет. Отвечай просто, весело и интересно. Вопрос: {user_message}"
    answer = ask_gemini(prompt)
    await update.message.reply_text(answer)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
