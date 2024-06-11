from var10 import get_group_func


# Тест для проверки корректного подсчета средней цены для мужчин и женщин
def test_avg_fares():
    lines = [
        ",,,,,male,,,,,7.25,,",
        ",,,,,male,,,,,21.075,,",
        ",,,,,female,,,,,71.2833,,",
        ",,,,,female,,,,,7.925,,"
    ]
    assert get_group_func(lines, 'avg') == (14.1625, 39.60415)


# Тест для проверки корректного подсчета максимальной цены для мужчин и женщин
def test_max_fares():
    lines = [
        ",,,,,male,,,,,7.25,,",
        ",,,,,male,,,,,21.075,,",
        ",,,,,female,,,,,71.2833,,",
        ",,,,,female,,,,,7.925,,"
    ]
    assert get_group_func(lines, 'max') == (21.075, 71.2833)


# Тест для проверки корректного подсчета минимальной цены для мужчин и женщин
def test_min_fares():
    lines = [
        ",,,,,male,,,,,7.25,,",
        ",,,,,male,,,,,3.15,,",
        ",,,,,female,,,,,71.2833,,",
        ",,,,,female,,,,,7.925,,"
    ]
    assert get_group_func(lines, 'min') == (3.15, 7.925)


# Тест для данных с отсутствием информации о ценах билетов для мужчин
def test_no_fares():
    lines = [
        ",,,,,male,,,,,,,",
        ",,,,,female,,,,,71.2833,,",
        ",,,,,female,,,,,7.925,,"
    ]
    assert get_group_func(lines, 'min') == (0, 7.925)


# Тест с полным отсутствием информации
def test_no_data():
    lines = []
    assert get_group_func(lines, 'avg') == (0, 0)
