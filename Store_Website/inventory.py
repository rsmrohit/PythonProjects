import sqlite3
import random

def create_dummy():
    connection = sqlite3.connect("inventory.db")
    connection.executemany("INSERT INTO Goods VALUES(?, ?, ?, ?)", getData())
    connection.commit()
    connection.close()

def getData():
    returnMe = []
    i = 0
    while (i<50):
        returnMe.append(("tomatoes", random.randint(0, 20), random.randint(0, 20)+(random.randint(0, 20)/100), "March 23, 2023"))
        i+=1
    return returnMe

if __name__ == "__main__":
    # create_dummy()
    pass