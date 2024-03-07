def ask_question(question, options):
    print(question, options)
    answer = input("Выберите один из вариантов ответа: ")
    while answer not in options:
        answer = input("Пожалуйста, выберите один из предложенных вариантов: ")
    return answer


def scale_number(number, old_min, old_max, new_min, new_max):
    scaled_number = (number - old_min) / (old_max - old_min) * (new_max - new_min) + new_min
    return scaled_number
