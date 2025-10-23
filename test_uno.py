from app import saludar

def test_saludo_correcto():
    assert saludar("Miguel") == "Hola, Miguel!"
