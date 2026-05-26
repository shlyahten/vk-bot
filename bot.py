import os
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text

bot = Bot(os.environ["VK_GROUP_TOKEN"])

# Собираем клавиатуру
def main_keyboard():
    return (
        Keyboard(one_time=False, inline=False)
        .add(Text("🌤 Погода"), color=KeyboardButtonColor.PRIMARY)
        .add(Text("📰 Новости"), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Text("⚙️ Настройки"), color=KeyboardButtonColor.SECONDARY)
        .add(Text("❓ Помощь"), color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text("🚫 Убрать клавиатуру"), color=KeyboardButtonColor.NEGATIVE)
    )

def empty_keyboard():
    return Keyboard(one_time=True)  # пустая — скрывает клавиатуру


# Старт — показываем клавиатуру
@bot.on.message(text=["Начать", "Старт", "/start"])
async def start_handler(message: Message):
    await message.answer(
        "Привет! Выбери действие 👇",
        keyboard=main_keyboard()
    )

# Обработка кнопок
@bot.on.message(text="🌤 Погода")
async def weather_handler(message: Message):
    await message.answer("Сегодня солнечно, +22°C ☀️")

@bot.on.message(text="📰 Новости")
async def news_handler(message: Message):
    await message.answer("Новостей пока нет 📭")

@bot.on.message(text="⚙️ Настройки")
async def settings_handler(message: Message):
    await message.answer("Настройки пока недоступны 🔧")

@bot.on.message(text="❓ Помощь")
async def help_handler(message: Message):
    await message.answer(
        "Доступные кнопки:\n"
        "🌤 Погода — прогноз\n"
        "📰 Новости — последние события\n"
        "⚙️ Настройки — конфигурация\n"
        "🚫 Убрать клавиатуру — скрыть панель"
    )

@bot.on.message(text="🚫 Убрать клавиатуру")
async def hide_keyboard_handler(message: Message):
    await message.answer("Клавиатура скрыта. Напиши «начать» чтобы вернуть.", keyboard=empty_keyboard())

# Fallback
@bot.on.message()
async def fallback_handler(message: Message):
    await message.answer(
        "Не понял тебя 🤔 Напиши «начать»",
        keyboard=main_keyboard()
    )

bot.run_forever()