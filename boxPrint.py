def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be a single caracther string')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2: 
        raise  Exception('height must be greater than 2')
    

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)

symbol = input("Give me the symbol: ")
width = int(input("Give me the width: "))
heigth = int(input("Give me the heigth: "))
boxPrint(symbol, width, heigth)
