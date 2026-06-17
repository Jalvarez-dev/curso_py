1. # crear un programa que busque en el pensamiento de cesar acuña la palabra politicos.
# hay políticos que no hacen nada porque nunca han hecho nada.
# y mostrarlo por terminal si lo encuentra
pensamiento_uno:str="hay políticos que no hacen nada porque nunca han hecho nada."
palabra_buscar="políticos"
print("políticos" if pensamiento_uno.find(palabra_buscar)>0 else "texto no encontrado")
2. # crear un programa que en el siguiente texto 'yo ya no vivo en Trujillo, vivo en Perú'. busque Perú y lo reemplaze por Narnia. finalmente mostrarlo por terminal
pensamiento_dos:str='yo ya no vivo en Trujillo, vivo en Perú'
print(pensamiento_dos)
print(pensamiento_dos.replace("Perú","Narnia"))