import re

vetor=[]
cep = int (input('Digite seu CEP: '))

if (cep >=999999) or (cep < 100000):
    print("CEP INVÁLIDO!")
    
else:
    cep=str(cep)
    p1=re.compile(r'\d')
    verif=p1.findall(cep)
    vetor=verif

if vetor[0]==vetor[1]:
    print("CEP INVÁLIDO!")
elif vetor[0]==vetor[2]:
    print("CEP INVÁLIDO!")
elif vetor[2]==vetor[4]:
    print("CEP INVÁLIDO!")
elif vetor[1]==vetor[3]:
    print("CEP INVÁLIDO!")
elif vetor[3]==vetor[5]:
    print("CEP INVÁLIDO!")
else:
    print("CEP VALIDO!")