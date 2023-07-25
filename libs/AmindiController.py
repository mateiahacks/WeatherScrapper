from .helpers import getDriver, getWeatherDescription
from selenium.webdriver.common.by import By

class Amindi:
    def __init__(self, city):
        self._driver = getDriver()
        self._weathers = []
        self._url = (f"https://amindi.ge/ka/city/{city}/")

    def getWeathers(self):
        return self._weathers

    def getBrowserDriver(self):
        return self._driver

    def fetchWeathers(self, days):
        if days not in [5, 10, 14]:
            raise Exception("days argument could be only 5, 10 or 14")

        self._driver.get(self._url + f"?d={days}")
        weatherElements = self._driver.find_elements(By.CLASS_NAME, "card")
        
        result = []
    
        for element in weatherElements:
            weekDay = element.find_element(By.CLASS_NAME, "weekDay").text
            day = element.find_element(By.CLASS_NAME, "day").text
            desc = getWeatherDescription(element.find_element(By.TAG_NAME, "img").get_attribute("src"))
            celsiuses = [e.text for e in element.find_elements(By.TAG_NAME, "span")]

            result.append({ 
                "weekDay": weekDay, 
                "day": day,
                "celsiuses": celsiuses,
                "desc": desc,
            })
        self.weathers = result

        return result

    def getOneDayWeather(self, date):
        weathers = self.fetchWeathers(14)

        res = list(filter(lambda x: x["day"] == date, weathers))
        if (len(res) == 0):
            return res
        return res[0]

    def getHourly(self):
        self._driver.get('https://amindi.ge/ka/hourly')

        hours = self._driver.find_elements(By.CLASS_NAME, "card")
        result = []

        for element in hours:
            hour = element.find_element(By.CLASS_NAME, "weekDay").text
            day = element.find_element(By.CLASS_NAME, "day").text
            desc = getWeatherDescription(element.find_element(By.TAG_NAME, "img").get_attribute("src"))
            celsius = element.find_element(By.TAG_NAME, "span").text
            result.append({
                "hour": hour,
                "day": day,
                "desc": desc,
                "celsius": celsius,
            })
        return result
        

    def closeDriver(self):
        self._driver.close()
    

    def visualize(self):
        pass


