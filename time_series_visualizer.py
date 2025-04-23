import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importar os dados do arquivo fcc-forum-pageviews.csv
#    e definir o índice como data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Limpar os dados removendo os top/bottom 2.5%
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.975)
df_clean = df[(df['value'] >= low) & (df['value'] <= high)]

def draw_line_plot():
    """
    Gera e retorna um gráfico de linha dos page views diários.
    Título: Daily freeCodeCamp Forum Page Views 5/2016-12/2019
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_clean.index, df_clean['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    return fig


def draw_bar_plot():
    """
    Gera e retorna um gráfico de barras mostrando a média de page views
    por mês agrupado por ano.
    """
    # Preparar dados
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    # Ordenar meses
    months_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_grouped = df_grouped.reindex(columns=months_order)
    # Plot
    fig = df_grouped.plot(kind='bar', figsize=(12, 8)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    return fig


def draw_box_plot():
    """
    Gera e retorna dois box plots: um por ano (trend) e outro por mês
    (seasonality).
    """
    df_box = df_clean.copy().reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    return fig 