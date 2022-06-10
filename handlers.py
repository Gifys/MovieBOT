from aiogram import types


from main import bot, dp
from keybords import greet_kb, otherMenu, greet_zoloto, greet_zoloto1, greet_zoloto2
from parser import playbill
from config import Rio_photo, Empire_of_Dreams_photo, Petrel_photo, my_vk_url



#arr= ['3008946','8320137','8151399']
#arr[0] = ЗМ, arr[1] = Буревестник, arr[2] = РИО
#Теги для сайта

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    if msg.text.lower() == '/start' or 'start':
      await bot.send_photo(msg.from_user.id, 'https://i.pinimg.com/474x/99/d4/69/99d4693a780debeaac15a5518832d780.jpg')
      await msg.answer('Итак, начнем!', reply_markup=greet_kb)
    elif msg.text.lower() == '/help' or 'help':
        await msg.answer('Бог поможет!')

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'давай знакомица!':
       await bot.send_message(msg.from_user.id, f'Привет, {msg.from_user.first_name}. Меня зовут Бот. Чувство юмора у моих создателей, конечно, присутствует.\n\n'
                                                ' Я был создан для того, чтобы показывать афишу Нижегородских кинотеатров. Если что, вот мой создатель'
                                                f' {my_vk_url}')
   elif msg.text.lower() == 'выбор кинотеатра:':
       await bot.send_message(msg.from_user.id, 'Смотри :)', reply_markup = otherMenu)
   elif msg.text.lower() == 'главное меню':
       await bot.send_message(msg.from_user.id, 'Окей!', reply_markup = greet_kb)


   elif msg.text.lower() == 'золотая миля':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto)
   elif msg.text.lower() == 'расположение зм:':
       await bot.send_photo(msg.from_user.id, Empire_of_Dreams_photo)
       await bot.send_message(msg.from_user.id, 'ул. Коминтерна, 105, Нижний Новгород.')
   elif msg.text.lower() == 'афиша зм:':
        await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
        await bot.send_message(msg.from_user.id, playbill("Empire_of_Dreams"))


   elif msg.text.lower() == 'буревестник':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto1)
   elif msg.text.lower() == 'расположение бв:':
       await bot.send_photo(msg.from_user.id, Petrel_photo)
       await bot.send_message(msg.from_user.id, 'ул. Коминтерна, 244, Нижний Новгород, Нижегородская обл.')
   elif msg.text.lower() == 'афиша бв:':
       await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
       await bot.send_message(msg.from_user.id, playbill("Petrel"))


   elif msg.text.lower() == 'трц рио':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto2)
   elif msg.text.lower() == 'расположение рио:':
       await bot.send_photo(msg.from_user.id, Rio_photo)
       await bot.send_message(msg.from_user.id, 'Московское ш., 12, Нижний Новгород')
   elif msg.text.lower() == 'афиша рио:':
       await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
       await bot.send_message(msg.from_user.id, playbill("Rio"))


   else:
       await msg.answer('Бип-буп-бип... Не понимаю, что ты пишешь...')

