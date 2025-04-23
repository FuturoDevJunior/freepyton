import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Importar os dados do arquivo epa-sea-level.csv
df = pd.read_csv('epa-sea-level.csv')


def draw_plot():
    """
    Gera e retorna um gráfico de dispersão dos dados de nível do mar,
    incluindo duas linhas de regressão linear (todas as datas e desde 2000).
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    # Scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', color='blue')
    # Linha de regressão para todo o período
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res_all.intercept + res_all.slope * x_pred
    ax.plot(x_pred, y_pred, 'r', label='Best fit: 1880-2050')
    # Linha de regressão para dados desde 2000
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res_2000.intercept + res_2000.slope * x_pred2
    ax.plot(x_pred2, y_pred2, 'green', label='Best fit: 2000-2050')
    # Labels e título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    return fig 