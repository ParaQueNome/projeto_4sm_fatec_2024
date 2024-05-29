
import pickle

class RedeNeuralService:

    def __init__(self):
        with open('redeNeural.sav','rb') as file:
           self.model = pickle.load(file)

    def preview(self, dados):
       
       return self.model.predict(dados)