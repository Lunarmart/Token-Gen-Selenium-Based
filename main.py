import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Style, init
from fake_useragent import UserAgent
from pystyle import *
import requests
import time
import random
import string
import re
import os
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import tls_client

WEBHOOK_URL = "https://discord.com/api/webhooks/1322082195585765396/ykC3kVJVr7QIkipGf6dY23ch0JiecJcKeX3O5JW4M8TRYmRR5MDtyz8LwtHBlKhPfhfW"
banner = f'''
        _ _   _                 _       
       | | | (_)               | |      
  _   _| | |_ _ _ __ ___   __ _| |_ ___ 
 | | | | | __| | '_ ` _ \ / _` | __/ _ \
 | |_| | | |_| | | | | | | (_| | ||  __/
  \__,_|_|\__|_|_| |_| |_|\__,_|\__\___|
                                                                               
                                        🚀 Ultimate EVS Tool 🚀'''




def account_ratelimit():
    """Fetches rate limit using account creation data."""
    try:
        m = format(''.join(random.choice(string.digits) for _ in range(6)))
        email = format(''.join(random.choice(string.ascii_lowercase) for _ in range(9)))+m
        mail = "{}@gmail.com".format(''.join(random.choice(string.ascii_lowercase) for _ in range(11)))
        nam = "ultimate"
        client = tls_client.Session(client_identifier='chrome_110')
        client.headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.5",
                "Content-Type": "application/json",
                "DNT": "1",
                "Host": "discord.com",
                "Origin": "https://discord.com",
                "Referer": 'https://discord.com/register',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
                "X-Debug-Options": "bugReporterEnabled",
                "X-Discord-Locale": "en-US",
                "X-Discord-Timezone": "Asia/Calcutta",
                "X-Super-Properties": 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIEZyYW1lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImdyLUFSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgOC4wOyBXaW5kb3dzIE5UIDYuMTsgVHJpZGVudC80LjA7IEdUQjcuNDsgY2hyb21lZnJhbWUvMjQuMC4xMzEyLjU3OyBTTENDMjsgLk5FVCBDTFIgMi4wLjUwNzI3OyAuTkVUIENMUiAzLjUuMzA3Mjk7IC5ORVQgQ0xSIDMuMC4zMDcyOTsgLk5FVDQuMEM7IEluZm9QYXRoLjM7IE1TLVJUQyBMTSA4OyBCUkkvMikiLCJicm93c2VyX3ZlcnNpb24iOiIyNC4wLjEzMTIiLCJvc192ZXJzaW9uIjoiNyIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cueW91dHViZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy55b3V0dWJlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJhc2suY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0ODQ3OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
            }
        data = {
                'email': mail,
                'password': 'ultimate12$$',
                'date_of_birth': "2000-09-20",
                'username': email,
                'consent': True,
                'captcha_service': 'hcaptcha',
                'global_name': nam,
                'captcha_key': None,
                'invite': None,
                'promotional_email_opt_in': False,
                'gift_code_sku_id': None
            }
        req = client.post(f'https://discord.com/api/v9/auth/register', json=data)
        if 'The resource is being rate limited' in req.text:
                limit = req.json()['retry_after']
                return limit
        else:
                return 1
    except Exception as e:
        print(f'{Fore.RED} Error fetching rate limit: {str(e)}')
# List of proxies
# proxies = ([
#     "ln1qelya1yfw3fo-country-uz:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-ch:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-sa:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-ma:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-my:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-pk:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-no:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-tr:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-lk:161wvzyv7qk4xrj@rp.proxyscrape.com:6060",
#     "ln1qelya1yfw3fo-country-br:161wvzyv7qk4xrj@rp.proxyscrape.com:6060"
# ])

# def setup_proxy():
#     """Randomly select a proxy to use."""
#     proxy = random.choice(proxies)
#     proxy_settings = Proxy()
#     proxy_settings.proxy_type = ProxyType.MANUAL
#     proxy_settings.http_proxy = proxy
#     proxy_settings.ssl_proxy = proxy
#     return proxy_settings

init(autoreset=True)
os.system("cls")
os.system("title Ultimate EV GEN V1 Discord-lunarmart/termwave_")
def random_sleep(base=2, variation=3):
    time.sleep(base + random.uniform(0, variation))

def set_random_user_agent(options):
    """Set a random user agent."""
    ua = UserAgent()
    random_user_agent = ua.random
    options.add_argument(f"user-agent={random_user_agent}")
    print(f"{timestamp()} {Fore.BLUE}Using User-Agent: {random_user_agent}{Style.RESET_ALL}")

def timestamp():
    return f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S %d-%m-%Y')}]"

def print_templog(temp_email):
    print(f"{timestamp()} {Fore.BLUE}Using tempmail{Style.RESET_ALL}: {Fore.GREEN}{temp_email}{Style.RESET_ALL}")

def generate_yopmail_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    email = f"{username}@1xp.fr"
    return username, email

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def load_cf_clearance():
    try:
        with open('url.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def send_webhook(email, password, token):
    embed = {
        "embeds": [{
            "title": "Token Information",
            "description": f"```{email}:{password}:{token}```",
            "color": 800080  # Red color, can be changed
        }]
    }
    response = requests.post(WEBHOOK_URL, json=embed)
    if response.status_code == 204:
        print(f"{timestamp()} {Fore.GREEN}✅ Token sent successfully via webhook.{Style.RESET_ALL}")
    else:
        print(f"{timestamp()} {Fore.RED}❌ Failed to send token via webhook. Response: {response.text}{Style.RESET_ALL}")

def login_and_fetch_token(email, password):
    data = {"email": email, "password": password, "undelete": "false"}
    headers = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    }
    r = requests.post("https://discord.com/api/v9/auth/login", json=data, headers=headers)
    if r.status_code == 200:
        token = r.json().get("token")
        if token:
            print(f"{timestamp()} {Fore.GREEN}Token fetched: {token}{Style.RESET_ALL}")
            send_webhook(email, password, token)
            with open("tokens.txt", "a") as f:
                f.write(f"{token}\n")
            with open("evs.txt", "a") as f:
                f.write(f"{email}:{password}:{token}\n")
            return True
    elif "captcha-required" in r.text:
        print(f"{timestamp()} {Fore.RED}Discord returned captcha, stopping retry.{Style.RESET_ALL}")
        return False
    return False

def main():
    print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
    while True:
        # proxy = setup_proxy()
        username, email = generate_yopmail_email()
        print(f"{timestamp()} {Fore.BLUE}Using temporary email: {email}{Style.RESET_ALL}")
        if not email:
            print(f"{timestamp()} {Fore.RED}Failed to create temporary email.{Style.RESET_ALL}")
            continue
        print_templog(email)
        driver = None
        try:
            options = uc.ChromeOptions()
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--ignore-certificate-errors")
            driver = uc.Chrome(options=options)
            driver.maximize_window()
            # proxy_address = proxy.http_proxy
            # options.add_argument(f'--proxy-server=http://{proxy_address}')
            # print(f"{timestamp()} {Fore.YELLOW}[INFO] Using proxy:{Fore.GREEN} {proxy_address}")
            cf_clearance = load_cf_clearance()
            driver.get("https://discord.com/register")
            if cf_clearance:
                try:
                    driver.delete_cookie("cf_clearance")
                except Exception:
                    pass
                driver.add_cookie({"name": "cf_clearance", "value": cf_clearance, "domain": "discord.com"})
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
            driver.find_element(By.NAME, "email").send_keys(email)
            driver.find_element(By.NAME, "global_name").send_keys("Lunarmart")
            username = generate_random_string()
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(email)
            element_3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input')))
            element_3.send_keys('15')
            element_3.send_keys(Keys.RETURN)
            element_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-3-input')))
            element_2.send_keys('MAY')
            element_2.send_keys(Keys.RETURN)
            element_4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-4-input')))
            element_4.send_keys('1995')
            continue_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            limit = account_ratelimit()
            if limit > 1:
                print(f'{timestamp()}{Fore.RED}[INFO] Ratelimited for {limit} seconds. Retrying after ratelimit disappears.')
                time.sleep(limit)
            continue_button.click()
            while True:
                WebDriverWait(driver, 300).until(EC.url_contains("discord.com/channels/@me"))
                print(f"{timestamp()} {Fore.GREEN}Redirected to the Discord page!{Style.RESET_ALL}")
                usernamebaba = email.split('@')[0]
                driver.get(f"https://yopmail.com/en/?login={usernamebaba}")
                print(f"{timestamp()} {Fore.BLUE}Navigate to Yopmail and verify email manually.{Style.RESET_ALL}")
                print(f"{timestamp()} {Fore.BLUE}Once you've solved the CAPTCHA and clicked the verification link, Close the Browser to continue.{Style.RESET_ALL}")
                while True:
                    try:
                        driver.title  
                    except Exception:
                        print(f"{timestamp()} {Fore.GREEN}Browser closed by the user. Proceeding...{Style.RESET_ALL}")
                        break
                success = login_and_fetch_token(email, email)
                if success:
                    print(f"{timestamp()} {Fore.GREEN}Process complete. Restarting...{Style.RESET_ALL}")
                else:
                    print(f"{timestamp()} {Fore.RED}Failed to fetch the token.{Style.RESET_ALL}")
                break

        finally:
            if driver:
                try:
                    driver.quit()
                    print(f"{timestamp()} {Fore.GREEN}Driver closed successfully.{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{timestamp()} {Fore.YELLOW}Driver already closed or error occurred: {e}{Style.RESET_ALL}")
                finally:
                    driver = None 

if __name__ == "__main__":
    main()