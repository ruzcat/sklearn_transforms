from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        #Borramos registros con datos faltantes para tener data mas certera ya que promediar cualquier valor no es buena practica
        #Registro incompletos 685 (3.35%) de la total 20499 (100%)
        data.dropna(subset=self.columns, inplace=True)       
        # Devolvemos un nuevo dataframe de 19814 Registros con datos completos sin las columnas no deseadas sin valoren nan
        return data.drop(labels=self.columns, axis='columns')
