from selenium import webdriver

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver=webdriver.Chrome(options=options)

    return driver

