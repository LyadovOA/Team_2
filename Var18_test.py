import pytest
from main import calculate_survival_rates

# Тестовые данные
test_data_1 = [
    {'Age': '22', 'Survived': '1', 'Embarked': 'S'},
    {'Age': '28', 'Survived': '0', 'Embarked': 'C'},
    {'Age': '', 'Survived': '1', 'Embarked': 'Q'},
    {'Age': '42', 'Survived': '1', 'Embarked': 'S'},
    {'Age': '31', 'Survived': '0', 'Embarked': 'C'},
    {'Age': '25', 'Survived': '1', 'Embarked': 'C'},
]
# Тест для проверки расчета доли выживших без ограничения по возрасту
def test_1():
    assert calculate_survival_rates(test_data_1) == {'C': 33.33333333333333, 'Q': 100.0, 'S': 100.0}

# Тест для проверки расчета доли выживших с ограничением по возрасту
def test_2():
    assert calculate_survival_rates(test_data_1, max_age=30) == {'S': 100.0, 'C': 50.0, 'Q': 100.0}


# Тест для проверки обработки отсутствующего пункта посадки
def test_3():
    test_data_2 = [
        {'Age': '22', 'Survived': '1', 'Embarked': ''},
        {'Age': '28', 'Survived': '0', 'Embarked': 'C'},
    ]
    assert calculate_survival_rates(test_data_2) == {'': 100.0, 'C': 0.0}


# Тест для проверки расчета при всех выживших
def test_4():
    test_data_3 = [
        {'Age': '22', 'Survived': '1', 'Embarked': 'S'},
        {'Age': '28', 'Survived': '1', 'Embarked': 'C'},
        {'Age': '35', 'Survived': '1', 'Embarked': 'Q'},
    ]
    assert calculate_survival_rates(test_data_3) ==  {'S': 100.0, 'C': 100.0, 'Q': 100.0}
