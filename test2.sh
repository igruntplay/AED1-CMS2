#!/bin/bash

echo "Running Fibonacci tests..."

output=$(echo 10 | python3 ej2-fibonacci.py)
if [ "$output" -ne "55" ]; then
  echo "Test 1 failed, expected output 55, but got $output"
fi

output=$(echo 20 | python3 ej2-fibonacci.py)
if [ "$output" -ne "6765" ]; then
  echo "Test 2 failed, expected output 6765, but got $output"
fi

output=$(echo 0 | python3 ej2-fibonacci.py)
if [ "$output" -ne "0" ]; then
  echo "Test 3 failed, expected output 0, but got $output"
fi

output=$(echo 1 | python3 ej2-fibonacci.py)
if [ "$output" -ne "1" ]; then
  echo "Test 4 failed, expected output 1, but got $output"
fi

echo "All tests passed!"
