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
@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("5;5", 25), #test case 1
])    

def test_multiply_5_5_return_25(mon_param, mon_resultat):
    # Act
    product = StringCalculator.Multiply(mon_param)
    # Assert
    assert product == mon_resultat

# test que la multiplication de "4" == 4
@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("4", 4), #test case 1
])     

def test_multiply_4_return_4(mon_param, mon_resultat):
    # Act
    product = StringCalculator.Multiply(mon_param)
    # Assert
    assert product == mon_resultat

# test que la multiplication de "5;3;2" == 30
@pytest.mark.parametrize("mon_param, mon_resultat", [
    ("5;3;2", 30), #test case 1
    ("2;2;2", 8), #test case 2
    ("2;4;5;2", 80), #test case 3
])         
    
def test_multiply_5_3_2_return_30(mon_param, mon_resultat):
    # Act
    product = StringCalculator.Multiply(mon_param)
    # Assert
    assert product == mon_resultat
    
# test qu'avec 5;a;3 il retourne une erreur
@pytest.mark.parametrize("mon_param", [
    ("5;a;2"), #test case 1
    ("b;2;2"), #test case 2
    ("2;4;c;2"), #test case 3
])      
    
def test_multiply_avec_lettre_return_erreur(mon_param):
    # Act
    with pytest.raises(ValueError, match="Invalid input:"):
    # Assert
        StringCalculator.Multiply(mon_param)

#test qu'avec des nombre a virgule ça marche
def test_multiply_de_nombre_decimaux():
    # Arrange
    mon_param = "1.5;2"
    mon_resultat = 3
    # Act
    product = StringCalculator.Multiply(mon_param)
    # Assert
    assert product == mon_resultat
