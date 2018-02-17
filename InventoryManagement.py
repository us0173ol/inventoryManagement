import sqlite3

from tkinter import *
from datetime import datetime, date

databaseFilename = "inventoryManagement.db"
dailyBeerCount = 0
dailyLiquorCount = 0
dailyWineCount = 0
dailyNACount = 0
dailyAppCount = 0
dailySoupSaladCount = 0
dailySandwichCount = 0
dailyEntreeCount = 0

class MainGUI(Frame):



    def  __init__(self):

        self.root = Tk()

        self.topFrame = Frame(self.root)
        self.topFrame.pack()
        self.middleFrame = Frame(self.root)
        self.middleFrame.pack(side=BOTTOM)
        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack(side=RIGHT)

        Frame.__init__(self)
        self.master.title("Inventory Management")

        self.master.minsize(600,200)
        self.pack(side=LEFT)

        self.beerButton = Button(self.topFrame, text="Beer", width=12, command=self.beer)
        self.beerButton.pack(side=LEFT)

        self.liquorButton = Button(self.topFrame, text="Liquor", width=12, command=self.liquor)
        self.liquorButton.pack(side=LEFT)

        self.wineButton = Button(self.topFrame, text="Wine", width=12, command=self.wine)
        self.wineButton.pack(side=LEFT)

        self.NAButton = Button(self.topFrame, text="N/A", width=12, command=self.NA)
        self.NAButton.pack(side=LEFT)

        self.appetizersButton = Button(self.topFrame, text="Appetizers", width=12, command=self.appetizers)
        self.appetizersButton.pack(side=LEFT)

        self.soupSaladButton = Button(self.topFrame, text="Soups/Salads", width=12, command=self.soupSalad)
        self.soupSaladButton.pack(side=LEFT)

        self.sandwichesButton = Button(self.topFrame, text="Sandwiches", width=12, command=self.sandwiches)
        self.sandwichesButton.pack(side=LEFT)

        self.EntreesButton = Button(self.topFrame, text="Entrees", width=12, command=self.entrees)
        self.EntreesButton.pack(side=LEFT)

        self.ExitButton = Button(self.bottomFrame, text="Exit", width=12, command=self.exit)
        self.ExitButton.pack(side=BOTTOM)

        self.SendButton = Button(self.bottomFrame, text="Send", width=12, command=self.send)
        self.SendButton.pack(side=BOTTOM)

        self.beerVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.beerVar)
        self.resultLabel.pack(side=TOP)

        self.liquorVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.liquorVar)
        self.resultLabel.pack(side=TOP)

        self.wineVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.wineVar)
        self.resultLabel.pack(side=TOP)

        self.NAVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.NAVar)
        self.resultLabel.pack(side=TOP)

        self.appVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.appVar)
        self.resultLabel.pack(side=TOP)

        self.soupSaladVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.soupSaladVar)
        self.resultLabel.pack(side=TOP)

        self.sandwichVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.sandwichVar)
        self.resultLabel.pack(side=TOP)

        self.entreeVar = StringVar()
        self.resultLabel = Label(self.middleFrame, text=" \n ", textvariable=self.entreeVar)
        self.resultLabel.pack(side=TOP)

        self.tableVar = StringVar()
        self.resultLabel = Label(self.bottomFrame, text="\n", textvariable=self.tableVar)
        self.resultLabel.pack(side=BOTTOM)


    def beer(self):
        global dailyBeerCount
        dailyBeerCount += 1
        value = ("Beer: " + str(dailyBeerCount))
        self.beerVar.set(value)


    def liquor(self):
        global dailyLiquorCount
        dailyLiquorCount += 1
        value = ("Liquor: " + str(dailyLiquorCount))
        self.liquorVar.set(value)

    def wine(self):
        global dailyWineCount
        dailyWineCount += 1
        value = ("Wine: " + str(dailyWineCount))
        self.wineVar.set(value)

    def NA(self):
        global dailyNACount
        dailyNACount += 1
        value = ("N/A: " + str(dailyNACount))
        self.NAVar.set(value)

    def appetizers(self):
        global dailyAppCount
        dailyAppCount += 1
        value = ("Appetizers: " + str(dailyAppCount))
        self.appVar.set(value)

    def soupSalad(self):
        global dailySoupSaladCount
        dailySoupSaladCount += 1
        value = ("Soups/Salads: " + str(dailySoupSaladCount))
        self.soupSaladVar.set(value)

    def sandwiches(self):
        global dailySandwichCount
        dailySandwichCount += 1
        value = ("Sandwiches: " + str(dailySandwichCount))
        self.sandwichVar.set(value)

    def entrees(self):
        global dailyEntreeCount
        dailyEntreeCount += 1
        value = ("Entrees " + str(dailyEntreeCount))
        self.entreeVar.set(value)

    def exit(self):
        db = sqlite3.connect(databaseFilename)
        cursor = db.cursor()
        # cursor.execute('DROP TABLE DAILY')
        db.commit()
        db.close()

        exit(0)
    def send(self):
        global dailyBeerCount
        global dailyLiquorCount
        global dailyWineCount
        global dailyNACount
        global dailyAppCount
        global dailySoupSaladCount
        global dailySandwichCount
        global dailyEntreeCount
        print("before")
        manipulate_beer()
        manipulate_liquor()
        manipulate_wine()
        manipulate_NA()
        manipulate_apps()
        manipulate_soupSalad()
        manipulate_sandwiches()
        manipulate_entrees()
        showTable()
        dailyBeerCount = 0
        dailyLiquorCount = 0
        dailyWineCount = 0
        dailyNACount = 0
        dailyAppCount = 0
        dailySoupSaladCount = 0
        dailySandwichCount = 0
        dailyEntreeCount = 0
        print("After")

def showTable():
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM DAILY')
    print("During")
    for row in cursor:
        print(row)

def startGUI():

    MainGUI().mainloop()

def main():
    setupDatabase()
    startGUI()

def setupDatabase():

    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    TodaysDate = date.today()
    # TodaysDate = '2018-02-18'
    # cursor.execute('DROP TABLE DAILY')

    cursor.execute('CREATE TABLE IF NOT EXISTS DAILY(Id primary key, Beer int, Liquor int, Wine int, NA int, Appetizers int, SoupSalad int, Sandwiches int, Entrees int )')
    currentDate = cursor.execute('SELECT Id from DAILY')
    print(currentDate)
    cursor.execute('UPDATE DAILY SET Id = ?', (TodaysDate,))
    # cursor.execute('INSERT OR REPLACE INTO DAILY VALUES(?,0,0,0,0,0,0,0,0)',(TodaysDate,))
    db.commit()

def manipulate_beer():
    TodaysDate = date.today()
    global dailyBeerCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Beer = Beer + ? WHERE Id = ?', (dailyBeerCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_liquor():
    TodaysDate = date.today()
    global dailyLiquorCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Liquor = Liquor + ? WHERE Id = ?', (dailyLiquorCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_wine():
    TodaysDate = date.today()
    global dailyWineCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Wine = Wine + ? WHERE Id = ?', (dailyWineCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_NA():
    TodaysDate = date.today()
    global dailyNACount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET NA = NA + ? WHERE Id = ?', (dailyNACount, TodaysDate))
    db.commit()
    db.close()

def manipulate_apps():
    TodaysDate = date.today()
    global dailyAppCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Appetizers = Appetizers + ? WHERE Id = ?', (dailyAppCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_soupSalad():
    TodaysDate = date.today()
    global dailySoupSaladCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET SoupSalad = SoupSalad + ? WHERE Id = ?', (dailySoupSaladCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_sandwiches():
    TodaysDate = date.today()
    global dailySandwichCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Sandwiches = Sandwiches + ? WHERE Id = ?', (dailySandwichCount, TodaysDate))
    db.commit()
    db.close()

def manipulate_entrees():
    TodaysDate = date.today()
    global dailyEntreeCount
    db = sqlite3.connect(databaseFilename)
    cursor = db.cursor()
    cursor.execute('UPDATE DAILY SET Entrees = Entrees + ? WHERE Id = ?', (dailyEntreeCount, TodaysDate))
    db.commit()
    db.close()

if __name__ == '__main__':
        main()
