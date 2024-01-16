import telebot
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

service_chrome = Service()
options_chrome = Options()
options_chrome.add_argument("--disable-blink-features=AutomationControlled")
options_chrome.add_argument("--no-first-run")
options_chrome.add_argument("--no-service-autorun")
options_chrome.add_argument("--no-default-browser-check")
options_chrome.add_argument("--disable-extensions")
options_chrome.add_argument("--disable-popup-blocking")
options_chrome.add_argument("--profile-directory=Default")
options_chrome.add_argument("--ignore-certificate-errors")
options_chrome.add_argument("--disable-plugins-discovery")
options_chrome.add_argument("--incognito")
options_chrome.add_argument("--window-size=1920,1080")
options_chrome.add_argument("--headless")
options_chrome.add_argument('--disable-gpu')
options_chrome.add_argument('--no-sandbox')
options_chrome.add_argument('--start-maximized')
options_chrome.add_argument('--disable-setuid-sandbox')
options_chrome.add_experimental_option("excludeSwitches", ["enable-automation"])
options_chrome.add_experimental_option('useAutomationExtension', False)
options_chrome.add_argument("--user-agent='Mozilla/5.0 (X11; Linux x8"
                            "6_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'")

TOKEN_BOT = '6891703177:AAGQDyqemvyWQoNHU2YPfOYhIvVbOuX5vSc'
bot = telebot.TeleBot(TOKEN_BOT)
l = "m.shjoreel@gmail.com"
p = "parus12Mishasteam$$"


def wait_element(browser, xpath):
    while len(browser.find_elements(By.XPATH, xpath)) == 0:
        sleep(1)


def get_browser(options=None, service=None):
    return webdriver.Chrome(
        service=service,
        options=options)


def start(count_games, file):
    browser = get_browser(options=options_chrome)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
            delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
      '''
    })
    print("Loading page...")
    browser.get("https://stake.pink/ru")
    sleep(8)
    if len(browser.find_elements(By.XPATH, "//iframe[@sandbox='allow-same-origin allow-scripts allow-popups']")) != 0:
        print("Cloudflare detected")
        iframe = browser.find_element(By.XPATH, "//iframe[@sandbox='allow-same-origin allow-scripts allow-popups']")
        browser.switch_to.frame(iframe)
    print("Success")
    print("Sign in...")
    sleep(4)
    wait_element(browser, "//*[@id='svelte']/div[2]/div[2]/div[2]/div/div/div/section/div/button[1]")
    browser.find_element(By.XPATH, "//*[@id='svelte']/div[2]/div[2]/div[2]/div/div/div/section/div/button[1]").click()
    wait_element(browser, "//*[@id='svelte']/div[1]/div[2]/div/div/div[2]/form/button")
    browser.find_element(By.XPATH, "//*[@id='svelte']/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/button").click()
    sleep(4)
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[1])
    sleep(2)
    browser.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(l)
    sleep(3)
    if len(browser.find_elements(By.XPATH, "//*[@id='identifierNext']/div/button")) != 0:
        browser.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
    else:
        browser.find_element(By.XPATH, "//button[text()='Next']").click()
    sleep(6)
    if len(browser.find_elements(By.XPATH, "//div[@jscontroller='ZUKRxc']")) != 0:
        captcha_block = browser.find_element(By.XPATH, "//div[@jscontroller='ZUKRxc']")
        print(captcha_block.value_of_css_property('display'))
        if captcha_block.value_of_css_property('display') != 'none':
            print("Gooogle auth captcha deteced")
            browser.save_screenshot('captcha.png')
            sleep(10)
            text = str(input("Captcha: "))
            browser.find_element(By.XPATH, "//*[@id='ca']").send_keys(text)
            if len(browser.find_elements(By.XPATH, "//*[@id='identifierNext']/div/button")) != 0:
                browser.find_element(By.XPATH, "//*[@id='identifierNext']/div/button").click()
            else:
                browser.find_element(By.XPATH, "//button[text()='Next']").click()
    sleep(6)
    browser.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(p)
    sleep(2)
    browser.find_element(By.XPATH, "//*[@id='passwordNext']/div/button").click()
    sleep(3)
    window_handles = browser.window_handles
    if len(window_handles) > 1:
        if len(browser.find_elements(By.XPATH, "//span[text()='Двухэтапная аутентификация']")) != 0:
            while len(browser.find_elements(By.XPATH, "//span[text()='Двухэтапная аутентификация']")) != 0:
                print("Load сonfirmation page...")
                sleep(2)
            print("Сonfirmation required")
            sleep(5)
    window_handles = browser.window_handles
    browser.switch_to.window(window_handles[0])
    print("Signed")
    sleep(3)
    print("Loading roulette")
    browser.get("https://stake.pink/ru/casino/games/roulette")
    print("Loaded")
    wait_element(browser, "//div[@class='wheel-house svelte-1p8f5xw']")
    wait_element(browser, "//button[@class='button variant-tab size-sm align-left rounded svelte-1epmied']")
    browser.find_element(By.XPATH, "//button[@class='button variant-tab size-sm align-left rounded svelte-1epmied']").click()
    sleep(1)
    wait_element(browser, "//button[@aria-label='Select usdt']")
    browser.find_element(By.XPATH, "//button[@aria-label='Select usdt']").click()
    browser.find_elements(By.XPATH, "//button[@class='button variant-neutral size-sm align-left no-shadow "
                                    "svelte-1epmied']")[1].click()
    sleep(2)
    browser.find_elements(By.XPATH, "//button[@class='wrap svelte-10l8lsh']")[4].click()
    sleep(1)
    browser.find_element(By.XPATH, "//*[@id='main-content']/div/div[1]/div[2]/div/div/div[3]/button[4]").click()
    print("Parsing")
    for i in range(count_games):
        button = browser.find_element(By.XPATH, "//*[@id='main-content']/div/div[1]/div[1]/button")
        button.click()
        while button.get_attribute('data-test-action-enabled') == 'false':
            sleep(0.2)
        while len(browser.find_element(By.XPATH, "//*[@id='main-content']/div/div[1]/div[2]/div/div/div[1]/div/span").text) == 0:
            sleep(0.2)
        value = browser.find_element(By.XPATH, "//*[@id='main-content']/div/div[1]/div[2]/div/div/div[1]/div/span").text
        print("Current value: ", value)
        message = "<b>Индекс: %s, значение - %s</b>" % (str(i + 1), value)
        bot.send_message(
            588522164,
            message,
            parse_mode='html'
        )
        file.write(value + '\n')


file = open('file.txt', 'w')
start(10, file)
file.close()