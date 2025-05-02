import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from tkinter import Tk, Label, Button, Entry, StringVar
from tkinter import ttk
from crime_data import data_json


# JSON файл с данными о преступности
crime_data = pd.DataFrame(data_json).T.reset_index()
crime_data.columns = ["Год", "Кража", "Убийство", "Мошенничество"]
crime_data["Год"] = crime_data["Год"].astype(int)
# Функция для расчета прогноза преступности по скользящей средней
def calculate_forecast(data, target_year, n=3):
    # Берем данные до текущего года для прогноза
    current_year = data["Год"].iloc[-1]
    future_years = list(range(current_year + 1, target_year + 1))

    forecast_data = {year: {} for year in future_years}

    for crime_type in ["Кража", "Убийство", "Мошенничество"]:
        series = list(data[crime_type])

        # Прогноз на основе скользящей средней (с учетом последних n лет)
        for year in future_years:
            if len(series) >= n:
                rolling_mean = np.mean(series[-n:])
            else:
                rolling_mean = series[-1]  # если меньше данных, просто берём последнее значение
            forecast_data[year][crime_type] = round(rolling_mean)  # Округляем до целого
            series.append(rolling_mean)

    return forecast_data


# Функция для обновления данных и объединения прогноза с исходными данными
def update_data_with_forecast(data, forecast_data):
    # Обновляем данные с прогнозами
    forecast_years = list(forecast_data.keys())
    forecast_df = pd.DataFrame(forecast_data).T
    forecast_df["Год"] = forecast_years
    combined_data = pd.concat([data, forecast_df], ignore_index=True)
    return combined_data


# Функция для построения графика статистики преступности
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


# Функция для построения графика статистики с прогнозом
def plot_crime_trends_with_forecast(data, target_year):
    # Считаем прогнозные данные
    forecast_data = calculate_forecast(data, target_year)

    # Обновляем данные с прогнозами
    combined_data = update_data_with_forecast(data, forecast_data)

    # Строим график
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
def show_trends():
    plot_crime_trends(crime_data)


def show_forecast():
    try:
        target_year = int(year_input.get())
        if target_year > crime_data["Год"].iloc[-1]:
            plot_crime_trends_with_forecast(crime_data, target_year)
        else:
            print("Пожалуйста, введите год больше последнего года в наборе данных.")
    except ValueError:
        print("Некорректный ввод года. Пожалуйста, введите правильный год.")


root = Tk()
root.title("Статистика преступности")

Label(root, text="Добро пожаловать! Выберите опцию:").grid(row=0, column=0, columnspan=2)
Button(root, text="1) Показать таблицу данных", command=show_table).grid(row=1, column=0, sticky="ew")
Button(root, text="2) Построить график статистики преступности", command=show_trends).grid(row=2, column=0, sticky="ew")

Label(root, text="Введите год для прогноза:").grid(row=3, column=0)
year_input = StringVar()
Entry(root, textvariable=year_input).grid(row=3, column=1)
Button(root, text="3) Построить прогноз", command=show_forecast).grid(row=4, column=0, columnspan=2, sticky="ew")

treeview = ttk.Treeview(root, columns=("Год", "Кража", "Убийство", "Мошенничество"), show="headings")
treeview.heading("Год", text="Год")
treeview.heading("Кража", text="Кража")
treeview.heading("Убийство", text="Убийство")
treeview.heading("Мошенничество", text="Мошенничество")
treeview.grid(row=5, column=0, columnspan=2)

root.mainloop()
