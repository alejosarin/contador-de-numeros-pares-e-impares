n=int(input("\ndiguite un numero natural: "))
npares=0
nimpares=0
while n!=0:
    if n%2==0:
        npares=npares+1
    else:
        nimpares=nimpares+1
    n=int(input("\ndiguite un numero natural: "))
print("La cantidad de numeros pares es "+str(npares)+"\ny la cantidad de numeros impares es "+str(nimpares)+"\n\n")

