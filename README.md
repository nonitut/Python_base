# Типы данных в Python

Python поддерживает несколько типов данных, которые можно разделить на категории: **примитивные типы** и **структуры данных**.

| **Тип данных**     | **Пример**                 | **Описание**                                                                      |
|---------------------|----------------------------|----------------------------------------------------------------------------------|
| **int**            | `42`, `-7`, `0`            | Целые числа. Поддерживают произвольную точность.                                |
| **float**          | `3.14`, `-0.001`, `1.0e10` | Числа с плавающей точкой.                                                       |
| **complex**        | `1+2j`, `-3j`              | Комплексные числа с действительной и мнимой частями.                            |
| **bool**           | `True`, `False`            | Логические значения, подкласс `int`.                                            |
| **str**            | `"hello"`, `'world'`       | Строки (последовательности символов).                                           |
| **bytes**          | `b"hello"`                 | Последовательности байтов.                                                      |
| **list**           | `[1, 2, 3]`                | Изменяемая упорядоченная коллекция объектов любого типа.                        |
| **tuple**          | `(1, 2, 3)`                | Неизменяемая упорядоченная коллекция объектов.                                  |
| **range**          | `range(5)`                 | Последовательность чисел, полезна для итераций.                                 |
| **set**            | `{1, 2, 3}`                | Неупорядоченная коллекция уникальных объектов.                                  |
| **frozenset**      | `frozenset({1, 2, 3})`     | Неизменяемое множество.                                                        |
| **dict**           | `{"key": "value"}`         | Словарь (хэш-таблица) для хранения пар "ключ-значение".                         |
| **NoneType**       | `None`                     | Специальный тип для обозначения отсутствия значения.                            |

## Проверка типов



В Python можно проверить тип данных объекта с помощью функции `type()`:

```python
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("hello"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2, 3]))    # <class 'list'>
print(type({"key": "value"}))  # <class 'dict'>
**

## Проверка типов

| **Характеристика**         | **Словарь (dict)**                                      | **Кортеж (tuple)**                        | **Список (list)**                          |
|----------------------------|---------------------------------------------------------|-------------------------------------------|--------------------------------------------|
| **Синтаксис**              | `{ключ: значение}`                                      | `(элемент1, элемент2)`                    | `[элемент1, элемент2]`                     |
| **Изменяемость**           | Изменяемый: можно добавлять/удалять пары                | Неизменяемый: нельзя изменять элементы    | Изменяемый: можно добавлять/удалять элементы |
| **Порядок**                | С Python 3.7 порядок сохраняется                       | Порядок сохраняется                       | Порядок сохраняется                        |
| **Доступ к элементам**     | По ключу: `dict["ключ"]`                                | По индексу: `tuple[0]`                    | По индексу: `list[0]`                      |
| **Повторяющиеся элементы** | Ключи уникальны, значения могут повторяться             | Могут повторяться                         | Могут повторяться                          |
| **Основное назначение**    | Ассоциативное хранение данных                           | Хранение неизменяемых последовательностей | Хранение изменяемых последовательностей    |
| **Пример**                 | `{"имя": "Аня", "возраст": 25}`                        | `("яблоко", "банан", "вишня")`            | `["яблоко", "банан", "вишня"]`             |
| **Методы**                 | Много методов (`.keys()`, `.values()`, `.items()`)      | Почти нет методов (`.count()`, `.index()`) | Много методов (`.append()`, `.remove()`)   |
| **Скорость работы**        | Быстрее поиска по ключам                                | Быстрее списка (из-за неизменяемости)     | Медленнее при большом количестве операций  |
| **Использование памяти**   | Требует больше памяти, чем списки или кортежи           | Наиболее экономичен                       | Занимает больше памяти, чем кортежи        |
