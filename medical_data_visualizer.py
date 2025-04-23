import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Importar os dados do arquivo medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Adicionar coluna overweight
# BMI = peso (kg) / (altura (m))^2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalizar dados de colesterol e gluc (0 = bom, 1 = ruim)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    """
    Gera e retorna o gráfico categórico (catplot) para as variáveis
    cholesterol, gluc, smoke, alco, active e overweight, segmentadas por
    cardio.
    """
    # 4. Criar DataFrame para o catplot usando pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    # 5. Agrupar e formatar os dados para o catplot
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # 6. Criar gráfico com sns.catplot
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )
    fig = g.fig
    return fig

def draw_heat_map():
    """
    Gera e retorna o heatmap da matriz de correlação dos dados médicos
    filtrados.
    """
    # 8. Limpar os dados conforme critérios especificados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    # 9. Calcular matriz de correlação
    corr = df_heat.corr()
    # 10. Gerar máscara para triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # 11. Configurar figura matplotlib
    fig, ax = plt.subplots(figsize=(12, 10))
    # 12. Plotar heatmap com sns.heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5}
    )
    return fig 