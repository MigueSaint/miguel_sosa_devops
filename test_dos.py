from app import saludar

def test_saludo_falla():
    assert saludar("Mundo") == "Hola Mundo"  # Falla porque falta la coma
