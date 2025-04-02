n1 = int(input("Digite um valor :"))
n2 = int(input("Digite um valor :"))

if n1<n2 :
    n1=n1*10
    n2=n2/2
    n3=n1+n2
    if n3 % 2 ==0:
        print(f' {n3}é par')

    else:
        print(f'{n3}é par')

else:
    n2<n1
    n2=n2*10
    n1=n1/2
    n4=n2+n1
    if n4 % 2 ==0:
        print(f'{n4}é par')
    else:
        print(f'{n4}é impar')
