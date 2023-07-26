from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .constants import ICONS

def getDriver():
    options = Options()
    options.headless = True
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=options)

    return driver

def getWeatherDescription(url):
    first = url.split('.')

    first = first[len(first)-2]

    num = int(first[-2:])

    for key in ICONS:
        if num in ICONS[key]:
            return key

    return ''


