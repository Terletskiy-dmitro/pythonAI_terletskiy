# https://web.telegram.org/k/#@pythonAI_terletskiy_bot
from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
import random


url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

# print(links_list)
f = open('info.txt', 'w', encoding='utf-8')
list_name = []
list_desc = []
list_year = []

for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0])
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)

f.close()
command = """/help – список всіх команд бота
/hello – привітання,
/film – список найновіших фільмів,
/about - інформація про бота та розробника
/jokes - жарти:)
/time - поточний час у Києві
/day_of_week - індикує чи будень сьогодні, чи вихідний
/daily_forecast - вибирає який у тебе сьогодні день"""


about_bot = 'Цей бот створений учнем ІТ СТЕП академії, зараз розробник у 7 класі, і навчається кодити.'

jokes_list = ["Що каже Python, коли бачить баг? – «Try except!»",
    "Мамо, я програміст! – Повернись у свій підвал.",
    "Як звуть айтішника в армії? — Сержант.Рар.",
    "У тебе є дівчина? — Є, в базі даних.",
    "Якщо довго не комітиш, починаєш сумніватись у собі."]

forecasts = ["Сьогодні буде все погано, ну ніічого",
             "Сьогодні буде чудовий день, усе буде ок",
             "Цей день принесе тобі несподівані сюрпризи, будь готовий"]

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f'{list_name[i]}\n{list_desc[i]}\n{links_list[i]}'
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)

# ----------------------------------------------------------------

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{about_bot}')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    current_time = datetime.utcnow()
    current_time = current_time.replace(hour=current_time.hour + 3)
    await update.message.reply_text(f'Поточний час у Києві: {current_time.strftime("%H:%M:%S")}')

async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_joke = random.choice(jokes_list)
    await update.message.reply_text(random_joke)

async def day_of_week(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    today = datetime.today()
    day = today.strftime("%A")
    is_weekend = "Так" if day in ["Saturday", "Sunday"] else "Ні"
    await update.message.reply_text(f"Сьогодні {day}. Вихідний? {is_weekend}")

async def daily_forecast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    forecast = random.choice(forecasts)
    await update.message.reply_text(f"Прогноз на день: {forecast}")

app = ApplicationBuilder().token("7724660147:AAGgXJcMjwnQrX1YPXp_UpDEXupqYifjG6M").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))

# ----------------------------мої 5----------------------------

app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("jokes", jokes))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("day_of_week", day_of_week))
app.add_handler(CommandHandler("daily_forecast", daily_forecast))

app.run_polling()