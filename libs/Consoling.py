
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

    def out(text):
        print(f"< {text}")
