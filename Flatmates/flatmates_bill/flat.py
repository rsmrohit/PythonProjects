class Bill:
    """
    Object that contains data about a bill, such as total amount and period of bill
    """

    def __init__(self, amount, period) -> None:
        self.amount = int(amount)
        self.period = period


class Flatmate:
    """
    Person living in the flat, paying a share of the bill
    """

    def __init__(self, name, days_in_house) -> None:
        self.name = name
        self.days_in_house = int(days_in_house)

    def pays(self, bill, flatmates):
        return round(bill.amount*self.percent_of_pay(flatmates)*100)/100

    def percent_of_pay(self, flatmates):
        return self.days_in_house / sum(y.days_in_house for y in flatmates)
