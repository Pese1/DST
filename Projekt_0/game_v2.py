"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Вводим счётчик попыток
    number = np.random.randint(1, 101) # присваиваем переменной number сгенерированное число
    min = 0 # задаём минимальное значение в переменной min
    max = 100 # максимум в max
    while True:
        count += 1
        predict_number = round((min + max)/2) # предполагаемое число округлённое среднее между min и max (50)
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number: # если загаданное число больше предполагаемого (> 50)
            min = predict_number # предполагаемое становится минимальным
            predict_number = round(min + max)/2 # новое предполагаемое число - это среднее между 50 и 100 
        elif number < predict_number: # если загаданное меньше
            max = predict_number # предполагаемое становится максимальным
            predict_number = round (min + max)/2
    return(count)
print(f'Количество попыток: {random_predict()}')    

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
if __name__ == '__main__':
    score_game(random_predict)   