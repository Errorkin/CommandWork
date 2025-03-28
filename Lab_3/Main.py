import tkinter as tk

from tkinter import ttk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("Лабораторная №3")
        self.geometry(f"{400}x{275}+{550}+{250}")
        self.resizable(False, False)

        # Надпись "Выберите вариант"
        _label_choice = ttk.Label(self, text="Выберите вариант:")
        _label_choice.pack(pady=(20, 5))

        # Выпадающий список с вариантами "Вова" и "Ваня"
        self._choice_var = tk.StringVar()
        self._choice_combobox = ttk.Combobox(
            self,
            textvariable=self._choice_var,
            values=["Вова", "Ваня"],
            state="readonly"
        )
        self._choice_combobox.pack(pady=5)
        self._choice_combobox.current(0)  # Устанавливаем "Вова" по умолчанию

        # Надпись "Введите n"
        self._label_n = ttk.Label(self, text="Введите n от 2 до 15:")
        self._label_n.pack(pady=(10, 5))

        # Поле для ввода числа n
        self._n_entry = ttk.Entry(self)
        self._n_entry.pack(pady=5)

        # Надпись количество лет
        self._label_years = ttk.Label(self, text="Введите количество лет для прогноза (от 1 до 10)")
        self._label_years.pack(pady=(10, 5))

        # Поле для ввода количества лет
        self._years_entry = ttk.Entry(self)
        self._years_entry.pack(pady=5)

        # Кнопка "Выполнить!"
        self._execute_button = ttk.Button(self, text="Выполнить!", command=self._main)
        self._execute_button.pack(pady=(15, 0))

    @staticmethod
    def _is_valid(n: str, years: str) -> bool:
        """Проверка данных на корректность"""
        try:
            int(n)
            int(years)
        except (TypeError, ValueError):
            return False

        n = int(n)
        years = int(years)

        if 2 <= n <= 15 and 1 <= years <= 10:
            return True
        return False

    def _main(self):
        n = self._n_entry.get()
        years = self._years_entry.get()
        variant = self._choice_combobox.get()

        if not self._is_valid(n, years):
            messagebox.showerror("Ошибка", "Некорректные данные")
        else:
            n = int(n)
            years = int(years)

            if variant == "Вова":
                pass
            elif variant == "Ваня":
                pass

    def run(self):
        self.mainloop()

    def _Vova_task(self, n: int):
        pass

    def _Vanya_task(self, n: int):
        pass

    """
        Идея такая:
        По нажатию кнопки открывать новое окно, и в нем реализовывать свой вариант
        (строить графики, таблицы и т.п.)

        Чтобы ничего друг другу не поломать, разделил работу на 2 функции выше. 
        Работаем каждый в своей функции 
    """


if __name__ == "__main__":
    app = App()
    app.run()
