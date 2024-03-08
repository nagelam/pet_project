import joblib
class Predictor:
    def __init__(self, dataframe):
        self.df = dataframe

    def predict(self):
        self.df.drop(columns=['Unnamed: 0','default_flg'], inplace=True)
        model = joblib.load('predict_model')  # Предполагается, что модель сохранена в файле predict_model.joblib
        prediction = model.predict_proba(self.df)[0][0]
        return prediction