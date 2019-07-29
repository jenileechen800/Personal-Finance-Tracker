import tkinter as tk


class Assets:
    def __init__(self):
        self.taxable_accounts = TaxableAccounts()
        self.retirement_accounts = RetirementAccounts()
        self.business_owned_interests = BusinessOwnedInterests()
        self.use_assets = BusinessOwnedInterests()
        self.cash_equivalents = CashEquivalents()
        self.all_assets = [self.taxable_accounts, self.retirement_accounts, self.business_owned_interests,
                           self.use_assets, self.cash_equivalents]

    def total_assets_amt(self):
        total_assets = \
            self.total_use_assets() + \
            self.total_invested_assets() + \
            self.total_cash()

        return total_assets

    def total_use_assets(self):
        total_use_assets = 0

        for amt in self.use_assets.values():
            total_use_assets += amt

        return total_use_assets

    def total_invested_assets(self):
        total_invested_assets = 0

        for amt in self.taxable_accounts.values():
            total_invested_assets += amt

        for amt in self.retirement_accounts.values():
            total_invested_assets += amt

        for amt in self.business_owned_interests.values():
            total_invested_assets += amt

        return total_invested_assets

    def total_cash(self):
        total_cash = 0

        for amt in self.cash_equivalents.values():
            total_cash += amt

        return total_cash


class TaxableAccounts:
    def __init__(self):
        self.list = {"Brokerage": 0,
                     "Other": 0}
        self.name = "Taxable Accounts"
        self.sum = calc_sum(self.list.values())


class RetirementAccounts:
    def __init__(self):
        self.list = {"IRA": 0,
                     "Roth IRA": 0,
                     "401(k) or 403(b)": 0,
                     "SEP-IRA": 0,
                     "Keogh (other qualified plan)": 0,
                     "Pension (vested benefit)": 0,
                     "Annuity (accumulated value)": 0}
        self.name = "Retirement Accounts"
        self.sum = calc_sum(self.list.values())


class BusinessOwnedInterests:
    def __init__(self):
        self.list = {"Real Estate (rental property, land": 0,
                     "Sole Proprietorship": 0,
                     "Partnership": 0,
                     "C Corporation": 0,
                     "S Corporation": 0,
                     "Limited Liability Company": 0,
                     "Other": 0}
        self.name = "Business Owned Interests"
        self.sum = calc_sum(self.list.values())


class CashEquivalents:
    def __init__(self):
        self.list = {"Checking Accounts": 0,
                     "Savings Accounts": 0,
                     "Money Market Accounts": 0,
                     "Savings Bonds": 0,
                     "CD's": 0,
                     "Cash Value of Life Insurance": 0}
        self.name = "Cash Equivalents"
        self.sum = calc_sum(self.list.values())


def calc_sum(dict):
    total_liabilities = 0

    for amt in dict:
        total_liabilities += amt

    return total_liabilities

