import pytest
from hola import Suma

def test_calcular_suma():
    caso1 = Suma(5, 10)
    assert caso1.calcular_suma() == 15

    caso2 = Suma(-1, 1)
    assert caso2.calcular_suma() == 0

    caso3 = Suma(-5, -10)
    assert caso3.calcular_suma() == -15

    caso4 = Suma(0, 0)
    assert caso4.calcular_suma() == 0

    caso5 = Suma(2.5, 3.5)
    assert caso5.calcular_suma() == 6.0
