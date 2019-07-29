import tkinter as tk
from Data.Net_Worth import Net_Worth
import tktable


class GUI:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Net Worth Worksheet")
        self.var = None
        self.row_count = 0
        self.tb = None

        self.net_worth = Net_Worth()
        self.assets = self.net_worth.assets
        self.liabilities = self.net_worth.liabilities

        self.tb = tktable.Table(self.win,
                                width=50,
                                rows=80,
                                cols=2,
                                colwidth=40)
        self.var = tktable.ArrayVar(self.win)

        self.text_intro()
        self.update_gui()
        self.show_assets()
        tk.mainloop()

    def show_assets(self):
        self.fill_finance_data()

        self.tb['variable'] = self.var
        self.tb.pack()
        self.tb.tag_configure('beige', background="#FDEBD0")
        self.tb.tag_configure('brown', background="#93631B")

    def fill_finance_data(self):
        self.fill_finance_header_main("Personal Net Worth Worksheet")

        self.fill_finance_header_main("Liabilities")
        for liability_type in self.liabilities.all_liabilities:
            self.fill_finance_header(liability_type.name)
            self.fill_finance_category(liability_type.list)

        self.fill_finance_header_main("Assets")
        for asset_type in self.assets.all_assets:
            self.fill_finance_header(asset_type.name)
            self.fill_finance_category(asset_type.list)

    def fill_finance_category(self, net_worth_category):
        for name, amt in net_worth_category.items():
            index = "%i,%i" % (self.row_count, 0)
            self.var[index] = name

            index = "%i,%i" % (self.row_count, 1)
            self.var[index] = amt

            self.row_count += 1

    def fill_finance_sum(self, sum_type, sum):
        index = "%i,%i" % (self.row_count, 1)
        self.tb.tag_cell('brown', index)
        self.var[index] = "Total " + sum_type

        index = "%i,%i" % (self.row_count, 1)
        self.tb.tag_cell('brown', index)
        self.var[index] = sum

        self.row_count += 1

    def fill_finance_header(self, header):
        index = "%i,%i" % (self.row_count, 0)
        self.var[index] = header
        self.tb.tag_cell('beige', index)

        self.row_count += 1

    def fill_finance_header_main(self, header):
        index = "%i,%i" % (self.row_count, 0)
        self.var[index] = header
        self.tb.tag_cell('brown', index)

        self.row_count += 1

    def text_intro(self):
        intro_header = tk.Label(self.win, text="Welcome to \"My Net Worth Worksheet\":", font=(None, 20))
        intro_body = tk.Label(self.win, text = "Here you can keep updated on your finances "
                                               "by caulculating your net worth.\n")
        intro_header.pack()
        intro_body.pack()

    def update_gui(self):
        update_button = tk.Button(self.win, text="Update", command=self.update_backend())
        update_button.pack()

    def update_backend(self):
        label = tk.Label(self.win, text="hi")
        label.pack()

        for curr_row in range(self.row_count): #iterate through every row and update table
            index = "%i,%i" % (curr_row, 0)
            if self.var.get(index) == "Current Liabilities":
                curr_row = self.update(self.liabilities.current, curr_row)
            elif self.var.get(index) == "Longterm Liabilities":
                curr_row = self.update(self.liabilities.long_term)
        self.show_assets()

    def update(self, liabilties_type, curr_row):
        for liability in liabilties_type:
            index = "%i,%i" % (curr_row, 0)
            liabilties_type[liability] = self.var.get(index)

            curr_row += 1

        return curr_row




gui = GUI()










