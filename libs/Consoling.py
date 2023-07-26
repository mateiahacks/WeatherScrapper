class Console:

    def __init__(self):
        self._log = []
    
    @staticmethod
    def getString(text):
        print(text)
        return input("> ")
    
    @staticmethod
    def getInt(text):
        print(text)
        return int(input("< "))

    @staticmethod
    def out(text):
        print(f"< {text}")

    @staticmethod
    def outWeather(obj):
        min = obj["celsiuses"][0]
        max = obj["celsiuses"][1]
        print(f"min: {min}")
        print(f"max: {max}")
        print(obj["desc"])

    @staticmethod
    def outHours(arr):
        for item in arr:
            hour = item["hour"].split(' ')[0]
            celsius = item["celsius"]
            print(f"{hour} hour: {celsius} celsius")
        
    @staticmethod
    def outWeathers(arr):
        for item in arr:
            weekday = item["weekDay"]
            day = item["day"]
            min, max = item["celsiuses"][0], item["celsiuses"][1]
            print(f"{day} {weekday}")
            print(f"min: {min} - max: {max}")
            print("\n")