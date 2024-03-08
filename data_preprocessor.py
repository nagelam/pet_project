import pandas as pd
class DataPreprocessor:
    def __init__(self, user_profile):
        self.profile = user_profile
        self.df = pd.read_csv('sample.csv', nrows=1)

    def process(self):
        for col in self.df.columns:
            self.df[col] = False
        if self.profile['gender'] == 'f':
            self.df['gender_cd_F'] = True
        else:
            self.df['gender_cd_M'] = True

        if self.profile['has_car'] == 'y':
            self.df['car_own_flg_Y'] = True
            if self.profile['foreign_car'] == 'y':
                self.df['car_type_flg_Y'] = True
            else:
                self.df['car_type_flg_N'] = True
        else:
            self.df['car_own_flg_N'] = True
            self.df['car_type_flg_N'] = True

        if self.profile['has_passport'] == 'y':
            self.df['Air_flg_Y'] = True
        else:
            self.df['Air_flg_N'] = True

        self.df['age' + self.profile['age_range']] = True
        self.df['appl_rej_cnt_' + self.profile['credit_denials']] = True

        if self.profile['working_experience'] == 'y':
            self.df['good_work_flg_1'] = True
        else:
            self.df['good_work_flg_0'] = True

        if self.profile['scaled_credit_rating'] <= -3.5:
            self.df['Score_bki_3.5'] = True
        elif self.profile['scaled_credit_rating'] <= -3:
            self.df['Score_bki_3.5_3'] = True
        elif self.profile['scaled_credit_rating'] <= -2.5:
            self.df['Score_bki_3_2.5'] = True
        elif self.profile['scaled_credit_rating'] <= -2:
            self.df['Score_bki_2.5_2'] = True
        elif self.profile['scaled_credit_rating'] <= -1.5:
            self.df['Score_bki_2_1.5'] = True
        elif self.profile['scaled_credit_rating'] <= -1:
            self.df['Score_bki_1.5_1'] = True
        elif self.profile['scaled_credit_rating'] <= -0.5:
            self.df['Score_bki_1_0.5'] = True
        elif self.profile['scaled_credit_rating'] <= 0:
            self.df['Score_bki_0.5'] = True
        if self.profile['income'] == 'a':
            self.df['income_to_6*10^4'] = True
        elif self.profile['income'] == 'b':
            self.df['income_from_6*10^4_to_10^5'] = True
        elif self.profile['income'] == 'c':
            self.df['income_from_10^5_to_2*10^5'] = True
        elif self.profile['income'] == 'd':
            self.df['income_from_2*10^5'] = True

        self.df['out_request_cnt_' + self.profile['bki_request']] = True
        self.df['first_time_cd_' + self.profile['first_loan']] = True
        self.df[self.profile['education_level']] = True