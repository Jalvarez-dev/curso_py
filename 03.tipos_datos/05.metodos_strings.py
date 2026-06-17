# metodo para convertir un texto en mayuscula
texto_minuscula:str="hola"
print(texto_minuscula.upper())
# metodo para convertir un texto en minusculas
texto_mayuscula:str="HOLASSSSSS"
print(texto_mayuscula.lower())
# metodo para convertir solo la primer letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para convertir la primera letra de cada palabra en mayuscula como un titulo
print(texto.title())

# metodo par quitar espacios
texto_espacios:str="       osos       "
print(texto_espacios)
# este metodo quita los espacios que estan a la derecha e izquierda . si deseamo quietar solo los espacion de la izquierda usamos el metodo lstrip() y si deseamo quietra los espacios solo de la derecha usamos rstrip()
print(texto_espacios.strip())

# metodo para buscar un caracterec o conjunto de caracteres
# find retorna el indice donde comienza el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo a mi mama de gianfranco"
print(parrafo.find("gianfranco"))
print(parrafo[35:])

# metodo para reemplazar una parte de texto
texto_incorrecto:str="gianfranco es malo"
print(texto_incorrecto.replace("malo","bueno"))

# (metodo) operador binario de existencia
# este operador verifica si cierto texto existe o no dentro de otro retorna True si existe y False si no 
vocales:str="aeiouAEIUO"
print("A" in vocales)

# tarea averigua que son y cuales son los operadores unarios, binarios y ternarios
not False

# ternario
# valor_si_verdadero if condicion else valor_si_falso   
print("es verdad" if 20>30 else "es falso")

## realizar un programa que nos pida la contraseña si la contraseña es correcta el usuario podra ingresar caso contrario le dara un mensaje de contraseña incorrecta

password_user:str=input("ingresa tu contraseña:")
print("bienvenido al sistema" if password_user=="hola1234" else "contraseña incorrecta")