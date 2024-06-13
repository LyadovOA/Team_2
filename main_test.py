import pytest
from main import get_survived_pass


# Тестирование на корректность подсчета количества женщин, у которых не было братьев или сестер
def test_get_count_number_women_0():
    lines = [
        ",1,,,,female,,1,,,,,",
        ",1,,,,female,,1,,,,,",
        ",1,,,,female,,0,,,,,"
    ]
    number_men_0, survived_men_0, number_women_0, survived_women_0, number_men_1, survived_men_1, number_women_1, survived_women_1, number_men_3, survived_men_3, number_women_3, survived_women_3 = get_survived_pass(lines)
    assert number_women_0 == 1


# Тестирование на корректность подсчета при наличии пропусков
def test_count_with_pass():
    lines = [
        ",0,,,,male,,1,,,,,",
        ",0,,,,male,,3,,,,,",
        ",0,,,,male,,,,,,,",
        ",1,,,,male,,1,,,,,"
    ]
    number_men_0, survived_men_0, number_women_0, survived_women_0, number_men_1, survived_men_1, number_women_1, survived_women_1, number_men_3, survived_men_3, number_women_3, survived_women_3 = get_survived_pass(lines)
    assert survived_men_1 == 1


# Тестирование на корректность подсчета при отсутствии значений, удовлетворяющих заданным параметрам
def test_get_count_not_variants():
    lines = [
        ",0,,,,male,,0,,,,,",
        ",0,,,,male,,0,,,,,",
        ",0,,,,male,,0,,,,,"
    ]
    number_men_0, survived_men_0, number_women_0, survived_women_0, number_men_1, survived_men_1, number_women_1, survived_women_1, number_men_3, survived_men_3, number_women_3, survived_women_3 = get_survived_pass(lines)
    assert survived_women_3 == 0


# Тестирование на корректность подсчета при наличии удовлетворяющих позиций при ошибке пола
def test_get_count_sex_mistake():
    lines = [
        ",0,,,,male,,1,,,,,",
        ",1,,,,male,,4,,,,,",
        ",0,,,,female,,2,,,,,",
        ",0,,,,male,,0,,,,,",
        ",0,,,,male,,2,,,,,",
        ",0,,,,male,,5,,,,,",
        ",1,,,,fem,,3,,,,,"
    ]
    number_men_0, survived_men_0, number_women_0, survived_women_0, number_men_1, survived_men_1, number_women_1, survived_women_1, number_men_3, survived_men_3, number_women_3, survived_women_3 = get_survived_pass(lines)
    assert number_men_3 == 2
