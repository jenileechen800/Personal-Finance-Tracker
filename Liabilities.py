import tkinter as tk

class Liabilities:
    def __init__(self):
        self.current = CurrentLiabilities()
        self.long_term = LongtermLiabilities()
        self.all_liabilities = [self.current, self.long_term]

    def total_liabilities_amt(self):
        return self.current.sum + self.long_term.sum


class CurrentLiabilities:
    def __init__(self):
        self.list = {"Credit Card Balances": 0,
                        "Estimated Income Tax Owed": 0,
                        "Other Outstanding Bills": 0}
        self.name = "Current Liabilities"
        self.sum = calc_sum(self.list.values())


class LongtermLiabilities:
    def __init__(self):
        self.list = {"Home Mortgage": 0,
                          "Home Equity Loan": 0,
                          "Mortgages on Rental Properties": 0,
                          "Car Loans": 0,
                          "Student Loans": 0,
                          "Life Insurance Policy Loans": 0,
                          "Other Long-Term Debt": 0}
        self.name = "Longterm Liabilities"
        self.sum = calc_sum(self.list.values())


def calc_sum(dict):
    total_liabilities = 0

    for amt in dict:
        total_liabilities += amt

    return total_liabilities

















