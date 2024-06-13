import matplotlib.pyplot as plt
import streamlit as st

def get_survived_pass(lines):
    all_men_0 = 0
    all_women_0 = 0
    survived_men_0 = 0
    survived_women_0 = 0
    all_men_1 = 0
    all_women_1 = 0
    survived_men_1 = 0
    survived_women_1 = 0
    all_men_3 = 0
    all_women_3 = 0
    survived_men_3 = 0
    survived_women_3 = 0
    for line in lines:
        data = line.split(',')
        if data[5] not in ['male', 'female'] or data[7] == '':
            continue
        elif data[5] == 'male' and data[7] == '0':
            all_men_0 += 1
            if data[1] == '1':
                survived_men_0 += 1
        elif data[5] == 'female' and data[7] == '0':
            all_women_0 += 1
            if data[1] == '1':
                survived_women_0 += 1
        elif data[5] == 'male' and (data[7] == '1' or data[7] == '2'):
            all_men_1 += 1
            if data[1] == '1':
                survived_men_1 += 1
        elif data[5] == 'female' and (data[7] == '1' or data[7] == '2'):
            all_women_1 += 1
            if data[1] == '1':
                survived_women_1 += 1
        elif data[5] == 'male' and int(data[7]) > 2:
            all_men_3 += 1
            if data[1] == '1':
                survived_men_3 += 1
        elif data[5] == 'female' and int(data[7]) > 2:
            all_women_3 += 1
            if data[1] == '1':
                survived_women_3 += 1
    return all_men_0, survived_men_0, all_women_0, survived_women_0, all_men_1, survived_men_1, all_women_1, survived_women_1, all_men_3, survived_men_3, all_women_3, survived_women_3

with open("data.csv", 'r') as file:
    lines = file.readlines()
all_men_0, survived_men_0, all_women_0, survived_women_0, all_men_1, survived_men_1, all_women_1, survived_women_1, all_men_3, survived_men_3, all_women_3, survived_women_3 = get_survived_pass(lines)



def do_var5():
    st.subheader('Доля выживших пассажиров Титаника')
    st.write('Чтобы узнать долю выживших определенного пола, выберите количество братьев или сестер у пассажира')
    choice = st.selectbox('Выберите количество братьев или сестер у выжившего пассажира:', ['0', '1-2', 'больше 2'])

    if choice == '0':
        x = ['мужчины', 'женщины']
        y = [f'{survived_men_0 / all_men_0 * 100:.2f}%', f'{survived_women_0 / all_women_0 * 100:.2f}%']
        tab = {'Пол пассажира': x, 'Доля выживших пассажиров': y}
        st.dataframe(tab)
        fig = plt.figure(figsize=(8, 3))
        plt.bar(x, [int(survived_men_0 / all_men_0 * 100)
                    if all_men_0 > 0 else 0,
                    int(survived_women_0 / all_women_0 * 100)
                    if all_women_0 > 0 else 0
                    ],
                color='brown')
        plt.xlabel('Пол пассажира')
        plt.ylabel('Доля выживших пассажиров, %')
        plt.title('Доля выживших пассажиров')
        st.pyplot(fig)

    elif choice == '1-2':
        x = ['мужчины', 'женщины']
        y = [f'{survived_men_1 / all_men_1 * 100:.2f}%', f'{survived_women_1 / all_women_1 * 100:.2f}%']
        tab = {'Пол пассажира': x, 'Доля выживших пассажиров': y}
        st.dataframe(tab)
        fig = plt.figure(figsize=(8, 3))
        plt.bar(x, [int(survived_men_1 / all_men_1 * 100)
                    if all_men_1 > 0 else 0,
                    int(survived_women_1 / all_women_1 * 100)
                    if all_women_1 > 0 else 0
                    ],
                color='brown')
        plt.xlabel('Пол пассажира')
        plt.ylabel('Доля выживших пассажиров, %')
        plt.title('Доля выживших пассажиров')
        st.pyplot(fig)

    elif choice == 'больше 2':
        x = ['мужчины', 'женщины']
        y = [f'{survived_men_3 / all_men_3 * 100:.2f}%', f'{survived_women_3 / all_women_3 * 100:.2f}%']
        tab = {'Пол пассажира': x, 'Доля выживших пассажиров': y}
        st.dataframe(tab)
        fig = plt.figure(figsize=(8, 3))
        plt.bar(x, [int(survived_men_3 / all_men_3 * 100)
                    if all_men_3 > 0 else 0,
                    int(survived_women_3 / all_women_3 * 100)
                    if all_women_3 > 0 else 0
                    ],
                color='brown')
        plt.xlabel('Пол пассажира')
        plt.ylabel('Доля выживших пассажиров, %')
        plt.title('Доля выживших пассажиров')
        st.pyplot(fig)


do_var5()
