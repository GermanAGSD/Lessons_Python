# Рекурсивные функции

def recursive(value):
    print(value)
    if value > 4:
        recursive(value + 1)
    print(value)
recursive(1)
