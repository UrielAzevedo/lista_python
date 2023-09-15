
def vogais():

    vogais = "AEIOUaeiou"
    lines = ''

    while True:

        line = input()

        if line == '':
            break

        lines += line

    
    vogais = sum(1 for char in lines if char in vogais)

    print(vogais)