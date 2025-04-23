import pandas as pd


def calculate_demographic_data(print_data=True):
    """
    Analisa dados demográficos do censo de 1994 usando Pandas.
    Retorna um dicionário com as respostas para as perguntas do desafio.
    """
    # Carregar o dataset
    df = pd.read_csv(
        'adult.data.csv',
        header=None,
        names=[
            'age', 'workclass', 'fnlwgt', 'education', 'education-num',
            'marital-status', 'occupation', 'relationship', 'race', 'sex',
            'capital-gain', 'capital-loss', 'hours-per-week',
            'native-country', 'salary'
        ],
        na_values='?'
    )

    # 1. Quantidade de pessoas por raça
    race_count = df['race'].value_counts()

    # 2. Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. % de pessoas com Bacharelado
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # 4. % de pessoas com/sem educação avançada que ganham >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education
    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 6. % de pessoas que trabalham o mínimo e ganham >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 7. País com maior % de pessoas que ganham >50K
    country_counts = df['native-country'].value_counts()
    rich_country_counts = (
        df[df['salary'] == '>50K']['native-country'].value_counts()
    )
    country_rich_percent = (
        rich_country_counts / country_counts * 100
    ).dropna()
    highest_earning_country = country_rich_percent.idxmax()
    highest_earning_country_percentage = round(
        country_rich_percent.max(), 1
    )

    # 8. Ocupação mais comum entre quem ganha >50K na Índia
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')][
            'occupation'
        ]
        .value_counts()
        .idxmax()
        if not df[(df['native-country'] == 'India') & (df['salary'] == '>50K')][
            'occupation'
        ].empty
        else None
    )

    if print_data:
        print("Number of each race:", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: "
            f"{higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: "
            f"{lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: "
            f"{rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            f"Highest percentage of rich people in country: "
            f"{highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': (
            highest_earning_country_percentage
        ),
        'top_IN_occupation': top_IN_occupation
    } 