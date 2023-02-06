
# Ejercicio de Factorial de forma recusiva
def Factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*(Factorial(n-1))

print("Forma recursiva",Factorial(5))


#Ejercicio de Factorial de forma iterativa

def Factorial(n):
  result = 1
  for i in range(1,n+1):
    result = result * i
  return result

print("Forma iterativa",Factorial(5))

