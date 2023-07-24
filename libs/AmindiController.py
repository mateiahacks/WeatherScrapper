from .helpers import getDriver
from selenium.webdriver.common.by import By

class Amindi:

    def __init__(self, city):
        self.driver = getDriver()
        self.url = (f"https://amindi.ge/ka/city/{city}/")

    def getWeathers(self, days):
        if days not in [5, 10, 14]:
            raise Exception("days argument could be only 5, 10 or 14")

        self.driver.get(self.url + f"?d={days}")
        weatherElements = self.driver.find_elements(By.CLASS_NAME, "card")
        result = []
    
        for element in weatherElements:
            weekDay = element.find_element(By.CLASS_NAME, "weekDay").text
            day = element.find_element(By.CLASS_NAME, "day").text
            celsiuses = [e.text for e in element.find_elements(By.TAG_NAME, "span")]
            result.append({ 
                "weekDay": weekDay, 
                "day": day,
                "celsiuses": celsiuses,
            })

        return result

