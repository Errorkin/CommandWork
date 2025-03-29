import sqlite3

from collections import deque


class SlicePrognoses:
    """
    Функция возвращает копию исходного списка данных, дополненный прогнозами.
    Прогнозы вычисляются на основе буфера.
    """

    @staticmethod
    def calculate(data: list[tuple[str, int, int | float]], n: int, years: int) -> list[tuple[str, int, int | float]]:
        buffer: deque[int | float] = deque((x[2] for x in data[-n:]))
        new_data = data.copy()

        for _ in range(years):
            new_record = (new_data[-1][0], new_data[-1][1] + 1, round(sum(buffer) / n, 2))
            new_data.append(new_record)

            buffer.append(new_data[-1][2])
            buffer.popleft()

        return new_data


class DatabaseWork:
    """
    Класс для работы с базой данных

    Таблица tourists:
    country text
    year int
    tourists_count int
    """

    def __init__(self):
        self.connection = sqlite3.connect("var_11_database.db")
        self.cursor = self.connection.cursor()

    def get_country_data(self, country_name: str) -> list[tuple[str, int, int]]:
        """Возвращает все данные из базы по выбранной стране"""
        query = f"select * from tourists where country = {repr(country_name)}"
        return self.cursor.execute(query).fetchall()

    def get_all_data(self):
        query = "select * from tourists"
        return self.cursor.execute(query).fetchall()


if __name__ == '__main__':
    pass
