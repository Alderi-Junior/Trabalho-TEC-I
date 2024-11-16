Análise do Histórico de Preços do Bitcoin
Este projeto utiliza dados históricos de preços do Bitcoin para realizar uma análise de dados, aplicando técnicas de mineração de dados como visualizações, correlação entre variáveis e regressão linear para prever o preço de fechamento do Bitcoin. O projeto foi desenvolvido utilizando Python e bibliotecas como pandas, matplotlib, seaborn e scikit-learn.

Estrutura do Projeto
main.py: Código principal onde os dados são carregados, processados e analisados. Gera gráficos e realiza regressões.
BitcoinHistoricalData.csv: Conjunto de dados contendo o histórico de preços do Bitcoin (arquivo CSV).
Gráficos gerados:
Evolução do preço de fechamento do Bitcoin ao longo do tempo.
Mapa de correlação entre as variáveis.
Gráfico de valores reais versus valores previstos do preço de fechamento.
Importância das variáveis preditivas na regressão.
Requisitos
Para executar este projeto, você precisará das seguintes bibliotecas:

pandas (para manipulação de dados)
matplotlib (para visualização de dados)
seaborn (para visualizações avançadas)
scikit-learn (para modelagem preditiva)
Instalação
Primeiro, crie um ambiente virtual para o projeto e instale as dependências:

bash
Copiar código
# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Windows
.venv\Scripts\activate
# No Linux/macOS
source .venv/bin/activate

# Instale as bibliotecas
pip install pandas matplotlib seaborn scikit-learn
Como Reproduzir a Análise
Siga os passos abaixo para reproduzir a análise:

Faça o download dos dados:

O arquivo esta disponivel neste repositório: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data

Abra o terminal ou prompt de comando e execute o script main.py:
bash
Copiar código
python main.py
Verifique os gráficos gerados:

Após a execução do script, os gráficos serão salvos no diretório atual do projeto. Os gráficos gerados são:
bitcoin_close_price_evolution.png: Gráfico da evolução do preço de fechamento do Bitcoin.
bitcoin_correlation_map.png: Mapa de correlação entre as variáveis.
real_vs_predicted_close_price.png: Gráfico de comparação entre valores reais e previstos do preço de fechamento.
predictor_variable_importance.png: Gráfico mostrando a importância das variáveis preditivas no modelo de regressão.
Interprete os resultados:

Visualização da Evolução do Preço: Um gráfico é gerado para mostrar como o preço de fechamento do Bitcoin variou ao longo do tempo.

Correlação entre Variáveis: Um mapa de calor é gerado para mostrar a correlação entre as variáveis como preço de abertura, preço mais alto, preço mais baixo, volume de transações e preço de fechamento.

Modelo de Regressão Linear: Um modelo de regressão linear é treinado para prever o preço de fechamento do Bitcoin com base em variáveis preditivas como preço de abertura, preço mais alto, preço mais baixo e volume de transações. O modelo é avaliado utilizando métricas como MSE e R².

Gráficos de Resultados:

Gráfico de valores reais vs. previstos para comparar o desempenho do modelo de regressão.
Gráfico de importância das variáveis para visualizar a contribuição de cada variável preditora.
