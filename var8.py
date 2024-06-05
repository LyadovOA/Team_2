# найти количество отдельно мужчин отдельно женщин по каждому классу обслуживания
import matplotlib.pyplot as plt
import streamlit as st

def get_pass_count(lines, choise):
    res = {'Мужчин': 0, 'Женщин': 0}
    for line in lines:
        d = line.split(',')
        Sex = d[5]
        Pclass = d[2]
        if choise == "Всего":
            if Sex in {'Мужчин', 'Женщин'}:
                res[Sex] += 1
            if Sex == 'Age':
                continue
            if Sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choise == "1 класс" and Pclass == '1':
            if Sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choise == "2 класс" and Pclass == '2':
            if Sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
        elif choise == "3 класс" and Pclass == '3':
            if Sex == 'male':
                res['Мужчин'] += 1
            else:
                res['Женщин'] += 1
    return res

def do_var8():
    st.title('Вариант 8')

    st.header('Данные пассажиров Титаника')
    st.write("Для просмотра данных по количеству пассажиров каждого пола по указанному классу обслуживания, выберите соответствующий пункт из списка")
    choise = st.selectbox("Укажите класс обслуживания:", ["Всего", "1 класс", "2 класс", "3 класс"])

    with open('data.csv') as file:
        lines = file.readlines()
        # Вызываем функцию get_pass_count с передачей аргумента choise
        res = get_pass_count(lines, choise)

    st.dataframe(res)
    fig = plt.figure(figsize=(10,5))
    plt.bar(['Мужчин','Женщин'],[res['Мужчин'],res['Женщин']])
    st.pyplot(fig)

do_var8()