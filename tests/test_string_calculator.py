from src.string_calculator import StringCalculator
import pytest

def test_add_param_vide_return_zero():
    # Arrange
    mon_param = ""
    mon_resultat = 0
    # Act
    somme = StringCalculator.Add(mon_param)
    # Assert
    assert somme == mon_resultat

def test_add_param_return_param():
    # Arrange
    mon_param = "5"
    mon_resultat = 5
    # Act
    somme = StringCalculator.Add(mon_param)
    # Assert
    assert somme == mon_resultat


@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("1;2;3", 6), # test case 4
    ("1;2;3;4", 10), # test case 5
    ("1;2;5", 8), # test case 6
    ("1;2;0", 3), # test case 7
    ("1;2;1000", 1003), # test case 8
    ("1;2;1001", 3), # test case 9
])

def test_add_plusieurs_nombres(mon_param, mon_resultat):
    # Act
    somme = StringCalculator.Add(mon_param)
    # Assert
    assert somme == mon_resultat

# test que la multiplication de "5;5" == 25
def test_multiply_5_5_return_25():
    # Arrange
    mon_param = "5;5"
    mon_resultat = 25
    # Act
    produit = StringCalculator.Multiply(mon_param)
    # Assert
    assert produit == mon_resultat

# test que la multiplication de "5;3;2" == 30
    
    
# test que la multiplication de "4" == 4