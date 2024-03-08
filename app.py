from user import UserProfiler
from data_preprocessor import DataPreprocessor
from predictor import Predictor

class Application:
    def run(self):
        user_profiler = UserProfiler()
        preprocessor = DataPreprocessor(user_profiler.profile)
        preprocessor.process()
        predictor = Predictor(preprocessor.df)
        prediction = predictor.predict()
        print(f"Вероятность вашего возврата: {prediction}")

        # Расчет и вывод вашей ставки
        df = preprocessor.df.copy()  # Создадим копию DataFrame для безопасности


        a = prediction  # Используем значение предсказания, полученное ранее
        rate = 15 + ((1 - a) / a) * 100  # Исправлено использование оператора деления
        print(f"Ваша ставка: {rate}")

if __name__ == "__main__":
    app = Application()
    app.run()
