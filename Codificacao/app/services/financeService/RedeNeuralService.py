
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
class RedeNeuralService:

    def __init__(self):
        with open('redeNeural.sav','rb') as file:
           self.model = pickle.load(file)
        self.scaler = StandardScaler()

    def preview(self, dados):
       dados = np.asarray(dados)
       dados = dados.reshape(-1, 1)
       dados = self.scaler.fit_transform(dados)
       dados = dados.reshape(-1, 5)
       return self.model.predict(dados)