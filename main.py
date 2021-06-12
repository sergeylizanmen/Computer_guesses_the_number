
"""
Консольная игра, в которой компьютер отгадывает число от 1 до 100 за семь попыток

Для решения задачи используется алгоритм Бинарного поиска
"""

print('Загадайте число от 1 до 100, а я попробую его отгадать за семь попыток')

counter = 0
left_border = 1
right_border = 100

while True:

    middle_number = (left_border + right_border) // 2
    print(f'\nТвое число равно, меньше или больше, чем {middle_number}?')
    choice = input('1 — равно, 2 — больше, 3 — меньше: ')

    if choice == '1':
        print(f'Твое число = {middle_number}:)')
        break
    elif choice == '2':
        left_border = middle_number
    elif choice == '3':
        right_border = middle_number
    else:
        print('Неправильный ввод команды')
        continue
    counter += 1
print(f'Число попыток: {counter}')