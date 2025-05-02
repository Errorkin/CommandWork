import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from tkinter import Tk, Label, StringVar, Entry
from tkinter import ttk
from crime_data import data_json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from tkinter import Tk, Label, StringVar, Entry
from tkinter import ttk
from crime_data import data_json

# создаем DataFrame из JSON-данных
crime_data = pd.DataFrame(data_json).T.reset_index()
crime_data.columns = ["Год", "Кража", "Убийство", "Мошенничество"]
crime_data["Год"] = crime_data["Год"].astype(int)

# функция для расчета прогноза преступности по скользящей средней
def calculate_forecast(data, target_year, n=3):
    current_year = data["Год"].iloc[-1]
    future_years = list(range(current_year + 1, target_year + 1))
    forecast_data = {year: {} for year in future_years}

    # расчет прогноза для каждого типа преступления
    for crime_type in ["Кража", "Убийство", "Мошенничество"]:
        series = list(data[crime_type])
        for year in future_years:
            if len(series) >= n:
                rolling_mean = np.mean(series[-n:])
            else:
                rolling_mean = series[-1]
            forecast_data[year][crime_type] = round(rolling_mean)
            series.append(rolling_mean)

    return forecast_data

# обновление данных с добавлением прогноза
def update_data_with_forecast(data, forecast_data):
    forecast_years = list(forecast_data.keys())
    forecast_df = pd.DataFrame(forecast_data).T
    forecast_df["Год"] = forecast_years
    combined_data = pd.concat([data, forecast_df], ignore_index=True)
    return combined_data

# построение графика статистики с прогнозом
def plot_crime_trends_with_forecast(data, target_year, n):
    forecast_data = calculate_forecast(data, target_year, n)
    combined_data = update_data_with_forecast(data, forecast_data)

    # визуализация данных
    plt.figure(figsize=(12, 7))
    for crime_type in ["Кража", "Убийство", "Мошенничество"]:
        plt.plot(combined_data["Год"], combined_data[crime_type], marker='o', label=crime_type)

    plt.title("Статистика преступности с прогнозом", fontsize=14)
    plt.xlabel("Год", fontsize=12)
    plt.ylabel("Количество случаев", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# отображение таблицы данных в окне
def show_table():
    for row in treeview.get_children():
        treeview.delete(row)
    for index, row in crime_data.iterrows():
        treeview.insert("", "end", values=(row["Год"], row["Кража"], row["Убийство"], row["Мошенничество"]))

# построение графика статистики
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

# отображение графика статистики
def show_trends():
    plot_crime_trends(crime_data)

# отображение графика с прогнозом
def show_forecast():
    try:
        target_year = int(year_input.get())  # целевой год
        n = int(n_input.get())  # количество лет для прогноза
        plot_crime_trends_with_forecast(crime_data, target_year, n)
    except ValueError:
        print("Ошибка: Убедитесь, что введены корректные числа для года и n.")

# создаем окно
root = Tk()
root.title("Статистика преступности")

# заголовок
header_label = Label(root, text="Добро пожаловать! Выберите опцию:", font=("Helvetica", 16, "bold"), foreground="black")
header_label.grid(row=0, column=0, columnspan=2, pady=20)

# кнопки
btn_style = ttk.Style()
btn_style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#4CAF50", foreground="black")

ttk.Button(root, text="1) Показать таблицу данных", command=show_table, style="TButton").grid(row=1, column=0, sticky="ew", padx=20, pady=10)
ttk.Button(root, text="2) Построить график статистики преступности", command=show_trends, style="TButton").grid(row=2, column=0, sticky="ew", padx=20, pady=10)

# ввод данных для прогноза
Label(root, text="Введите год для прогноза:", font=("Arial", 12), foreground="black").grid(row=3, column=0, padx=20, pady=10)
year_input = StringVar()
Entry(root, textvariable=year_input, font=("Arial", 12), width=10).grid(row=3, column=1, padx=20, pady=10)

Label(root, text="Введите количество лет для прогноза (n):", font=("Arial", 12), foreground="black").grid(row=4, column=0, padx=20, pady=10)
n_input = StringVar()
Entry(root, textvariable=n_input, font=("Arial", 12), width=10).grid(row=4, column=1, padx=20, pady=10)

# кнопка для построения прогноза
ttk.Button(root, text="3) Построить прогноз", command=show_forecast, style="TButton").grid(row=5, column=0, columnspan=2, padx=20, pady=10)

# таблица
treeview = ttk.Treeview(root, columns=("Год", "Кража", "Убийство", "Мошенничество"), show="headings")
treeview.heading("Год", text="Год")
treeview.heading("Кража", text="Кража")
treeview.heading("Убийство", text="Убийство")
treeview.heading("Мошенничество", text="Мошенничество")
treeview.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()
crime_data = pd.DataFrame(data_json).T.reset_index()
crime_data.columns = ["Год", "Кража", "Убийство", "Мошенничество"]
crime_data["Год"] = crime_data["Год"].astype(int)

# Функция для расчета прогноза преступности по скользящей средней
def calculate_forecast(data, target_year, n=3):
    current_year = data["Год"].iloc[-1]
    future_years = list(range(current_year + 1, target_year + 1))

    forecast_data = {year: {} for year in future_years}

    for crime_type in ["Кража", "Убийство", "Мошенничество"]:
        series = list(data[crime_type])

        for year in future_years:
            if len(series) >= n:
                rolling_mean = np.mean(series[-n:])
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
def plot_crime_trends_with_forecast(data, target_year, n):
    forecast_data = calculate_forecast(data, target_year, n)
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
        n = int(n_input.get())  # Получаем количество лет для прогноза из ввода
        plot_crime_trends_with_forecast(crime_data, target_year, n)
    except ValueError:
        print("Ошибка: Убедитесь, что введены корректные числа для года и n.")

# Настроим окно
root = Tk()
root.title("Статистика преступности")

# Заголовок
header_label = Label(root, text="Добро пожаловать! Выберите опцию:", font=("Helvetica", 16, "bold"), foreground="black")
header_label.grid(row=0, column=0, columnspan=2, pady=20)

# Кнопки
btn_style = ttk.Style()
btn_style.configure("TButton", font=("Arial", 12), padding=10, relief="flat", background="#4CAF50", foreground="black")

ttk.Button(root, text="1) Показать таблицу данных", command=show_table, style="TButton").grid(row=1, column=0, sticky="ew", padx=20, pady=10)
ttk.Button(root, text="2) Построить график статистики преступности", command=show_trends, style="TButton").grid(row=2, column=0, sticky="ew", padx=20, pady=10)

# Ввод года для прогноза и количество лет для скользящей средней
Label(root, text="Введите год для прогноза:", font=("Arial", 12), foreground="black").grid(row=3, column=0, padx=20, pady=10)
year_input = StringVar()
Entry(root, textvariable=year_input, font=("Arial", 12), width=10).grid(row=3, column=1, padx=20, pady=10)

Label(root, text="Введите количество лет для прогноза (n):", font=("Arial", 12), foreground="black").grid(row=4, column=0, padx=20, pady=10)
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
