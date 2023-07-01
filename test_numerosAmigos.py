import pytest
from numerosAmigos import numeros_amigos

def test_numerosamigo():
    assert numeros_amigos(17296,18416) == "17296 y 18416 son amigos"
    print("Esta bien")
    
def test_numerosamigo2():
    assert numeros_amigos(12285,14595) == '12285 y 14595 son amigos'
    print("Esta bien")

def test_numerosamigo3():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")

def test_numerosamigo4():
    assert numeros_amigos(2984,8550) == '2984 y 8550 no son amigos'
    print("Esta bien")
    
def test_numerosamigo5():
    assert numeros_amigos(700,800) == '700 y 800 no son amigos'
    print("Esta bien")

def test_numerosamigo6():
    assert numeros_amigos(4,4) == '4 y 4 son amigos'
    print("Esta bien")

def test_numerosamigo7():
    assert numeros_amigos(514,123) == '514 y 123 son amigos'
    print("Esta bien")

def test_numerosamigo8():
    assert numeros_amigos(32,1352) == '32 y 1352 son amigos'
    print("Esta bien")
    
def test_numerosamigo9():
    assert numeros_amigos(445,8124) == '445 y 8124 son amigos'
    print("Esta bien")
    
def test_numerosamigo10():
    assert numeros_amigos(124,9) == '124 y 9  son amigos'
    print("Esta bien")

if __name__ == '__main__':
    test_numerosamigo()
    test_numerosamigo2()
    test_numerosamigo3()
    test_numerosamigo4()
    test_numerosamigo5()
    test_numerosamigo6()  
    test_numerosamigo7()
    test_numerosamigo8()
    test_numerosamigo9()  
    test_numerosamigo10()      