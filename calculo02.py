print("seja bem vindo ao cálculo de média da sua nota!")
print("siga as instruções a seguir, para calcular a média de natureza: ") 

f = int(input("sua nota em biologia: ")) 
while 0<=f>10:
        nota10=print("sua nota não pode ser maior que 10")
        f = int(input("sua nota em biologia: ")) 

y = int(input("sua nota em química: "))
while 0<=y>10:
        print(nota10)
        y = int(input("sua nota em química: "))
o = int(input("sua nota em física: "))
while 0<=o>10:
        print(nota10)
        o = int(input("sua nota em física: "))
t = ((f+y+o)/3)
q = print("ok, sua média em naturezas é: %i"  %t) 

print(" agora vamos calcular sua média em humanas:")
f1= int(input("sua nota em humanas: "))
while 0<=f1>10:
        print(nota10)
        f1 = int(input("sua nota em humanas: "))
y1= int(input("sua nota em geografia: "))
while 0<=y1>10:
        print(nota10)
        y1 = int(input("sua nota em geografia: "))
o1= int(input("sua nota em sociologia e filosofia: "))
while 0<=o1>10:
        print(nota10)
        o1 = int(input("sua nota em sociologia e filosofia: "))
t1 = ((f1+y1+o1)/3)
print("sua média em humanas é: %i" %t1)

print("agora vamos calcular sua média exatas e linguagens: ")
f2 = int(input(" sua nota em matemática: "))
while 0<=f2>10:
        print(nota10)
        f2 = int(input("sua nota em matemática: "))
y2 = int(input("sua nota em português:"))
while 0<=y2>10:
        print(nota10)
        y2 = int(input("sua nota em português: "))
t2 = ((f2+y2)/2)
print("sua média em liguagens e exatas %i" %t2)

t3 = ((t+t1+t2)/3)
print("veremos sua média geral: %i" %t3)

print("agora veremos o seu conceito geral: ")
p1= "parabéns, você conquistou o conceito"
list1=["E","D","C","B","A"]

if t3 == 0:
        print("você foi reprovado, seus requisitos mínimos não foram alcançados")
elif 1<=t3<=2: 
        print(p1,list1[0])
elif 3<=t3<=4:
        print(p1,list1[1])
elif 5<=t3<=6:
        print(p1,list1[2])
elif 7<=t3<=8:
        print(p1,list1[3])
else: 
        print(p1,list1[4])
print("muito obrigado pela preferência.")