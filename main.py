import streamlit as st
from var1 import do_var1
from Var5 import do_var5
from var8 import do_var8
from var10 import do_var10
from Var18 import do_var18

st.title('Практическое занятие №11')
st.image('titanic.jpg')
st.success('Команда №2')

choice = st.selectbox('Вариант номер:', [
    'вариант 1', 'вариант 5', 'вариант 8',
    'вариант 10', 'вариант 15', 'вариант 18'
])

if choice == 'вариант 1':
    st.subheader('Выполнила работу: Аристархова Е.В.', divider='rainbow')
    st.info('Найти диапазон возрастов (min и max) пассажиров, '
            'указав пол и спасен/погиб.')
    do_var1()
elif choice == 'вариант 5':
    st.subheader('Выполнила работу: Гаврилова Ю.А.', divider='rainbow')
    st.info('Вычислить долю выживших среди мужчин и женщин, '
            'выбрав количество братьев, сестер.')
    do_var5()
elif choice == 'вариант 8':
    st.subheader('Выполнила работу: Калачева В.В.', divider='rainbow')
    st.info('Найти количество пассажиров каждого пола '
            'по указанному классу обслуживания.')
    do_var8()
elif choice == 'вариант 10':
    st.subheader('Выполнил работу: Лядов О.А.', divider='rainbow')
    st.info('Найти для мужчин и женщин (отдельно) минимальную, '
            'максимальную или среднюю цену билета.')
    do_var10()
elif choice == 'вариант 15':
    st.subheader('Проект находится в стадии разработки: Фомин А.В.', divider='rainbow')
    st.info('Подсчитать количество выживших мужчин по каждому классу '
            'обслуживания, указав диапазон возрастов.')
    st.image('din.jpeg')
elif choice == 'вариант 18':
    st.subheader('Выполнила работу: Ярмошина О.Н.', divider='rainbow')
    st.info('Посчитать долю выживших по каждому пункту посадки указав максимальный возраст.')
    do_var18()
else:
    st.error('Выбран недопустимый вариант. Пожалуйста, выберите один из предложенных вариантов.')
