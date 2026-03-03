import scipy.integrate as spi

#QUESTÃO 4: Custo Total de Execução de Algoritmo
def g(n):
  return 0.01 * n**2 + 2 * n

resultado, erro = spi.quad(g, 0, 1000)

print("-" * 40)
print("RESULTADO QUESTÃO 4 - CUSTO TOTAL")
print("-" * 40)
print(f"O custo total acumulado e:{resultado:.2f})
print(f"Erro estimado pelo SciPy:{erro:.2e}")
print("-" * 40)
