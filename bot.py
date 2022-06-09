from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from bs4 import BeautifulSoup as BS

btnMain = KeyboardButton('Главное меню')
#---Main Menu---
#one_time_keyboard=True
btnHello = KeyboardButton("Давай знакомица!")
btnOther = KeyboardButton('Выбор кинотеатра:')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHello, btnOther)

#---Меню кинотеатров---
btnZoloto = KeyboardButton('Золотая Миля')
btn7nebo = KeyboardButton('Буревестник')
btnRIO = KeyboardButton('ТРЦ РИО')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnZoloto,btn7nebo,btnRIO, btnMain)

#---Золотая Миля---
btnInfo = KeyboardButton('Расположение ЗМ:')
btnAfisha = KeyboardButton('Афиша ЗМ:')
greet_zoloto = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAfisha, btnInfo, btnMain)

#---Седьмое Небо---
btnInfo1 = KeyboardButton('Расположение БВ:')
btnAfisha1 = KeyboardButton('Афиша БВ:')
greet_zoloto1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAfisha1, btnInfo1, btnMain)

#---ТРЦ РИО---
btnInfo2 = KeyboardButton('Расположение РИО:')
btnAfisha2 = KeyboardButton('Афиша РИО:')
greet_zoloto2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAfisha2, btnInfo2, btnMain)

TOKEN = "Your_Token"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

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
       await bot.send_message(msg.from_user.id, 'Давай {0.first_name}. Меня зовут Бот. Чувство юмора у моих создателей, конечно, присутствует.'
                                                ' Я был создан для того, чтобы показывать афишу Нижегородских кинотеатров. Если что, вот мой создатель'
                                                ' https://vk.com/misterigortrif'.format(msg.from_user))
   elif msg.text.lower() == 'выбор кинотеатра:':
       await bot.send_message(msg.from_user.id, 'Смотри :)', reply_markup = otherMenu)
   elif msg.text.lower() == 'главное меню':
       await bot.send_message(msg.from_user.id, 'Окей!', reply_markup = greet_kb)
   elif msg.text.lower() == 'золотая миля':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto)
   elif msg.text.lower() == 'расположение зм:':
       await bot.send_photo(msg.from_user.id, 'https://lh5.googleusercontent.com/p/AF1QipNcfJCgrYJEn44BicQG1xJUeoOCo6KFPvZVZHZb=w408-h306-k-no')
       await bot.send_message(msg.from_user.id, 'ул. Коминтерна, 105, Нижний Новгород.')
   elif msg.text.lower() == 'афиша зм:':
       # -------Парсер--------
        kino = ''
        r = requests.get('https://nn.kinoafisha.info/cinema/3008946/schedule/?date=&order=movie')
        html = BS(r.content, 'html.parser')
        items = html.select(".schedule_showtimes > .showtimes_item > .showtimes_cell > .showtimesMovie_wrapper")
        for el in items:
           title = el.select(".showtimesMovie_info > span")
           kino += str(title[0].text) + str('\n')
           if kino == '':
               kino = 'Кажется нет расписания...'
        #---------------------
        await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
        await bot.send_message(msg.from_user.id, kino)
   elif msg.text.lower() == 'буревестник':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto1)
   elif msg.text.lower() == 'расположение бв:':
       await bot.send_photo(msg.from_user.id, 'https://s3.afisha.ru/mediastorage/5f/b8/378471136225414b9df6fa61b85f.jpg')
       await bot.send_message(msg.from_user.id, 'ул. Коминтерна, 244, Нижний Новгород, Нижегородская обл.')
   elif msg.text.lower() == 'афиша бв:':
       # -------Парсер--------
       kino = ''
       r = requests.get('https://nn.kinoafisha.info/cinema/8320137/schedule/?date=&order=movie')
       html = BS(r.content, 'html.parser')
       items = html.select(".schedule_showtimes > .showtimes_item > .showtimes_cell > .showtimesMovie_wrapper")
       for el in items:
           title = el.select(".showtimesMovie_info > span")
           kino += str(title[0].text) + str('\n')
       if kino == '':
          kino = 'Кажется нет расписания...'
        #---------------------
       await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
       await bot.send_message(msg.from_user.id, kino)
   elif msg.text.lower() == 'трц рио':
       await bot.send_message(msg.from_user.id, 'Хороший выбор!', reply_markup = greet_zoloto2)
   elif msg.text.lower() == 'расположение рио:':
       await bot.send_photo(msg.from_user.id, 'https://www.be-in.ru/media/beingallery/uploads/mall/2016/07/28/rio-leninskiy-moskva.jpg')
       await bot.send_message(msg.from_user.id, 'Московское ш., 12, Нижний Новгород')
   elif msg.text.lower() == 'афиша рио:':
       # -------Парсер--------
       kino = ''
       r = requests.get('https://nn.kinoafisha.info/cinema/8151399/schedule/?date=&order=movie')
       html = BS(r.content, 'html.parser')
       items = html.select(".schedule_showtimes > .showtimes_item > .showtimes_cell > .showtimesMovie_wrapper")
       for el in items:
           title = el.select(".showtimesMovie_info > span")
           kino += str(title[0].text) + str('\n')
           if kino == '':
               kino = 'Кажется нет расписания...'
        #---------------------
       await bot.send_message(msg.from_user.id, 'Смотри! Сегодня у нас будут...')
       await bot.send_message(msg.from_user.id, kino)
   else:
       await msg.answer('Бип-буп-бип... Не понимаю, что ты пишешь...')


if __name__ == '__main__':
   executor.start_polling(dp)