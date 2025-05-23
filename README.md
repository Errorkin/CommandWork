# Туристический поток и статистика преступности в России

## Описание проекта
В рамках проекта была реализована программа для анализа и визуализации данных о туристическом потоке и преступности в России за последние 15 лет. Программа предоставляет пользователю возможность работать с этими данными через графический интерфейс, а также включает инструменты для построения прогнозов на основе метода скользящей средней.

## Функционал программы

### Анализ туристического потока
1. **Отображение данных:** 
   - Загрузка данных о туристическом потоке.
   - Отображение информации в удобном табличном формате.
2. **Построение графиков зависимости от года:**
   - Графики показывают изменения числа туристов из различных стран (Франция, США, Китай) за указанный период.
3. **Анализ данных:** 
   - Определение страны, из которой приехало больше всего туристов за последние 15 лет.
   - Определение страны с наименьшим количеством туристов за тот же период.
4. **Прогнозирование:**
   - Построение прогнозов на последующие N лет методом экстраполяции по скользящей средней.
   - Визуализация прогнозов на графике с выделением будущих данных другим цветом.

### Анализ преступности
1. **Отображение данных:**
   - Представление информации в табличной форме.
2. **Построение графиков зависимости от года:**
   - Графики показывают динамику различных видов преступлений за последние 15 лет.
3. **Анализ данных:** 
   - Определение вида преступности, который снизился больше всего за указанный период.
   - Выявление вида преступности с наименьшим снижением.
4. **Прогнозирование:**
   - Построение прогнозов на следующие N лет методом скользящей средней.
   - Отображение прогнозов на графике.

## Технологический стек
- **Python** — основной язык разработки.
- **pandas** — для обработки и анализа данных.
- **numpy** — для вычислений.
- **matplotlib** — для построения графиков.
- **tkinter** — для создания графического интерфейса пользователя (GUI).

## Организация разработки
Разработка велась в командном режиме с использованием системы контроля версий **Git**, что позволило:
- Эффективно разделить задачи между участниками команды.
- Поддерживать контроль версий и синхронизацию изменений.
- Упростить интеграцию функционала.

## Использование
1. Запустите программу.
2. Выберите один из режимов работы: "Вова" или "Ваня".
3. Выберите нужное действие: отображение таблицы, построение графика или прогнозов.
4. Введите параметры прогноза (например, количество лет) и получите результаты в графическом формате.
