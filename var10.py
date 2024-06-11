import matplotlib.pyplot as plt
import streamlit as st


def get_group_func(lines, choice):
    male_fares = []
    female_fares = []

    for line in lines:
        data = line.strip().split(',')
        sex = data[5]
        fare_str = data[10].strip()
        if fare_str:
            fare = float(fare_str)
            if sex == 'male':
                male_fares.append(fare)
            elif sex == 'female':
                female_fares.append(fare)

    statistics = {
        'avg': (sum(male_fares) / len(male_fares) if male_fares else 0,
                sum(female_fares) / len(female_fares) if female_fares else 0),
        'min': (min(male_fares) if male_fares else 0,
                min(female_fares) if female_fares else 0),
        'max': (max(male_fares) if male_fares else 0,
                max(female_fares) if female_fares else 0)
    }

    return statistics[choice]


with open("data.csv") as file:
    next(file)
    lines = file.readlines()


def do_var10():
    st.subheader('Данные пассажиров Титаника')
    st.write("Для просмотра данных о стоимости билетов, выберите пункт из списка.")
    selected = st.selectbox(
        'Выберите тип стоимости',
        ['Средняя цена', 'Максимальная цена', 'Минимальная цена']
    )

    fare_types = {'Средняя цена': 'avg', 'Максимальная цена': 'max', 'Минимальная цена': 'min'}
    selected_fare_type = fare_types[selected]
    fares = get_group_func(lines, selected_fare_type)

    male_fare, female_fare = fares
    sex = ['Мужчины', 'Женщины']
    data = {'Пол': sex, 'Цена': [male_fare, female_fare]}
    st.dataframe(data)

    fig = plt.figure(figsize=(10, 5))
    plt.bar(sex, [male_fare, female_fare], color=['blue', 'pink'])
    plt.xlabel('Пол')
    plt.ylabel('Цена')
    plt.title(f'{selected} стоимости билетов')
    st.pyplot(fig)


do_var10()
