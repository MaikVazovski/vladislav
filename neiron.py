import numpy as np

password_combinations = np.array(
    [
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
)
locked_unlocked = np.array([
    [0],
    [1],
    [0],
    [1],
    [1],
    [0]
])
weights = np.array([0.5, 0.48, -0.7])
alpha = 0.1

# первая комбинация паролей
input_data = password_combinations[0]

# что хотим понять: открыто или закрыто?
goal_prediction = locked_unlocked[0]

for iteration in range(100):

    # общая ошибка
    error = 0

    print(f'Веса: {weights}')

    # вложенный цикл
    for row in range(len(locked_unlocked)):
        # prediction = input_data.dot(weights)
        input_data = password_combinations[row]
        goal_prediction = locked_unlocked[row]

        # прогноз
        prediction = input_data.dot(weights)
        # print(f'Предсказание: {prediction}')
        # ошибка
        delta = prediction - goal_prediction
        error = delta**2
        # изменяем веса
        weights = weights - (alpha*(input_data*delta))

    print(f'Ошибка: {float(error)} \n')
