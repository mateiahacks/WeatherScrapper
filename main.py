from libs.AmindiController import Amindi
from libs.Consoling import Console

def main():

    cityName = Console.getString("Enter city name in Georgian")

    amindi = Amindi(cityName)

    days = Console.getInt("Enter how many weathers of days you want to get")
    
    Console.out("Fetching...")
    weathers = amindi.fetchWeathers(days)
    Console.out("Finished.")

    Console.outWeathers(weathers)

    choice = Console.getInt("(1) visualization, (2) get one day weather (3) next 24 hours hourly weather")

    while choice == 3:
        Console.out("Fetching...")
        hourly = amindi.getHourly()
        Console.outHours(hourly)
        choice = Console.getInt("(1) visualization, (2) get one day weather (3) next 24 hours hourly weather")

    while choice == 2:
        date = Console.getString("Enter date in following format: [number] [month name]")
        Console.out("Checking...")
        res = amindi.getOneDayWeather(date)

        while (len(res) == 0):
            Console.out("Error: This date weather is not known or it is Entered in invalid format!")
            date = Console.getString("Enter date in following format: [number] [month name]")
            Console.out("Checking...")
            res = amindi.getOneDayWeather(date)

        Console.outWeather(res)
        choice = Console.getInt("(1) visualization, (2) get one day weather")

    if choice == 1:
        amindi.visualize()
    

    amindi.closeDriver()

if __name__ == "__main__":
    main()