# Симуляция Боя

_Этот репозиторий содержит простую игру-симуляцию боя, реализованную на Python. Игра включает персонажей с различными классами и характеристиками, сражающихся друг с другом до определения победителя._

## Возможности:
- **Персонажи: Паладины и Воины с уникальными характеристиками здоровья, брони и атаки.**
- **Случайное Снаряжение: Персонажи могут быть оснащены различными предметами, которые улучшают их характеристики.**
- **Система Боя: Пошаговый бой с случайными исходами атак, включая промахи, обычные удары, слабые удары, критические удары и самоповреждения.**
- **Цветной Вывод: Используется библиотека colorama для цветного текста, чтобы улучшить пользовательский интерфейс.**
## Требования
- Python 3.x
- Библиотека colorama

## Установка

- Клонируйте репозиторий:
```
https://github.com/HarisNvr/arena_game.git
```
- Перейдите в директорию проекта:
```
cd arena_game
```
- Создайте и активируйте виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
- Установите зависимости:
```
pip install -r requirements.txt
```
- Запустите баттлер:
```
python arena_game.py
```

## Логика игры

### Инициализация:

- Создаются четыре персонажа (Паладины или Воины) случайным образом.
- Каждому персонажу присваивается уникальное имя.
- Персонажи оснащаются от 0 до 4 случайными предметами, которые модифицируют их базовые характеристики.
### Бой:

- Персонажи попарно сражаются друг с другом.

**Каждый ход определяется атакой с помощью 20-гранного кубика, что приводит к различным исходам:**

- Критический промах (самоповреждение)
- Промах (урон не наносится)
- Слабый удар (0,5х множитель урона)
- Обычный удар (1х множитель урона)
- Критический удар (2х множитель урона)
