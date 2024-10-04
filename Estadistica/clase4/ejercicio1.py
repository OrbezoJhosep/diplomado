import math
#Pregunta 1
def binomial (x,n,p):
    if n >= x >=0: #Evitamos problemas con el factorial
        factorial = math.factorial(n)/(math.factorial(x)*(math.factorial(n-x)))
        probaibilidade =  (p**x)*((1-p)**(n-x))
        return factorial * probaibilidade
    else:
        return 0
x = 14
n = 20
p = 0.8

Resultado = binomial(x,n,p)
print (f'La probabilidad de que de 20 personas solo se recuperen 14 es de {Resultado:.4f}')

#Pregunta 2 
x = 0
n = 10
p = 0.25

Resultado2 = binomial(x,n,p)
print(f'El resultado de que conteste 0 preguntas es de {Resultado2:.4f}')
print(f'El resultadod de no acertar al menos una es {1-Resultado2:4f}')

#Pregunta 3

def possion (t,u):
    e = math.exp(1)
    probailidad = (e**(-u))*((u)**t)/math.factorial(t)
    return probailidad
u = 7
t = 5

Resultado3 = possion(t,u)
print(f'La probabilidad de que llegan 5 personas es {Resultado3:4f}')

resultadoA = possion(0,7)
resultadoB = possion(1,7)

complemento = 1 - resultadoA - resultadoB

print(f'La probabilidad de que lleguen al menos dos clientes es {complemento:4f}')

#Pregunta 4
def hipergeometrica(K, N, n, k):
    return (math.comb(K, k) * math.comb(N - K, n - k)) / math.comb(N, n)

N = 20
K = 8 
n = 6 
k = 1

media = n * (K / N)
varianza = n * (K / N) * ((N - K) / N) * ((N - n) / (N - 1))

print(f"Media del número de afroamericanos en el jurado: {media:.4f}")
print(f"Varianza del número de afroamericanos en el jurado: {varianza:.4f}")

probabilidad_1_afroamericano = hipergeometrica(K, N, n, k)
print(f"Probabilidad de que solo haya 1 afroamericano en el jurado: {probabilidad_1_afroamericano:.4f}")