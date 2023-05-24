#!/bin/bash

# Definir función de prueba
test_meseta_mas_larga() {
    input=$1
    expected=$2

    result=$(python3 mesetaMasLarga.py <<< "$input")
    
    if [ "$result" == "$expected" ]; then
        echo "PASSED: Input: $input - Expected: $expected - Result: $result"
    else
        echo "FAILED: Input: $input - Expected: $expected - Result: $result"
    fi
}
# Ejecutar pruebas
test_meseta_mas_larga "1 1 1 3 3 3 3 4 4 4 4 4" "5"
test_meseta_mas_larga "1 1 2 2 2 3 3 3 3" "4"
test_meseta_mas_larga "1 1 1 2 2 2 2 3 3" "4"
test_meseta_mas_larga "1 1 1 1 2 2 2 2 2" "5"
test_meseta_mas_larga "1 1 1 1 1" "5"
test_meseta_mas_larga "1 2 3 4 5" "1"
test_meseta_mas_larga "1 1 1 2 3 4 5" "3"
test_meseta_mas_larga "1 1 2 3 4 4 4" "3"
test_meseta_mas_larga "1" "1"
test_meseta_mas_larga "" "0"
