# operaciones aritmeticas con numeros en python
# 1. suma - operador binario
# variables globales
## son datos que se pueden utilizar en cualquer parte del software que este construyendo
# variables locales
## son datos que solo son accesibles en pequeñas porciones de codigo o "scope"
firts_numb:int|float=20
second_numb:int|float=5

print(f"la suma de {firts_numb}+{second_numb}={firts_numb+second_numb}")
print(f"la resta de {firts_numb}-{second_numb}={firts_numb-second_numb}")
# divi
print(f"la divi de {firts_numb}/{second_numb}={firts_numb/second_numb}")
# multiplicacion
print(f"la multi de {firts_numb}*{second_numb}={firts_numb*second_numb}")
# divicion exacta
print(f"la diviexac de {firts_numb}//{second_numb}={firts_numb//second_numb}")

## incremento (++,+=) OjO: esta es una avreviatura de una expresion u operacion aritmetica no es un operador de incremente (numero=numero+1 , numero+=1)
print(f"el incremente de {firts_numb} es {++firts_numb}")
## decremento (--, +=) OjO: esta es una avreviatura de una expresion u operacion aritmetica no es un operador de incremente (numero=numero-1 , numero-=1)
print(f"el incremente de {firts_numb} es {--firts_numb}")
## potenciacion
print(f"la poten de {firts_numb}**{second_numb}={firts_numb**second_numb}")