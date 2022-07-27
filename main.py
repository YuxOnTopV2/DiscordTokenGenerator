from http import client
import mailbox
import random
import string
import threading
import requests
import os
import ascii2text
import time
import json
from fake_useragent import UserAgent
from PyMailGw import MailGwApi
import time
from python3_anticaptcha import HCaptchaTaskProxyless
from modules import SmsServiceAPI

apikey = "ANTI-CAPTCHA API KEY"
ua = UserAgent()
proxies = []

def loadproxies():
    r = requests.get("https://api.proxyscrape.com?request=getproxies&proxytype=http")
    rformat = r.text.strip()
    rformat = rformat.replace("\r","")
    rlist = list(rformat.split("\n"))
    with open("proxies.txt", "w") as x:
        for proxy in rlist:
            proxies.append(proxy)

def rn(l):
    return ''.join(random.choice(string.ascii_letters) for i in range(l))



def create(username):
    api = MailGwApi(timeout=5)
    session = requests.session()


    print('     [~] solving captcha...')

   
    getcookie = session.get("https://discord.com/register").headers['set-cookie']
    session.get("https://discord.com/")
    sep = getcookie.split(";")
    sx = sep[0]
    sx2 = sx.split("=")
    dfc = sx2[1]
    split = sep[6]
    split2 = split.split(",")
    split3 = split2[1]
    split4 = split3.split("=")
    sdc = split4[1]

    header2 = {
            "Host": "discord.com",
            "Connection": "keep-alive",
            "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
            "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
            "X-Context-Properties": "eyJsb2NhdGlvbiI6IlJlZ2lzdGVyIn0=",
            "Accept-Language": "en-US",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": ua['google chrome'],
            "Authorization": "undefined",
            "Accept": "*/*",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://discord.com/register",
            "Accept-Encoding": "gzip, deflate, br"
        }

    fingerprintres = session.get("https://discord.com/api/v9/experiments", timeout=10, headers=header2)

    fingerprint = fingerprintres.json()['fingerprint']

    headers = {
            "accept" : "*/*",
            "accept-encoding" : "gzip, deflate, br",
            "accept-language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "content-length":"4797",
            "content-type":"application-json",
            "cookie":f"__dcfduid={dfc}; __sdcfduid={sdc}; _gcl_au=1.1.33345081.1647643031; _ga=GA1.2.291092015.1647643031; _gid=GA1.2.222777380.1647643031; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+18+2022+18%3A53%3A43+GMT-0400+(%E5%8C%97%E7%BE%8E%E4%B8%9C%E9%83%A8%E5%A4%8F%E4%BB%A4%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __cf_bm=.fksdoBlzBs1zuhiY0rYFqFhDkstwwQJultZ756_yrw-1647645226-0-AaluVZQHZhOL5X4GXWxqEIC5Rp3/gkhKORy7WXjZpp5N/a4ovPxRX6KUxD/zpjZ/YFHBokF82hLwBtxtwetYhp/TSrGowLS7sC4nnLNy2WWMpZSA7Fv1tMISsR6qBZdPvg==; locale=en-US",
            "origin":"https://discord.com",
            "referer":"https://discord.com/register",
            "sec-ch-ua" : "Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99",
            "sec-ch-ua-mobile":"?0",
            "sec-ch-ua-platform":"macOS",
            "sec-fetch-dest":"empty",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            "x-discord-locale": "en-US",
            "x-fingerprint": fingerprint,
            "x-super-properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJ6aC1DTiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85OS4wLjQ4NDQuNzQgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijk5LjAuNDg0NC43NCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjExOTc2MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        }

    mail_adr = api.get_mail()

    if mail_adr == None:
        return

    result = HCaptchaTaskProxyless.HCaptchaTaskProxyless(anticaptcha_key=apikey).captcha_handler(websiteURL="https://discord.com/", websiteKey="4c672d35-0701-42b2-88c3-78380b0db560")

    #    payload = {
    #            "username": username,
    #           "email": mail_adr,
    #            "date_of_birth":"1978-06-09",
    #            "password": 'YuxOnTop123@!',
    #            "fingerprint": fingerprint,
    #            "gift_code_sku_id":"null",
    #            "invite": "wUrBTbBd",
    #            "consent": "true",
    #            "captcha_key": result['solution']['gRecaptchaResponse']
    #    }

    register_payload = {
        "captcha_key": result['solution']['gRecaptchaResponse'],
        "invite": "",
        "consent": True,
        "fingerprint": fingerprint,
        "password": 'YuxOnTop123@!',
        "date_of_birth":"1978-06-09",
        "username": username,
        "email": mail_adr
    }
    print(f'     [+] Creating token ({mail_adr})')

    session.headers['cookie'] = f'__dcfduid={session.cookies.get("__dcfduid")}; __sdcfduid={session.cookies.get("__sdcfduid")}; locale=zh-CN' # ; locale=fr
    session.headers['content-length'] = str(len(json.dumps(register_payload)))
    session.headers['content-type'] = 'application/json'
    session.headers['x-fingerprint'] = fingerprint # gen worked without

    r = session.post("https://discord.com/api/v9/auth/register", headers=headers, json=register_payload, timeout=15, cookies=session.cookies)

    if 'ratelimited' in r.text:
        print('Ratelimited')
        return
    else:
        pass

    token = r.json()['token']

    if token == None:
        return


    session.headers['cookie'] = f'__dcfduid={session.cookies.get("__dcfduid")}; __sdcfduid={session.cookies.get("__sdcfduid")}; locale=zh-CN'
    session.headers['authorization'] = token
    session.headers['x-debug-options'] = 'bugReporterEnabled'
    session.headers['x-discord-locale'] = 'zh-CN'
    session.headers['x-super-properties'] = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InpoLUNOIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjIiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwMDg5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='

    session.headers.pop('content-length')
    session.headers.pop('x-track')

    print(f'     [+] Created token ({token})')

    result = HCaptchaTaskProxyless.HCaptchaTaskProxyless(anticaptcha_key=apikey).captcha_handler(websiteURL='https://discord.com/api/v9/auth/verify', websiteKey="f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34")

    print('     [+] Solved Verify Captcha')

    print('     [+] Waiting for verification link !')


    try:
        verify = session.post('https://discord.com/api/v9/auth/verify', headers={
                    "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98',
                    'referer': 'https://discord.com/verify',
                    'authorization': token
                }, json={
                    'captcha_key': result['solution']['gRecaptchaResponse'],
                    'token': link
                }).text
    except:
        time.sleep(10)
        for m in api.fetch_inbox():
            if m['from']['address'] == "noreply@discord.com":
                link = api.get_message_content(m['id'])
                link = requests.get(str(str(link).split(': ')[1])).url
                link = str(link).split('verify#token=')[1]
                verify = session.post('https://discord.com/api/v9/auth/verify', headers={
                    "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98',
                    'referer': 'https://discord.com/verify',
                    'authorization': token
                }, json={
                    'captcha_key': result['solution']['gRecaptchaResponse'],
                    'token': link
                }).text

    
    print(f'     [+] Verified ({token})')

    check = session.get('https://discord.com/api/v6/auth/login', headers={"Authorization": r.json()['token']})
    
    response = session.post(f'https://discord.com/api/v6/invite/{random.randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        token_status = 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        token_status = 'Phone Lock'
    else:
        token_status = 'Valid'

    try:
        if 'token' in r.json():
            if check.status_code == 200:
                print("     [+] "+token+f' ({token_status})')
            else:
                print("     [-] "+token+f' ({token_status})')
        else:
            print("     [X] Ratelimited")
    except Exception as e:
        print(e)

def launch():
    while True:
        try:
            create(f'github.com/yuxontop')
        except:
            pass

def main():
    loadproxies()
    os.system('cls')
    for i in range(1):
        threading.Thread(target=launch).start()

main()
