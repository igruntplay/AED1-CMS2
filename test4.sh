#!/bin/bash

# Definir función de prueba
test_filas_parecidas() {
    filas=$1
    columnas=$2
    matriz=$3
    expected=$4

    result=$(echo -e "$filas\n$columnas\n$matriz" | python3 filasParecidas.py)
    
    if [ "$result" == "$expected" ]; then
        echo "PASSED: Input: $matriz - Expected: $expected - Result: $result"
    else
        echo "FAILED: Input: $matriz - Expected: $expected - Result: $result"
    fi
}

# Ejecutar pruebas
test_filas_parecidas "2" "2" "1 2\n2 3" "True"
test_filas_parecidas "2" "2" "1 2\n3 4" "False"
test_filas_parecidas "3" "3" "1 2 3\n2 3 4\n3 4 5" "True"
test_filas_parecidas "3" "3" "1 2 3\n4 5 6\n7 8 9" "False"
