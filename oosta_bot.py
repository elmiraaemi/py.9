import random
from datetime import date, datetime
import datetime
from khayyam import JalaliDate, JalaliDatetime
import qrcode
import gtts
import telebot
from telebot import types

bot = telebot.TeleBot("5818781749:AAF_8rhzUTcFGYu4kP60BcCrMLi8qtPeyV0", parse_mode=None)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('/QRcode')
itembtn2 = types.KeyboardButton('/game')
itembtn3 = types.KeyboardButton('/age')
itembtn4 = types.KeyboardButton('/voice')
itembtn5 = types.KeyboardButton('/max')
itembtn6 = types.KeyboardButton('/argmax')
itembtn7 = types.KeyboardButton('/help')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "  سلام" + message.from_user.first_name+ "عزیز" + "\n خوش اومدی جون دل", reply_markup=markup)

@bot.message_handler(commands=['QRcode'])
def crating_QRcode(message):
	text=bot.send_message(message.chat.id, "جمله ات چیه جون دل؟ ")
	bot.register_next_step_handler(text, crating_QRcode)
	
@bot.message_handler(commands=['game'])
def computer_namber(message):
	global nnamber
	nnamber = random.randint(0,5)
	bot.send_message(message.chat.id,"به بازی حدس عدد خوش اومدی"+"\n یک عدد بین 0 تا 5 حدس بزن جون دل")

@bot.message_handler(commands=['age'])
def user_birthday(message):
	brthdayy=bot.send_message(message.chat.id, "تاریخ تولت له ه.ش کیه جون دل(1320-04-21)")
	bot.register_next_step_handler(brthdayy, age_birthday)

@bot.message_handler(commands=['voice'])
def user_stering(message):
    text = bot.send_message(message.chat.id, "جمله ای که ویسش رو میخوای چیه جون دل؟ ")
    bot.register_next_step_handler( text, text_to_voice)   

@bot.message_handler(commands=['max'])
def user_namber_list(message):
	user_nambers=bot.send_message(message.chat.id, "اعداد لیست رو با استفاده از ',' از هم جدا کن")
	bot.register_next_step_handler(user_nambers, max_namber_list)
      
@bot.message_handler(commands=['argmax'])
def namber_list(message):
	user_nambers=bot.send_message(message.chat.id, "اعداد لیست رو با استفاده از ',' از هم جدا کن")
	bot.register_next_step_handler(user_nambers, argmax_namber_list)


@bot.message_handler(commands=['help'])
def help_user(message):
	bot.reply_to(message, "باتمون به ازای هر گزینه کار های مختلفی انجام میده که در ادامه برات اون هارو لیست میکنم")
	bot.send_message(message.chat.id, "QRcode  اوستا خلاف ازت یک جمله میگیره و تصویر کدکیوار اون رو ارسال میکنه"
				      	"\n age: با این انتخاب اوستا بات تاریخ روز تولت رو میگیره و دقیقا حساب میکنه چند سالته "
						"\n voice: اینو که بزنی بعدش باید یک جمله به انگلیسی تحویل اوستا بدی تا اونم ویس جمله ای که فرستادی رو بهت تحویل بده"
						"\n max: اینجای کار باید یک لیست از اعداد به اوستا خلاف تقدیم کنی, اوستا همه رو برای خودش نگه میداره ولی لطف میکنه و بهت بزرگ ترین عدد لیست رو بهت برمیگردونه"
						"\n argmax: دوباره ازت یک لیست از اعداد میگیره ولی این بار شماره خونه ی بزرگترین عدد رو میگه"
						"\n help: همینو زدی که مجبور شدم این همه حرف بزنم دیگه")
	
@bot.message_handler(func=lambda m: True)
def user_text(message):
	QR_text = message.text
	img = qrcode.make(QR_text)
	img.save("Qrcode.png")
	QRc = open("QrCode.jpg",'rb')
	bot.send_photo(message.chat.id, QRc, reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def user_namber(message):
    if nnamber > int(message.text) :
        bot.send_message(message.chat.id , "برو بالا تر")
    elif nnamber < int(message.text) :
        bot.send_message(message.chat.id , "بیا پایین تر") 
    elif nnamber == int(message.text) :
        bot.send_message(message.chat.id , "آفرین, برنده شدی", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def age_birthday(message):

    user_birthday = str(message.text)
    birthday_year = int(user_birthday.split("-")[0])
    birthday_month = int(user_birthday.split("-")[1])
    birthday_day = int(user_birthday.split("-")[2])
    miladi = JalaliDatetime(birthday_year, birthday_month, birthday_day).todate()
    dob = str(miladi)
    dob_date = datetime.date.fromisoformat(dob)
    today_date = datetime.date.today()
    age_timedelta = today_date - dob_date
    age_days=age_timedelta.days
    age_years=age_days // 365
    day2 = age_days - age_years*365
    age_month = day2 // 30
    month2=day2%30
    all = age_years,age_month,month2
    bot.reply_to(message, all, reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def text_to_voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("python\T9\Voice.mp3")
    voice_reader = open("python\T9\Voice.mp3", 'rb')
    bot.send_audio(message.chat.id , voice_reader, reply_markup=markup)        

@bot.message_handler(func=lambda m: True)
def max_namber_list(message):
    user_namber2 = str(message.text)
    nambers = user_namber2.split(" ")    
    list_namber=[]
    for namber in nambers :
        list_namber.append(namber)
    l=max(list_namber)
    bot.reply_to(message,l , reply_markup=markup)
    
@bot.message_handler(func=lambda m: True)
def argmax_namber_list(message):
    user_namber2 = message.text
    list_namber=[]
    nambers = user_namber2.split(" ")
    for namber in nambers :
        list_namber.append(namber)
    bot.reply_to(message, list_namber.index(max(list_namber)), reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "ok", reply_markup=markup)
	
bot.infinity_polling()