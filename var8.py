import matplotlib.pyplot as plt
import streamlit as st


def get_pass_count(lines, choice):
    res = {'Мужчин': 0, 'Женщин': 0}
    for line in lines:
        d = line.split(',')
        sex = d[5]
        pclass = d[2]
        if choice == "Всего":
            if sex in {'Мужчин', 'Женщин'}:
                res[sex] += 1
            if sex == 'Age':
                continue
            if sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choice == "1 класс" and pclass == '1':
            if sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choice == "2 класс" and pclass == '2':
            if sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choice == "3 класс" and pclass == '3':
            if sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
    return res


def do_var8():
    st.title('Вариант 8')
    st.header('Данные пассажиров Титаника')
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
