import matplotlib.pyplot as plt
import streamlit as st


def get_pass_count(lines, choice):
    res = {'Мужчин': 0, 'Женщин': 0}
    class_map = {'Всего': ['1', '2', '3'], '1 класс': ['1'], '2 класс': ['2'], '3 класс': ['3']}
    if choice in class_map:
        for line in lines:
            data = line.strip().split(',')
            if len(data) < 6 or data[5] not in ['male', 'female']:
                continue
            sex, pclass = data[5], data[2]
            if pclass in class_map[choice]:
                if sex == 'male':
                    res['Мужчин'] += 1
                elif sex == 'female':
                    res['Женщин'] += 1

    return res


def do_var8():
    st.title('Вариант 8')
    st.subheader('Данные пассажиров Титаника')
    st.write("Для просмотра данных по количеству пассажиров каждого пола "
             "по указанному классу обслуживания, выберите соответствующий "
             "пункт из списка")
    choice = st.selectbox("Укажите класс обслуживания:",
                          ["Всего", "1 класс", "2 класс", "3 класс"])

    with open('data.csv') as file:
        lines = file.readlines()
    res = get_pass_count(lines, choice)

    st.dataframe(res)
    fig = plt.figure(figsize=(10, 5))
    plt.bar(list(res.keys()), list(res.values()))
    st.pyplot(fig)


do_var8()
