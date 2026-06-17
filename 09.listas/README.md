# Datos estructurados
- tenemos 3 tipos de datos primarios (string, numerico, boleano)
- tenemos 2 tipos de datos estructuraados (listas, diccionarios)
## Listas
Son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener:
- listas de tipo numerica
- listas de tipo texto
- listas de tipo mixto
python nos permite acceder a estas listas a travez de indices, los indices son ascendentes empesando del numero 0.
### creacion de listas
para listas solo basta encerrar los elementos que deseamos almacenar con `[]` inmediatamente despues del operador de asignacion `=`
```python
# Creando una lista vacia
lista:list=[] #lista vacia
# lista numerica
## OJON: Los elementos de una lista se separan por comas
lista_numerica:list[int]=[3,8,6] # lista de numeros enteros
listas_num_miixto:list[int|float]=[3.6,7,.7]
# lista de texto
amigos:list[str]=['eduardo','kevin']
# lista mixta
lista_mixta:list=['pedro',20,False,1.67]
```
### Acceder y modificar elementos de una lista
Para poder acceder a un elemento de la lista trabajamos con los indices que python le asigna a cada elemeento tenemos:
- los indices positivos (comienzan de 0 y van de izquierda a derecha)
- los indices negativos (comienzan de -1 y van de derecha a izquierda)
con estos indices podemos acceder al valor del elemento y tambien podremos modificarlos.
tenemos dos formas de acceder a los elementos:
- acceder y modifcar por indice (posicion)
```python
## acceder a elementos
frutas:list[str]=["🍎","🍌","🍒","🍑"]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# aceder al 2 elemento por su indice negativo
print(frutas[-3])
## modificar
frutas[3]="naranja"
```
- acceder y modificar por rango (slicing)
```python
vocales:str=['a','e','i','o','u]
# acceder a elementos por slicing
# esta tecnica nos permite accede a mas de un elemento en un sola linea de codigo
vocales[0:3]
## reemplazar elemento por slicing
vocales[0:3]=['A','E','I']
```
### Metodos para listas
un metodo es una accion que puede realizar en una lista , los metodos por li general se utilizan despues de la variables y se accede al metodos a travez de un punto.
los metodos mas comunes son aquello que nos permiten, agrega, modificar y eliminar
```python
# agregar elementos
## append
animales:list[str]=[]
animales.append("leon")
animales.append("gato")
# el metodo append agrega los elementos en la ultima posicion de nuestra lista
## insert
numeros_pares:list[int]=[4,6,10]
numeros_pares.insert(0,2)
numeros_pares.insert(3,8)
amigos:list[str]=["juan","jose"]
amigos.insert(1,"deduardo")
# eliminar elementos
## eliminar por indice
vocales:list[str]=["a","e","i","o","U"]
del vocales[-1]
## eliminar por valor
vocales:list[str]=["a","e","i","o","U"]
vocales.remove("U")
## usanso metodo pop
vocales:list[str]=["a","e","i","o","U"]
vocales.pop()
# en este caso pop elimina por defecto el ultimo elemento
vocales.pop(3)
# en este caso eliminara el elemento que se encuentre en la posicion 3

# buscar
## este metodo permite ubicar a travez del valor el primer elemento(la primera coincidencia) dentro de una lista, y devolvera el indice de ese valor, este metodo es index
amantes:list[str]=['chapo','cristian','emerson','victor']
# quiero ubicar si en mi lista de infieles existe victor
buscar:int=amantes.index("victor")#retorna un indice si existe 3
amantes[buscar] # victor
## busqueda por pertenecia
existe:bool="chapo" in amantes
```
  
## Diccionarios