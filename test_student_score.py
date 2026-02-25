import pytest
# Asumiendo que tu función está en un archivo llamado evaluador.py
from student_score import evaluar_estudiante

def test_regla_critica_faltas():
    # ==============================================
    # 1. Pruebas Normales
    # ==============================================
    assert evaluar_estudiante(100, 0) == "SOBRESALIENTE"
    assert evaluar_estudiante(40, 0) == "REPROBADO"

def test_limites_exactos():
    # ==============================================
    # 2. Probar los bordes de los rangos (edge cases)
    # ==============================================
    assert evaluar_estudiante(60, 0) == "APROBADO"     # 60 es el mínimo para aprobar
    assert evaluar_estudiante(85, 0) == "EXCELENTE"    # 85 es el mínimo para excelente
    assert evaluar_estudiante(90, 0) == "SOBRESALIENTE" # 90 es el mínimo para sobresaliente

def test_excepciones_validación():
    # ==============================================
    # 3. Pruebas de error
    # ==============================================
    with pytest.raises(ValueError, match="Nota fuera de rango"):
        evaluar_estudiante(-5, 0)
    
    # Verifica que lance TypeError si el tipo de dato es incorrecto
    with pytest.raises(TypeError, match="Las faltas deben ser enteras"):
        evaluar_estudiante(80, "cinco")

def test_valores_extremos():
    # ==============================================
    # 4. Pruebas valores extremos
    # ==============================================
    assert evaluar_estudiante(0, 0) == "REPROBADO"
    
    # Caso de nota máxima con el máximo de faltas permitido antes de reprobar por faltas
    # (Nota 100, 10 faltas -> resta 5 puntos -> nota 95 -> SOBRESALIENTE)
    assert evaluar_estudiante(100, 10) == "SOBRESALIENTE"

def test_regla_penalizacion_faltas():
    # Nota 60 con 4 faltas (faltas > 3):
    # Se restan 5 puntos -> Nota real: 55 -> Debe REPROBAR
    assert evaluar_estudiante(60, 4) == "REPROBADO"
    
    # Nota 90 con 4 faltas:
    # Se restan 5 puntos -> Nota real: 85 -> Debe ser EXCELENTE (no Sobresaliente)
    assert evaluar_estudiante(90, 4) == "EXCELENTE"

def test_validacion_regla_critica():
    # Aunque tenga 100 de nota, si tiene más de 10 faltas debe reprobar
    assert evaluar_estudiante(100, 11) == "REPROBADO"
    
    # El límite exacto de la regla crítica
    assert evaluar_estudiante(100, 10) != "REPROBADO" # Sigue evaluando nota