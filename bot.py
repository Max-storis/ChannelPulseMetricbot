import os
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

# Настройка логов
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    """Команда /start с кнопками"""
    keyboard = [
        [InlineKeyboardButton("✨ Получить демо-доступ", callback_data='demo')],
        [InlineKeyboardButton("📊 Проанализировать канал", url='https://channelpulsemetric.onrender.com')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🚀 *ChannelPulseMetric* — аналитика для Telegram-каналов\n\n"
        "✅ Автоматические отчёты за 60 секунд\n"
        "✅ Персональные рекомендации для роста\n"
        "✅ Подходит для ЛЮБОГО канала\n\n"
        "Выберите действие:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def demo_access(update, context):
    """Выдача демо-доступа"""
    query = update.callback_query
    await query.answer()
    
    # Генерируем простой код (в реальности — база данных)
    demo_code = "DEMO-2026-01-18"
    
    await query.edit_message_text(
        f"✅ *Демо-аккаунт создан!*\n\n"
        f"🔑 **Код активации:** `{demo_code}`\n"
        f"⏳ **Срок действия:** 3 дня\n\n"
        f"👉 Перейдите в сервис и введите код:\n"
        f"https://channelpulsemetric.onrender.com\n\n"
        f"💡 *Для теста используйте канал @habr_com*",
        parse_mode="Markdown"
    )

def main():
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(demo_access, pattern='demo'))
    
    # Запускаем бота
    print("✅ Бот запущен! Открой Telegram → @ChannelPulseMetric_bot")
    application.run_polling()

if __name__ == "__main__":
    main()
