from var8 import get_pass_count


def test_1():
    lines = ["0,1,2,3,4,Age",
             "1,1,2,3,4,male",
             "2,1,2,3,4,male",
             "3,1,2,3,4,female"]
    assert get_pass_count(lines, 'Всего') == {'Мужчин': 2, 'Женщин': 1}


def test_2():
    lines = ['6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q',
             '13,0,3,"Saundercock, Mr. William Henry",male,20,0,0,A/5. 2151,8.05,,S',
             '14,0,3,"Andersson, Mr. Anders Johan",male,39,1,5,347082,31.275,,S',
             '16,1,2,"Hewlett, Mrs. (Mary D Kingcome) ",female,55,0,0,248706,16,,S']
    assert get_pass_count(lines, '3 класс') == {'Мужчин': 3, 'Женщин': 0}


def test_3():
    lines = ['92,0,3,"Andreasson, Mr. Paul Edvin",male,20,0,0,347466,7.8542,,S',
             '93,0,1,"Chaffee, Mr. Herbert Fuller",male,46,1,0,W.E.P. 5734,61.175,E31,S',
             '96,0,3,"Shorney, Mr. Charles Joseph",male,,0,0,374910,8.05,,S',
             '100,0,2,"Kantor, Mr. Sinai",male,34,1,0,244367,26,,S']
    assert get_pass_count(lines, '2 класс') == {'Мужчин': 1, 'Женщин': 0}


def test_4():
    lines = ['92,0,3,"Andreasson, Mr. Paul Edvin",male,20,0,0,347466,7.8542,,S',
             '93,0,1,"Chaffee, Mr. Herbert Fuller",male,46,1,0,W.E.P. 5734,61.175,E31,S',
             '96,0,3,"Shorney, Mr. Charles Joseph",male,,0,0,374910,8.05,,S',
             '100,0,2,"Kantor, Mr. Sinai",male,34,1,0,244367,26,,S']
    assert get_pass_count(lines, '1 класс') == {'Мужчин': 1, 'Женщин': 0}


def test_5():
    lines = ['0,1,2,3,4,Age',
             '1,1,2,3,4,male',
             '2,1,2,3,4,жен',
             '3,1,2,3,4,муж']
    assert get_pass_count(lines, 'Всего') == {'Мужчин': 1, 'Женщин': 2}
