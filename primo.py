numero = int(input())

if(i > 1):
    for i in range(2, numero):
        if(numero % i == 0):
            print("No es primo.")
            break
    else:
        print("Es primo.")
else:
    print("No es primo")
