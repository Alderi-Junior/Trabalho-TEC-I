# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# carregando datset
dataset_path = "archive/btcusd_1-min_data.csv"  # Substitua pelo caminho do arquivo
df = pd.read_csv(dataset_path)


df['Date'] = pd.to_datetime(df['Timestamp'], unit='s')

# ordenando
df = df.sort_values('Date')

# graficos
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Preço de Fechamento', color='blue')
plt.title('Evolução do Preço de Fechamento do Bitcoin')
plt.xlabel('Data')
plt.ylabel('Preço (USD)')
plt.legend()
plt.grid(True)
plt.savefig("bitcoin_close_price_evolution.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df[['Open', 'High', 'Low', 'Close', 'Volume']].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de Correlação das Variáveis")
plt.savefig("bitcoin_correlation_map.png")
plt.show()


variaveis_preditoras = ['Open', 'High', 'Low', 'Volume']
variavel_alvo = 'Close'
X = df[variaveis_preditoras]
y = df[variavel_alvo]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)


print("\nErro Quadrático Médio (MSE):", mean_squared_error(y_test, y_pred))
print("Coeficiente de Determinação (R²):", r2_score(y_test, y_pred))


plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='green')
plt.title('Valores Reais vs. Previstos')
plt.xlabel('Valor Real (Close)')
plt.ylabel('Valor Previsto (Close)')
plt.grid(True)
plt.savefig("real_vs_predicted_close_price.png")  # Salvando o gráfico
plt.show()


importancia = modelo.coef_
plt.figure(figsize=(10, 6))
plt.bar(variaveis_preditoras, importancia, color='orange')
plt.title('Importância das Variáveis Preditivas')
plt.ylabel('Coeficientes')
plt.savefig("praedictor_variable_importance.png")  # Salvando o gráfico
plt.show()
