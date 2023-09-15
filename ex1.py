def ex_a (arr):
    for n in arr:
        print(n)

def ex_b (arr):
    for i, n in enumerate(arr):
        if (i % 2 == 0):
            print (n)

def ex_c (arr):
    for i, n in enumerate(arr):
        if (i % 2 != 0):
            print (n)

def ex_d (arr):
    for n in arr:
        n = round(n, 1)
        print(n)
        # print("{:.1f}".format(n))

def ex_e (arr):

    total = round(sum(arr), 2)
    print(total)

def ex_f (arr):
    for n in arr:
        n = round(n, 0)
        print(n)

def ex_g (arr):
    for n in arr:
        print(bin(int(n))[2:])

def ex_h (arr):
    for n in arr:
        print(oct(int(n))[2:])

def ex_i (arr):
    for n in arr:
        print(hex(int(n))[2:])