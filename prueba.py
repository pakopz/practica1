import pytest
from suma import Suma

def test_suma_positivos():
    suma = Suma(3, 5)
    assert suma.calcular_suma() == 8

def test_suma_negativos():
    suma = Suma(-2, -3)
    assert suma.calcular_suma() == -5

def test_suma_con_cero():
    suma = Suma(0, 0)
    assert suma.calcular_suma() == 0

def test_suma_no_numerica():
    with pytest.raises(TypeError):
        suma = Suma("a", "b")
        suma.calcular_suma()
