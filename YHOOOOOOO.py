import yfinance as yf
import time
import telebot
import schedule

token = ""  # заполнить
bot = telebot.TeleBot(token)
chat_id = ""  # заполнить


def job():
    date = time.strftime("%Y-%m-%d", )
    data = yf.download("MSFT", start=date, end=date)
    bot.send_message(chat_id=chat_id, text=str(data["Close"]))
    return


schedule.every().day.at("02:42").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
