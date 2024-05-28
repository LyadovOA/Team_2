import streamlit as st

st.header('Практическое занятие №11')
st.image('titanic.jpg')
st.header('Команда №2 ')

choice = st.selectbox('Вариант номер:',  ['вариант 1','вариант 8','вариант 10', 'вариант 18'])

from var1 import do_var1
#from var5 import do_var5
from var8 import do_var8
from var10 import do_var10
from Var18 import do_var18
#from var15 import do_var15

if choice == 'вариант 1':
    st.header('Выполнила работу: Аристархова Е.В.', divider='rainbow')
    do_var1()
#elif choice == 'вариант 5':
    #do_var5()
elif choice == 'вариант 8':
    st.header('Выполнила работу: Калачева В.В.', divider='rainbow')
    do_var8()
elif choice == 'вариант 10':
    st.header('Выполнил работу: Лядов О.А.', divider='rainbow')
    do_var10()
#elif choice == 'вариант 15':
   # do_var15()
elif choice == 'вариант 18':
    st.header('Выполнила работу: Ярмошина О.Н.', divider='rainbow')
    do_var18()
