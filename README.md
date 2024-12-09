# Python Типы данных в Python Основные типы данных

# 1. **Числовые типы**
- **`int`**: Целые числа (например, `42`, `-5`).
- **`float`**: Числа с плавающей точкой (например, `3.14`, `-0.01`).
- **`complex`**: Комплексные числа (например, `1+2j`, `-3j`).

# 2. **Логический тип**
- **`bool`**: Логические значения (`True`, `False`).

# 3. **Последовательности**
- **`str`**: Строки (например, `"Hello, World!"`, `'Python'`).
- **`list`**: Списки, изменяемые (например, `[1, 2, 3]`, `['a', 'b', 'c']`).
- **`tuple`**: Кортежи, неизменяемые (например, `(1, 2, 3)`, `('a', 'b', 'c')`).
- **`range`**: Диапазоны (например, `range(10)`, `range(1, 5)`).

# 4. **Множества**
- **`set`**: Наборы уникальных элементов, изменяемые (например, `{1, 2, 3}`, `{'a', 'b', 'c'}`).
- **`frozenset`**: Наборы уникальных элементов, неизменяемые.

# 5. **Сопоставления (отображения)**
- **`dict`**: Словари (например, `{'key': 'value', 'name': 'John'}`).

# 6. **Тип None**
- **`NoneType`**: Единственное значение этого типа — `None`. Используется для обозначения отсутствия значения.

# 7. **Бинарные типы данных**
- **`bytes`**: Последовательности байтов (например, `b"hello"`).
- **`bytearray`**: Изменяемые последовательности байтов.
- **`memoryview`**: Представление объекта памяти.

# 8. **Типы для работы с числами в модулях**
- Например, `Decimal` и `Fraction` из модуля `fractions` для работы с дробями и точной арифметикой.

# Как узнать тип данных?

Используйте встроенные функции Python:
- **`type()`**: Для определения типа объекта.
- **`isinstance()`**: Для проверки принадлежности объекта к определённому типу.





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
