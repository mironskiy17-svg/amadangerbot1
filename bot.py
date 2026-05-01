import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import requests

# ================== НАСТРОЙКИ ==================
TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
GROQ_API_KEY = "import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import requests

# ================== НАСТРОЙКИ ==================
TOKEN = "7625173287:AAHLZp-7hOly8t9Qbw_YT0V8536lXcBuX-Q"

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
GROQ_API_KEY = "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"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

MODEL = "llama-3.3-70b-versatile"

# ===============================================

def ask_groq(prompt: str, history=None) -> str:
    if history is None:
        history = []
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": "Ты весёлый, добрый и умный друг ребёнка 8 лет. Отвечай просто, весело, с эмодзи и по-детски."}
    ] + history + [{"role": "user", "content": prompt}]
    
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.8,
        "max_tokens": 700
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            return "Что-то пошло не так 😔 Попробуй ещё раз!"
    except:
        return "Не могу сейчас ответить... Попробуй позже!"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = []  # очищаем историю при /start
    
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
        "Привет! 👋 Я твой весёлый бот-друг!\nЧто хочешь сегодня сделать?",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    prompts = {
        "memes": "Придумай 3 смешные идеи для мемов...",
        "cartoons": "Порекомендуй 3 крутых мультика...",
        "jokes": "Расскажи 3 весёлые шутки...",
        "games": "Посоветуй 3 интересные игры...",
        "music": "Порекомендуй весёлую музыку...",
        "edu": "Предложи 3 развивающие занятия...",
    }
    
    prompt = prompts.get(query.data, "Расскажи что-то интересное!")
    
    await query.edit_message_text(text="⏳ Думаю...")
    
    answer = ask_groq(prompt, context.user_data.get("history", []))
    
    # Сохраняем в историю
    if "history" not in context.user_data:
        context.user_data["history"] = []
    context.user_data["history"].append({"role": "user", "content": prompt})
    context.user_data["history"].append({"role": "assistant", "content": answer})
    
    # Оставляем кнопки
    keyboard = [ ... ]  # (те же кнопки, как раньше)
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=answer, reply_markup=reply_markup)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    await update.message.reply_text("⏳ Думаю...")
    
    answer = ask_groq(user_message, context.user_data.get("history", []))
    
    # Сохраняем историю
    if "history" not in context.user_data:
        context.user_data["history"] = []
    context.user_data["history"].append({"role": "user", "content": user_message})
    context.user_data["history"].append({"role": "assistant", "content": answer})
    
    await update.message.reply_text(answer)


# ================== ЗАПУСК БОТА ==================
if __name__ == "__main__":
    if GROQ_API_KEY == "gsk_вставь_сюда_свой_ключ_полностью":
        print("❌ Ты забыл вставить свой Groq ключ!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
        print("✅ Бот успешно запущен!")
        app.run_polling()"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

MODEL = "llama-3.3-70b-versatile"

# ===============================================

def ask_groq(prompt: str, history=None) -> str:
    if history is None:
        history = []
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": "Ты весёлый, добрый и умный друг ребёнка 8 лет. Отвечай просто, весело, с эмодзи и по-детски."}
    ] + history + [{"role": "user", "content": prompt}]
    
    data = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.8,
        "max_tokens": 700
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"].strip()
        else:
            return "Что-то пошло не так 😔 Попробуй ещё раз!"
    except:
        return "Не могу сейчас ответить... Попробуй позже!"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = []  # очищаем историю при /start
    
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
        "Привет! 👋 Я твой весёлый бот-друг!\nЧто хочешь сегодня сделать?",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    prompts = {
        "memes": "Придумай 3 смешные идеи для мемов...",
        "cartoons": "Порекомендуй 3 крутых мультика...",
        "jokes": "Расскажи 3 весёлые шутки...",
        "games": "Посоветуй 3 интересные игры...",
        "music": "Порекомендуй весёлую музыку...",
        "edu": "Предложи 3 развивающие занятия...",
    }
    
    prompt = prompts.get(query.data, "Расскажи что-то интересное!")
    
    await query.edit_message_text(text="⏳ Думаю...")
    
    answer = ask_groq(prompt, context.user_data.get("history", []))
    
    # Сохраняем в историю
    if "history" not in context.user_data:
        context.user_data["history"] = []
    context.user_data["history"].append({"role": "user", "content": prompt})
    context.user_data["history"].append({"role": "assistant", "content": answer})
    
    # Оставляем кнопки
    keyboard = [ ... ]  # (те же кнопки, как раньше)
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=answer, reply_markup=reply_markup)


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    await update.message.reply_text("⏳ Думаю...")
    
    answer = ask_groq(user_message, context.user_data.get("history", []))
    
    # Сохраняем историю
    if "history" not in context.user_data:
        context.user_data["history"] = []
    context.user_data["history"].append({"role": "user", "content": user_message})
    context.user_data["history"].append({"role": "assistant", "content": answer})
    
    await update.message.reply_text(answer)


# ================== ЗАПУСК БОТА ==================
if __name__ == "__main__":
    if GROQ_API_KEY == "gsk_вставь_сюда_свой_ключ_полностью":
        print("❌ Ты забыл вставить свой Groq ключ!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
        print("✅ Бот успешно запущен!")
        app.run_polling()
