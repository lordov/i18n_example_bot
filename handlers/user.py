from aiogram import F, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.i18n import gettext as _

# Инициализируем роутер уровня модуля
user_router = Router()


# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):
    username = html.quote(message.from_user.full_name)
    # Создаем объект инлайн-кнопки
    button = InlineKeyboardButton(
        text=_('Кнопка'),
        callback_data='button_pressed'
    )
    # Создаем объект инлайн-клавиатуры
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])

    # Отправляем сообщение пользователю
    await message.answer(
        text=_('Привет, {username}. Нажмите на кнопку').format(
            username=username),
        reply_markup=markup
    )


# Этот хэндлер срабатывает на команду /help
@user_router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(
        text=_('Это бот для демонстрации процесса интернационализации\n\n'
               'Доступные команды:\n\n'
               '/start - перезапуск бота'
               '/help - справка по работе бота')
    )


# Этот хэндлер срабатывает на нажатие инлайн-кнопки
@user_router.callback_query(F.data == 'button_pressed')
async def process_button_click(callback: CallbackQuery):
    await callback.answer(text=_('Вы нажали на кнопку!'))
