from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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
