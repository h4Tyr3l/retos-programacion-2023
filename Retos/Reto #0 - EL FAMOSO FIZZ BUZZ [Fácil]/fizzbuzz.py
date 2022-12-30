def fizzbuzz(rango,num_1,num_2):
    for num in range (1, rango+1):
        if num % num_1 == 0 and num % num_2 == 0:
            print("fizzbuzz", end="\n")
            continue
        elif num % num_2 == 0:
            print("buzz", end="\n")
            continue
        elif num % num_1 == 0:
            print("fizz", end="\n")
            continue
        print(num, end="\n")

rango=int(input("Informe el valor máximo del rango que le interesa: "))
num_1=int(input("Informe el valor que le interesaría reemplazar por la expresión fizz: "))
num_2=int(input("Informe el valor que le interesaría reemplazar por la expresión buzz: "))
fizzbuzz(rango,num_1,num_2)