from collections import deque

# definir la pila
historial = deque()

# usar append para agregar elementos
# es el equivalente al PUSH de una cola normal
historial.append('primera acción')
historial.append('segunda acción')
historial.append('tercera acción')
historial.append('cuarta acción')

print(f'History of the stack : {historial}')
print('#' * 5)

while len(historial) > 0:
    afterPoping = historial.pop()
    print(f'we are poping: {afterPoping}')
    print(f'How it looks now: {historial}')
    print("#" * 5)
    
