# crear un progrma que me permita agregar a mi lista de comprar los siguientes ingredientes (trucha,cebolla,limon,culantro,pinguita de nomo,papa,chancha)

# entrada de datos
ingredientes:list[str]=[]
# desarrollo
for i in range(7):
    ingrediente:str=input("ingres tu ingrediente: ")
    ingredientes.append(ingrediente)
# datos de salida
print(ingredientes)

## crear un programa que agrege al principio de la lista el grupo a de los paises participantes en el mundial
grupo_a:list[str]=[]
grupo_a.insert(0,"rep. checa")
# ["rep. checa"]
grupo_a.insert(0,"corea del sur")
# ["corea del sur","rep. checa"]
grupo_a.insert(0,"sudafrica")
# ["sudafrica","corea del sur","rep. checa"]
grupo_a.insert(0,"mexico")
# ["mexico","sudafrica","corea del sur","rep. checa"]
print(grupo_a)