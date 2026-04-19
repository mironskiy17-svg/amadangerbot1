import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get 7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q

# Меню с кнопками
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
        "Привет! 👋 Я твой весёлый бот!\nЧто хочешь найти?",
        reply_markup=reply_markup
    )

# Ответы на кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    links = {
        "memes": (
            "😂 Вот смешные мемы для тебя!\n\n"
            "🔗 https://www.youtube.com/results?search_query=смешные+мемы+для+детей\n"
            "🔗 https://www.youtube.com/results?search_query=funny+memes+for+kids"
        ),
        "cartoons": (
            "📺 Новые мультики!\n\n"
            "🔗 https://www.youtube.com/results?search_query=тресковые+мультики+новые+серии\n"
            "🔗 https://www.youtube.com/results?search_query=мультфильмы+2024+для+детей"
        ),
        "jokes": (
            "😄 Смешные шутки!\n\n"
            "🔗 https://www.youtube.com/results?search_query=детские+шутки+смешные\n"
            "🔗 https://www.youtube.com/results?search_query=анекдоты+для+детей"
        ),
        "games": (
            "🎮 Игры для детей!\n\n"
            "🔗 https://www.youtube.com/results?search_query=лучшие+игры+для+детей+8+лет\n"
            "🔗 https://poki.com/ru"
        ),
        "music": (
            "🎵 Детская музыка!\n\n"
            "🔗 https://www.youtube.com/results?search_query=весёлые+детские+песни\n"
            "🔗 https://www.youtube.com/results?search_query=детская+музыка+2024"
        ),
        "edu": (
            "🧠 Развивашки и обучалки!\n\n"
            "🔗 https://www.youtube.com/results?search_query=развивающие+мультики+8+лет\n"
            "🔗 https://learningapps.org"
        ),
    }

    # Снова показываем меню
    keyboard = [
        [InlineKeyboardButton("😂 Мемы", callback_data="memes"),
         InlineKeyboardButton("📺 Мультики", callback_data="cartoons")],
        [InlineKeyboardButton("😄 Шутки", callback_data="jokes"),
         InlineKeyboardButton("🎮 Игры", callback_data="games")],
        [InlineKeyboardButton("🎵 Музыка", callback_data="music"),
         InlineKeyboardButton("🧠 Развивашки", callback_data="edu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=links.get(query.data, "Не нашёл 😢"),
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
