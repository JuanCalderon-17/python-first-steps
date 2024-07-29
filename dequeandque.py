from collections import deque

cola = deque()

cola.append(" I am the first")
cola.append("I am the second")
cola.append("yo amo")
cola.append("a camy")

print(f'These are the things i got in my queue: {cola}')
print('#' * 5)
print()

while len(cola) > 0:
    next_element = cola.popleft()
    print(f'The following element is: {next_element}')
    print(f'cola de impresion {cola}')
    print('#' * 5)
