from collections import deque


class SlicePrognoses:
    """
    Функция возвращает исходный список данных, дополненный прогнозами.
    Прогнозы вычисляются на основе буфера.
    """
    @staticmethod
    def calculate(data: list[float | int], n: int, years: int):
        buffer: deque[float | int] = deque(data[-n:])
        data_with_prognoses: list[float | int] = data.copy()
        now_year: int = 0

        while now_year < years:
            data_with_prognoses.append(round(sum(buffer) / n, 2))
            buffer.append(data_with_prognoses[-1])
            buffer.popleft()

            now_year += 1

        return data_with_prognoses


if __name__ == '__main__':
    print(SlicePrognoses.calculate([60, 85, 80, 92, 88, 96], 3, 2))
