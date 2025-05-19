
import os
import time
import random
import string
import telebot
import threading

TOKEN = "7866943425:AAGGfXJ1C5rDw8tu3hMldHKOTV6oPP2OEmI"
OWNER_ID = 1104397846

bot = telebot.TeleBot(TOKEN)
stats_file = "eizonhits.txt"
running_process = False
infoinsta = {}
total_hits = 0

def InfoAcc(username, domain):
    global total_hits
    total_hits += 1
    result = f"""
صيد جديد ✅
عدد المتاحات: {total_hits}
يوزر: {username}
إيميل: {username}@{domain}
متابعين: {random.randint(10, 500)}
يتابع: {random.randint(10, 300)}
منشورات: {random.randint(1, 50)}
بايو: حساب تجريبي
"""
    with open(stats_file, 'a', encoding='utf-8') as f:
        f.write(result + "\n")
    print(result)

def scanner():
    while running_process:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        InfoAcc(username, 'gmail.com')
        time.sleep(2)

def send_stats(chat_id):
    last_sent = ""
    while running_process:
        if os.path.exists(stats_file):
            with open(stats_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            if lines:
                last = lines[-1]
                if last != last_sent:
                    try:
                        bot.send_message(chat_id, f"صيد جديد:\n{last}")
                        last_sent = last
                    except:
                        pass
        time.sleep(5)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    global running_process
    if message.chat.id != OWNER_ID:
        bot.send_message(message.chat.id, "❌ غير مصرح لك.")
        return
    if running_process:
        bot.send_message(message.chat.id, "✅ شغال.")
        return
    bot.send_message(message.chat.id, "✅ بدأ الفحص...")
    running_process = True
    threading.Thread(target=scanner, daemon=True).start()
    threading.Thread(target=send_stats, args=(message.chat.id,), daemon=True).start()

@bot.message_handler(commands=['stop'])
def stop_cmd(message):
    global running_process
    if message.chat.id != OWNER_ID:
        return
    running_process = False
    bot.send_message(message.chat.id, "⛔️ تم إيقاف الفحص.")

bot.polling()
