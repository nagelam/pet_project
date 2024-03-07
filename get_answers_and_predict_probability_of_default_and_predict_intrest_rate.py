from functions import ask_question, scale_number

gender = ask_question("Ваш пол? (F - женский, M - мужской): ", ["f", "m"])
has_car = ask_question("Есть ли у вас машина? (y/n): ", ["y", "n"])
if has_car == "y":
    foreign_car = ask_question("Это иностранная машина? (y/n): ", ["y", "n"])
else:
    foreign_car = ""
has_passport = ask_question("Есть ли у вас заграничный паспорт? (y, n): ", ["y", "n"])

age_range = ask_question("Ваш возраст? (18-24, 24-32, 32-38, 38-44, 44-55, 55-60, 60+): ",
                         ["18-24", "24-32", "32-38", "38-44", "44-55", "55-60", "60+"])
credit_denials = ask_question("Количество отказанных заявок на кредит в прошлом? (0-1, 2-3, 3-4, 4-5, 6-7, 8-9, 10+): ",
                              ["0-1", "2-3", "3-4", "4-5", "6-7", "8-9", "10+"])
working_experience = ask_question("Вы работаете больше года? (y, n): ", ["y", "n"])

credit_rating = int(input("Каков ваш кредитный рейтинг в БКИ от 0 до 1000? "))
scaled_credit_rating = scale_number(credit_rating, 0, 1000, -3.5, 0)

income = ask_question(
    "Ваша зарплата(выберите верный пункт): ( a) 0-60000, b)60000-100000, c)100000-200000, d)больше 200000): ",
    ["a", "b", "c", "d"])

bki_request = ask_question("Количество запросов в бки? (0-1, 2-3, 3-4, 4-5, 6-7, 8-9, 10+): ",
                           ["0-1", "2-3", "3-4", "4-5", "6-7", "8-9", "10+"])

first_loan = ask_question(
    "Вы давно брали свой первый кредит? 1) пока не брал 2) брал в течение года, 3) брал больше года, 4) брал очень давно: ",
    ["1", "2", "3", "4"])

education_level = ask_question(
    "Какой у вас уровень образования? (SCH - школьное образование, GRD - выпускник, UGR - старшекурсник, PGR - аспирант, ACD - академик): ",
    ["SCH", "GRD", "UGR", "PGR", "ACD"])

print("Спасибо за ваши ответы!")

import pandas as pd
import numpy as np
import matplotlib as plt

pd.set_option('display.max_columns', 500)
df = pd.read_csv('sample.csv', nrows=1)
# print(df)

for i in df.columns:
    df[i] = False

if (gender == 'f'):
    df['gender_cd_F'] = True
else:
    df['gender_cd_M'] = True

if (has_car == 'y'):
    df['car_own_flg_Y'] = True
    if (foreign_car == 'y'):
        df['car_type_flg_Y'] = True
    else:
        df['car_type_flg_N'] = True
else:
    df['car_own_flg_N'] = True
    df['car_type_flg_N'] = True

if (has_passport == 'y'):
    df['Air_flg_Y'] = True
else:
    df['Air_flg_N'] = True

df['age' + age_range] = True

df['appl_rej_cnt_' + credit_denials] = True

if (working_experience == 'y'):
    df['good_work_flg_1'] = True
else:
    df['good_work_flg_0'] = True

if (scaled_credit_rating <= -3.5):
    df['Score_bki_3.5'] = True
elif (scaled_credit_rating <= -3):
    df['Score_bki_3.5_3'] = True
elif (scaled_credit_rating <= -2.5):
    df['Score_bki_3_2.5'] = True
elif (scaled_credit_rating <= -2):
    df['Score_bki_2.5_2'] = True
elif (scaled_credit_rating <= -1.5):
    df['Score_bki_2_1.5'] = True
elif (scaled_credit_rating <= -1):
    df['Score_bki_1.5_1'] = True
elif (scaled_credit_rating <= -0.5):
    df['Score_bki_1_0.5'] = True
elif (scaled_credit_rating <= 0):
    df['Score_bki_0.5'] = True

if (income == 'a'):
    df['income_to_6*10^4'] = True
elif (income == 'b'):
    df['income_from_6*10^4_to_10^5'] = True
elif (income == 'c'):
    df['income_from_10^5_to_2*10^5'] = True
elif (income == 'd'):
    df['income_from_2*10^5'] = True

df['out_request_cnt_' + bki_request] = True

df['first_time_cd_' + first_loan] = True

df[education_level] = True
# print(df.columns)
# print(df)
import joblib

df.drop(columns=['Unnamed: 0', 'default_flg'], inplace=True)

model = joblib.load('predict_model')
a = model.predict_proba(df)[0][0]
print("Вероятность вашего возврата:", a)

# a-prediction
# по теории вероятности я должен выдать под 1-a/a где а вероятность возврата
# но есть безрисковая ставка 15%
print("Ваша ставка:", 15 + ((1 - a) / a) * 100)
