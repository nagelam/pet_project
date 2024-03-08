from functions import ask_question, scale_number

class UserProfiler:
    def __init__(self):
        self.profile = {}
        self.collect_user_info()

    def collect_user_info(self):
        self.profile['gender'] = ask_question("Ваш пол? (f, m): ", ["f", "m"])
        if self.profile['gender'] == 'f':
            self.profile['gender_cd_F'] = True
        else:
            self.profile['gender_cd_M'] = True
        self.profile['has_car'], self.profile['foreign_car'] = self.ask_car_info()
        self.profile['has_passport'] = ask_question("Есть ли у вас заграничный паспорт? (y, n): ", ["y", "n"])
        self.profile['age_range'] = ask_question("Ваш возраст? (18-24, 24-32, 32-38, 38-44, 44-55, 55-60, 60+): ",
                                                     ["18-24", "24-32", "32-38", "38-44", "44-55", "55-60", "60+"])
        self.profile['credit_denials'] = ask_question("Количество отказанных заявок на кредит в прошлом? (0-1, 2-3, 3-4, 4-5, 6-7, 8-9, 10+): ",
                                                          ["0-1", "2-3", "3-4", "4-5", "6-7", "8-9", "10+"])
        self.profile['working_experience'] = ask_question("Вы работаете больше года? (y, n): ", ["y", "n"])
        self.profile['credit_rating'] = int(input("Каков ваш кредитный рейтинг в БКИ от 0 до 1000? "))
        self.profile['scaled_credit_rating'] = scale_number(self.profile['credit_rating'], 0, 1000, -3.5, 0)
        self.profile['income'] = ask_question("Ваша зарплата (выберите верный пункт): (a) 0-60000, (b) 60000-100000, (c) 100000-200000, (d) больше 200000): ",
                                          ["a", "b", "c", "d"])
        self.profile['bki_request'] = ask_question("Количество запросов в бк? (0-1, 2-3, 3-4, 4-5, 6-7, 8-9, 10+): ",
                                               ["0-1", "2-3", "3-4", "4-5", "6-7", "8-9", "10+"])
        self.profile['first_loan'] = ask_question("Вы давно брали свой первый кредит? 1) пока не брал 2) брал в течение года, 3) брал больше года, 4) брал очень давно: ",
                                             ["1", "2", "3", "4"])
        self.profile['education_level'] = ask_question("Какой у вас уровень образования? (SCH - школьное образование, GRD - выпускник, UGR - старшекурсник, PGR - аспирант, ACD - академик): ",
                                                 ["SCH", "GRD", "UGR", "PGR", "ACD"])
        print("Спасибо за ваши ответы!")

    def ask_car_info(self):
        has_car = ask_question("Есть ли у вас машина? (y/n): ", ["y", "n"])
        if has_car == "y":
            foreign_car = ask_question("Это иностранная машина? (y/n): ", ["y", "n"])
        else:
            foreign_car = ""
        return has_car, foreign_car
