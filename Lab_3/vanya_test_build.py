import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from tkinter import Tk, Label, StringVar, Entry, messagebox
from tkinter import ttk
from crime_data import data_json
from tkinter import Toplevel

def start():
    crime_data = pd.DataFrame(data_json).T.reset_index()
    crime_data.columns = ["Год", "Кража", "Убийство", "Мошенничество"]
    crime_data["Год"] = crime_data["Год"].astype(int)

    # Функция для расчета прогноза преступности по скользящей средней
    def calculate_forecast(data, target_year, nn=3):
        current_year = data["Год"].iloc[-1]
        future_years = list(range(current_year + 1, target_year + 1))

        forecast_data = {year: {} for year in future_years}

        for crime_type in ["Кража", "Убийство", "Мошенничество"]:
            series = list(data[crime_type])

            for year in future_years:
                if len(series) >= nn:
                    rolling_mean = np.mean(series[-nn:])
                else:
                    rolling_mean = series[-1]
                forecast_data[year][crime_type] = round(rolling_mean)
                series.append(rolling_mean)

        return forecast_data

    # Функция для обновления данных и объединения прогноза с исходными данными
    def update_data_with_forecast(data, forecast_data):
        forecast_years = list(forecast_data.keys())
        forecast_df = pd.DataFrame(forecast_data).T
        forecast_df["Год"] = forecast_years
        combined_data = pd.concat([data, forecast_df], ignore_index=True)
        return combined_data

    # Функция для построения графика статистики с прогнозом
    def plot_crime_trends_with_forecast(data, target_year, nn):
        forecast_data = calculate_forecast(data, target_year, nn)
        combined_data = update_data_with_forecast(data, forecast_data)

        plt.figure(figsize=(12, 7))
        for crime_type in ["Кража", "Убийство", "Мошенничество"]:
            plt.plot(combined_data["Год"], combined_data[crime_type], marker='o', label=crime_type)

        plt.title("Статистика преступности с прогнозом", fontsize=14)
        plt.xlabel("Год", fontsize=12)
        plt.ylabel("Количество случаев", fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.show()

    # Функция для отображения таблицы данных в окне
    def show_table():
        for row in treeview.get_children():
            treeview.delete(row)
        for index, row in crime_data.iterrows():
            treeview.insert("", "end", values=(row["Год"], row["Кража"], row["Убийство"], row["Мошенничество"]))

    # GUI
    # Функция для построения графика статистики
    def plot_crime_trends(data):
        plt.figure(figsize=(12, 7))
        for crime_type in ["Кража", "Убийство", "Мошенничество"]:
            plt.plot(data["Год"], data[crime_type], marker='o', label=crime_type)

        plt.title("Статистика преступности", fontsize=14)
        plt.xlabel("Год", fontsize=12)
        plt.ylabel("Количество случаев", fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.show()

    # Упрощенная функция для отображения графика
    def show_trends():
        plot_crime_trends(crime_data)
    # Функция для отображения графика с прогнозом
    def show_forecast():
        try:
            target_year = int(year_input.get())  # Получаем целевой год из ввода
            nn = int(n_input.get())  # Получаем количество лет для прогноза из ввода
            plot_crime_trends_with_forecast(crime_data, target_year, nn)
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректные данные")

    def calculate_crime_reduction(data):
        reduction = {}
        for crime_type in ["Кража", "Убийство", "Мошенничество"]:
            start_value = data[crime_type].iloc[0]
            end_value = data[crime_type].iloc[-1]
            reduction[crime_type] = start_value - end_value  # Вычисляем снижение
        max_reduction = max(reduction, key=reduction.get)  # Наибольшее снижение
        min_reduction = min(reduction, key=reduction.get)  # Наименьшее снижение
        return max_reduction, min_reduction, reduction

    # Добавляем новую функцию для отображения информации о снижении
    def show_crime_reduction():
        max_reduction, min_reduction, reduction = calculate_crime_reduction(crime_data)
        message = (
            f"Вид преступности с наибольшим снижением: {max_reduction} ({reduction[max_reduction]} случаев)\n"
            f"Вид преступности с наименьшим снижением: {min_reduction} ({reduction[min_reduction]} случаев)"
        )
        messagebox.showinfo("Результаты анализа", message)

    # Настроим окно
    root = Toplevel()

    root.title("Статистика преступности")

    # Заголовок
    header_label = Label(root, text="Добро пожаловать! Выберите опцию:", font=("Helvetica", 16, "bold"), foreground="black")
    header_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Кнопки
    btn_style = ttk.Style()
    btn_style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#4CAF50", foreground="black")
    # Добавляем кнопку в интерфейс для запуска анализа
    ttk.Button(
        root,
        text="4) Анализ снижения преступности",
        command=show_crime_reduction
    ).grid(
        row=7, column=0, columnspan=2, padx=20, pady=20, ipadx=20, ipady=10
    )
    ttk.Button(root, text="1) Показать таблицу данных", command=show_table, style="TButton").grid(row=1, column=0, sticky="ew", padx=20, pady=10)
    ttk.Button(root, text="2) Построить график статистики преступности", command=show_trends, style="TButton").grid(row=2, column=0, sticky="ew", padx=20, pady=10)

    # Ввод года для прогноза и количество лет для скользящей средней
    Label(root, text="Введите год для прогноза:", font=("Arial", 12), foreground="black").grid(row=3, column=0, padx=20, pady=10)
    year_input = StringVar()
    Entry(root, textvariable=year_input, font=("Arial", 12), width=10).grid(row=3, column=1, padx=20, pady=10)

    Label(root, text="Введите количество лет для прогноза (nn):", font=("Arial", 12), foreground="black").grid(row=4, column=0, padx=20, pady=10)
    n_input = StringVar()
    Entry(root, textvariable=n_input, font=("Arial", 12), width=10).grid(row=4, column=1, padx=20, pady=10)

    # Кнопка для построения графика с прогнозом
    ttk.Button(root, text="3) Построить прогноз", command=show_forecast, style="TButton").grid(row=5, column=0, columnspan=2, padx=20, pady=10)

    # Настройка Treeview для отображения таблицы
    treeview = ttk.Treeview(root, columns=("Год", "Кража", "Убийство", "Мошенничество"), show="headings")
    treeview.heading("Год", text="Год")
    treeview.heading("Кража", text="Кража")
    treeview.heading("Убийство", text="Убийство")
    treeview.heading("Мошенничество", text="Мошенничество")
    treeview.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

    root.mainloop()
if "__main__" == __name__:
    start()