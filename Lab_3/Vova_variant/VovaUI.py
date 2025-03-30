import tkinter as tk

from tkinter import ttk

import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from VovaLogic import DatabaseWork, SlicePrognoses


class StatisticWindow(tk.Tk):
    def __init__(self, n: int, years: int):

        self._n = n
        self._years = years

        self._db_master = DatabaseWork()

        super().__init__()
        self.title("Variant 11")

        # region table_init
        self._table_frame = ttk.Frame(master=self, borderwidth=2, relief=tk.SOLID, padding=5)
        self._table_frame.pack(padx=10, pady=10)

        self._table_columns = ("Country", "Year", "Tourists_count")
        self._table = ttk.Treeview(master=self._table_frame, columns=self._table_columns, show="headings")
        self._table.pack(fill=tk.BOTH, expand=1)
        self._fill_table()
        # endregion
        # region graphic_init
        self._graphic_frame = ttk.Frame(master=self, borderwidth=2, relief=tk.SOLID, padding=5)
        self._graphic_frame.pack(padx=10, pady=10)

        self._fig = Figure(figsize=(5, 3), dpi=150)
        self._ax = self._fig.add_subplot()
        self._ax.set_title("Графики и прогнозы")
        self._ax.set_xlabel("Years")
        self._ax.set_ylabel("Peoples")
        self._ax.grid(which='major')

        canvas = FigureCanvasTkAgg(self._fig, master=self._graphic_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self._fill_graphic()
        self._ax.legend()
        # endregion

    def _fill_table(self):
        self._table.heading("Country", text="Country")
        self._table.heading("Year", text="Year")
        self._table.heading("Tourists_count", text="Tourists_count")

        for record in self._db_master.get_all_data():
            self._table.insert("", tk.END, values=record)

    def _fill_graphic(self):
        for country in ("Франция", "США", "Китай"):
            data = self._db_master.get_country_data(country)
            new_data = SlicePrognoses.calculate(data, self._n, self._years)
            data = list(map(lambda x: x[1:], data))
            new_data = list(map(lambda x: x[1:], new_data))

            if country == "Франция":
                self._ax.plot(range(data[0][0], data[-1][0] + 1), [x[1] for x in data],
                              'r', marker='o', markersize=2, label="Франция")
                self._ax.plot([int(x[0]) for x in new_data], [x[1] for x in new_data],
                              '--r', marker='o', markersize=2)
            elif country == "США":
                self._ax.plot(range(data[0][0], data[-1][0] + 1), [x[1] for x in data],
                              'b', marker='o', markersize=2, label="США")
                self._ax.plot([int(x[0]) for x in new_data], [x[1] for x in new_data],
                              '--b', marker='o', markersize=2)
            else:
                self._ax.plot(range(data[0][0], data[-1][0] + 1), [x[1] for x in data],
                              'k', marker='o', markersize=2, label="Китай")
                self._ax.plot([int(x[0]) for x in new_data], [x[1] for x in new_data],
                              '--k', marker='o', markersize=2)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    matplotlib.rcParams.update({'font.size': 6})
    a = StatisticWindow(3, 6)
    a.run()
