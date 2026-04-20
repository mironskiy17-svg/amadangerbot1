import os
import google.generativeai as genai
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"
GEMINI_KEY = os.environ.get("AIzaSyDOMhuvvK2fdqMCoF8msiBKu_VayOpivjE")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

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
        "cartoons": "Ты эксперт по мультикам для детей 8 лет. Порекомендуй 3 классных мультика или серии которые сейчас популярны. Каждый раз давай разные рекомендации!",
        "jokes": "Расскажи 3 смешные детские шутки или анекдота для ребёнка 8 лет. Каждый раз новые и разные!",
        "games": "Посоветуй 3 классные игры для ребёнка 8 лет. Можно мобильные или компьютерные. Каждый раз разные советы!",
        "music": "Порекомендуй весёлую детскую музыку или песни для ребёнка 8 лет. Каждый раз новые рекомендации!",
        "edu": "Предложи 3 интересные развивающие активности или игры для ребёнка 8 лет. Каждый раз разные и творческие!",
    }

    prompt = prompts.get(query.data, "Расскажи что-то интересное для ребёнка 8 лет!")

    await query.edit_message_text(text="⏳ Думаю...")

    response = model.generate_content(prompt)
    answer = response.text

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
    response = model.generate_content(prompt)
    await update.message.reply_text(response.text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
