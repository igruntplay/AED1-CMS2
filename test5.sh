#!/bin/bash

# Función de prueba que llama al script de Python con los valores de origen, destino y vuelos especificados y compara el resultado con el resultado esperado.
function run_test {
    origen=$1
    destino=$2
    vuelos=$3
    esperado=$4

    result=$(python3 sePuedeLlegar.py <<<"$origen"$'\n'"$destino"$'\n'"$vuelos")
    if [ "$result" != "$esperado" ]; then
        echo "Test falló: esperaba $esperado, obtuvo $result"
    else
        echo "Test pasó"
    fi
}

# Ejecuta varios tests.

run_test "rosario" "jujuy" "rosario,jujuy" "1" # Test 1
run_test "rosario" "jujuy" "rosario,misiones misiones,jujuy" "2" # Test 2
run_test "rosario" "jujuy" "rosario,misiones misiones,salta" "-1" # Test 3
run_test "rosario" "jujuy" "jujuy,rosario" "-1" # Test 4
run_test "rosario" "jujuy" "" "-1" # Test 5
run_test "rosario" "rosario" "rosario,rosario" "1" # Test 6
run_test "rosario" "misiones" "rosario,misiones misiones,jujuy jujuy,salta" "1" # Test 7
run_test "rosario" "jujuy" "rosario,misiones misiones,jujuy jujuy,salta" "3" # Test 8
run_test "rosario" "jujuy" "rosario,misiones misiones,jujuy jujuy,rosario" "-1" # Test 9
run_test "rosario" "jujuy" "rosario,misiones misiones,rosario" "-1" # Test 10
run_test "A" "Z" "X,Z A,B B,X" "3" # Test 11
