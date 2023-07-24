from libs.AmindiController import Amindi
from libs.Consoling import Console

def main():

    cityName = Console.getString("Enter city name in Georgian")

    amindi = Amindi(cityName)

    Console.out("Enter how many weathers of days you want to get")
    days = int(input("> "))
    
    Console.out("< Fetching...")
    weathers = amindi.getWeathers(days)
    Console.out("< Finished.")

    choice = Console.getInt("< (1) visualization, (2) get one day weather")




if __name__ == "__main__":
    main()