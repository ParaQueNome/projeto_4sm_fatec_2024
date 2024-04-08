import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# Defina sua chave de API da Polygon.io
api_key = '4U16LvuqPJUR1B8gFpAASREdkEqhdVoH'

# Função para obter dados históricos de preços de fechamento de uma ação específica
def obter_dados_historicos(symbol):
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/2000-01-01/2023-12-31?apiKey={api_key}'
    response = requests.get(url)
    data = response.json()['results']
    df = pd.DataFrame(data)
    df['t'] = pd.to_datetime(df['t'], unit='ms')  # Converter timestamp para datetime
    df.set_index('t', inplace=True)
    return df

# Função para obter dados históricos de preços de fechamento de todos os ativos disponíveis
def obter_dados_historicos_para_todos_ativos(symbols):
    dfs = []
    for symbol in symbols:
        df = obter_dados_historicos(symbol)
        dfs.append(df)
    return pd.concat(dfs)

# Obter lista de símbolos de ações (substitua 'AAPL' por uma lista de símbolos de ações que você deseja)
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA',]  # Exemplo com algumas ações, você pode adicionar mais símbolos conforme necessário

# Obter dados históricos de preços de fechamento de todos os ativos disponíveis
df = obter_dados_historicos_para_todos_ativos(symbols)

# Selecionar os preços de fechamento, abertura, volume, high e low como recursos (features)
X = df[['c', 'o', 'h', 'l', 'v']].values[:-1]  # Preços de fechamento, abertura, high, low e volume exceto o último dia

# Selecionar o preço de fechamento do próximo dia como alvo (target)
y = df['c'].values[1:]  # Preços de fechamento deslocados em 1 dia para frente

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Redimensionar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar o modelo de regressão em redes neurais
model = MLPRegressor(hidden_layer_sizes=(100, 50, 100,100,100,100,100,100,100), activation='relu', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Avaliar o modelo
train_score = model.score(X_train_scaled, y_train)
test_score = model.score(X_test_scaled, y_test)
print(f'Acurácia do modelo no conjunto de treinamento: {train_score}')
print(f'Acurácia do modelo no conjunto de teste: {test_score}')

# Calcular o erro médio quadrático
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f'Erro médio quadrático (MSE): {mse}')

import pickle
pickle.dump(model, open('redeNeural.sav','wb'))
