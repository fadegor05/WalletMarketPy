import json
import os

CONFIG_FILE = 'config.json'
CONFIG_TEMPLATE = {'currency': 'RUB', 'delta': 0.05, 'selection': 5}
ASCII_FILE = 'ascii'
CREDITS = '\n\n  Commit #4 | Version 1.1 | Made by fadegor05\n'

class ConfigParser:
    def __init__(self) -> None:
        self.jsonInit()

        self.parsedData = self.parseData()
        self.parsedASCII = ''.join(self.parseASCII())
    
    def jsonInit(self) -> None:
        if not os.path.isfile(CONFIG_FILE):
            with open(CONFIG_FILE, 'w') as file:
                file.write(json.dumps(CONFIG_TEMPLATE))
        
    def parseASCII(self) -> str:
        with open(ASCII_FILE, 'r') as file:
            return file.readlines()

    def parseData(self) -> dict:
        data = {}
        with open(CONFIG_FILE, 'r') as file:
            data = json.load(file)
        return data

    def getASCII(self) -> str:
        return self.parsedASCII
    
    def getCredits(self) -> str:
        return CREDITS

    def getCurrency(self) -> str:
        return self.parsedData['currency']

    def getDelta(self) -> float:
        return self.parsedData['delta']
    
    def getSelection(self) -> int:
        return self.parsedData['selection']