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

    st.header('Данные пассажиров Титаника')
    st.write("Для просмотра данных о стоимости билетов, выберите пункт из списка.")
    selected = st.selectbox(
        'Выберите тип стоимости',
        ['Средняя цена', 'Максимальная цена', 'Минимальная цена']
    )

    if selected == 'Средняя цена':
        average_fare = [avg_fares['male_avg_fare'], avg_fares['female_avg_fare']]
        sex = ['Мужчины', 'Женщины']
        data = {'Пол': sex, 'Цена': average_fare}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(sex, average_fare, color=['blue', 'pink'])
        plt.xlabel('Пол')
        plt.ylabel('Цена')
        plt.title('Средняя стоимость билетов')
        st.pyplot(fig)

    elif selected == 'Максимальная цена':
        max_fare = [max_fares['male_max_fare'], max_fares['female_max_fare']]
        sex = ['Мужчины', 'Женщины']
        data = {'Пол': sex, 'Цена': max_fare}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(sex, max_fare, color=['blue', 'pink'])
        plt.xlabel('Пол')
        plt.ylabel('Цена')
        plt.title('Максимальная стоимость билетов')
        st.pyplot(fig)

    elif selected == 'Минимальная цена':
        min_fare = [min_fares['male_min_fare'], min_fares['female_min_fare']]
        sex = ['Мужчины', 'Женщины']
        data = {'Пол': sex, 'Цена': min_fare}
        st.table(data)

        fig = plt.figure(figsize=(10, 5))
        plt.bar(sex, min_fare, color=['blue', 'pink'])
        plt.xlabel('Пол')
        plt.ylabel('Цена')
        plt.title('Минимальная стоимость билетов')
        st.pyplot(fig)


do_var10()
