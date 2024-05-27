#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    
    fibonacci_sequence = [0]
    if length == 1:
        print(fibonacci_sequence)
        return
    
    fibonacci_sequence.append(1)
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence)
