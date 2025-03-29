import tkinter as tk

from tkinter import ttk

from VovaLogic import DatabaseWork


class StatisticWindow(tk.Tk):
    def __init__(self):
        self._db_master = DatabaseWork()

        super().__init__()

        self.title("Variant 11")

        self._table_frame = ttk.Frame(master=self, borderwidth=2, relief=tk.SOLID, padding=5)
        self._table_frame.grid(row=0, column=0, padx=10)

        self._graphic_frame = ttk.Frame(master=self, borderwidth=2, relief=tk.SOLID, padding=5)
        self._graphic_frame.grid(row=0, column=1, padx=10)

        self._table_columns = ("Country", "Year", "Tourists_count")
        self._table = ttk.Treeview(master=self._table_frame, columns=self._table_columns, show="headings")
        self._table.pack(fill=tk.BOTH, expand=1)
        self._fill_table()

    def _fill_table(self):
        self._table.heading("Country", text="Country")
        self._table.heading("Year", text="Year")
        self._table.heading("Tourists_count", text="Tourists_count")

        for record in self._db_master.get_all_data():
            self._table.insert("", tk.END, values=record)

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    a = StatisticWindow()
    a.run()
