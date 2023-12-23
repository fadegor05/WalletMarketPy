from configParser import ConfigParser
from mainHandler import MainHandler

class App:
    def __init__(self) -> None:
        self.configParser = ConfigParser()
        self.mainHandler = None

        self.main()


    def main(self) -> None:
        print(self.configParser.getASCII(), self.configParser.getCredits())
        self.mainHandler = MainHandler(self.getAmount(), 
                                       self.configParser.getDelta(),
                                       self.configParser.getCurrency())

    def getAmount(self) -> int:
        while True:
            try: 
                return int(input(f'  Amount ({self.configParser.getCurrency()}) > '))
            except ValueError:
                print("  Try again...")
            finally:
                print('')
        