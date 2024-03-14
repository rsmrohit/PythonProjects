from flat import Bill, Flatmate
from reports import PdfReport


def handleBill():
    done = False
    while not done:
        print("Type the number to edit bill or type '0' to create new\n")
        for i in bills:
            print(f"{1+bills.index(i)}\tAmount: {i.amount}\t Period: {i.period}")
        bill = 0
        try:
            bill = int(input())-1
        except Exception:
            done = True
            break

        if bill != -1:
            bills.pop(bill)

        bill_amt = int(input("Bill Amount: "))
        bill_period = input("Bill Period: ")
        bills.append(Bill(amount=bill_amt, period=bill_period))

    pass


def handleFlatmates():
    done = False
    while not done:
        print("Type the number to edit Flatmate or type '0' to create new\n")
        for i in flatmates:
            print(
                f"{1+flatmates.index(i)}\tName: {i.name}\t DaysinHouse: {i.days_in_house}")
        flatmate = 0
        try:
            flatmate = int(input())-1
        except Exception:
            done = True
            break

        if flatmate != -1:
            flatmates.pop(flatmate)

        name = input("Name: ")
        days_in_house = int(input("Days in the house: "))
        flatmates.append(Flatmate(name=name, days_in_house=days_in_house))

    pass


def handleGeneration():
    print("Bills below:")
    [print(f"{1+bills.index(i)}\tAmount: {i.amount}\t Period: {i.period}")
     for i in bills]
    bill_num = int(input("Select which bill: \n"))-1

    print("Flatmates below: ")
    [print(f"{1+flatmates.index(i)}\tName: {i.name}\t DaysinHouse: {i.days_in_house}")
     for i in flatmates]

    done = False
    selected = []
    while not done:
        try:
            selected.append(flatmates[int(input())-1])
        except Exception:
            done = True
            break

    pdf = PdfReport("Flatmate Bill")
    pdf.generate(bills[bill_num], *selected)


# the_bill = Bill(amount=120, period="March 2021")
# john = Flatmate(name="John", days_in_house=20)
# mary = Flatmate(name="Mary", days_in_house=25)
# Storage for created bills and flatmates
bills = []
flatmates = []

# Adding user functionality
done = False
while not done:
    action = input(
        "Type 'B' for Bill actions\nType 'F' to view flatmate actions\nType 'G' to generate Report\n")
    if action.upper() == "B":
        handleBill()
    elif action.upper() == "F":
        handleFlatmates()
    elif action.upper() == "G":
        handleGeneration()
    else:
        done = True
