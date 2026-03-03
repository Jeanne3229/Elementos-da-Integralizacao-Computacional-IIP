import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#Questao 3:
#Um processo em execução tem consumo de CPU instantâneo  c(t)=0.5t**2+3  unidades de CPU por segundo em  t∈[0,10] .



def consumo_da_cpu(t):
  return 0.5 * t**2 + 3

#primeiro calcular a integral
def calculara_integral():
  t = sp.symbols('t')
  funcao_simbolica = 0.5 * t**2 + 3
  resultado_exato = sp.integrate(funcao_simbolica, (t, 0, 10))
  return float(resultado_exato)

#Agora pela soma de riemann (ponto medio)

def midpoint(a, b, n):
  largura = (b - a) / n
  soma_areas = 0
  for i in range(n):
    x_daesquerda = a + i * largura
    x_dadireita = x_daesquerda + largura
    ponto_medio = (x_daesquerda + x_dadireita) / 2
    #Agora o cálculo da área = 
    soma_areas += consumo_da_cpu(ponto_medio) * largura 
  return soma_areas

#Cálculo final com os pontos inferiores e superiores
limite_a = 0
limite_b = 10
n_retangulos = 100

#puxando as funcoes:
valor_exato = calculara_integral() #esse puxa o calculo da integral
valor_aproximado = midpoint(limite_a, limite_b, n_retangulos) #esse puxa o calculo com a soma de riemann

#agora o calculo do erro entre eles:
erro = abs(valor_exato - valor_aproximado)


#agora impressoes entre eles
print("-" * 40)
print(f"RESULTADOS QUESTÃO 3")
print("-" * 40)
print(f"1. Integral Definida (SymPy):   {valor_exato:.4f}")
print(f"2. Aproximação Riemann (n={n_retangulos}): {valor_aproximado:.4f}")
print(f"3. Erro entre as respostas:      {erro:.6f}")
print("-" * 40)


