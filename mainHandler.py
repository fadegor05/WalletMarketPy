from marketsAPI import getItem, getItemList
import statistics

class MainHandler:
    def __init__(self, amount : int, delta : float, currency : str) -> None:
        self.amount = amount
        self.delta = delta
        self.currency = currency
        self.amounts = {'min': self.amount * (1 - self.delta), 'max': self.amount * (1 + self.delta)}

        self.itemList = getItemList(currency=self.currency)
        self.fittableItemList = self.getFittablePrice(self.itemList)
        self.maxVolumeItemList = self.getMaxVolume(self.fittableItemList)
        self.handledItemList = self.getHandledItemList(self.maxVolumeItemList)
        self.printOutItemList(self.handledItemList)

    def getFittablePrice(self, itemList : list) -> list:
        items = list()
        for item in itemList:
            if self.amounts['min'] < float(item['price']) < self.amounts['max']:
                items.append(item)
        return items
    
    def getMaxVolume(self, itemList : list) -> list:
        items = dict()
        for item in itemList:
            volume = int(item['volume'])
            if volume in items:
                items[volume].append(item)
            else:
                items[volume] = [item]
        return items[max(items)]
    
    def getSteamItemPrice(self, itemName : str) -> float:
        steamItem = getItem(itemName, self.currency)
        steamPrice = statistics.mean([float(steamItem["median_price"]),
                                      float(steamItem["lowest_price"]),
                                      float(steamItem["average_price"])]) * 0.87
        
        return steamPrice

    def getHandledItemList(self, itemList : list) -> list:
        items = list()
        for item in itemList:
            steamPrice = self.getSteamItemPrice(item['market_hash_name'])
            itemOut = {
                'name': item['market_hash_name'],
                'marketPrice': item['price'],
                'steamPrice': round(steamPrice, 2),
                'profit': round(steamPrice - float(item['price']), 2)
             }
            items.append(itemOut)
        return items
    
    def printOutItemList(self, itemList : list) -> None:
        for n, item in enumerate(itemList):
            print(f'  {n+1}.', item['name'])
            print(f'  • CS:GO Market Price: ', item['marketPrice'], self.currency)
            print(f'  • Steam Price (SELL): ~', item['steamPrice'], self.currency)
            print(f'  • Profit: ~', item['profit'], self.currency)
