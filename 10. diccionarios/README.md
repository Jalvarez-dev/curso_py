# Diccionarios
los diccionarios son la forma mas comun de almacenar datos estructuraados de objetos que nos rodea en el mundo, al igual que las listas que guardan informacion en `elementos`, de igual manera los diccionarios almacenan sus datos en `elementos` separados por comas.
la diferencia es que las listas almacenan los elementos por `indice` y `valor`.
y los diccionarios almacenan los elementos por `clave:valor`.
**ejemplo:**
```python
vocales:list[str]=['a','e','i','o','u'] #valores
#  indices          0    1   2   3   4
# un elemento en un lista esta confromado por dos cositas el indice y su valor.
# para acceder aun vaor en una lista
vocales[2] # i
alumno:dict={'nombre':'eduardo','edad':40}
# un elemento en un diccionario esta confromado por clave:valor
# pra acceder a un diccionaario
alumno["nombre"] # eduardo
```
## acceder a elementos
- **por clave (forma directa)**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona["edad"]) #16
print(persona["email"]) #celi@email.com
```
- **por su metodo (forma mas segura)**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com"
}
print(persona.get("nombre")) #celia
# la diferecnia de este metodo es que no permite manejar errores
print(persona.get("telefono")) #None
print(persona.get("telefono","No disponible")) # si la clave telefono no existe no mostra None si no el segundo parametro que le pasemos al metod get.
```
## modificaar elementos
**cambiar un valor existente**
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
}
persona["edad"]=19
# egregar una nueva clave:valor
persona["carrera"]="agro"
# si la clave no existe se crea automaaticmente. si existe se actualiza.
```
## agregar/actualizar multiples elementos
para esto tenemos que hacer uso de el metodo `.update`
se peude agregar si lo pares de `clave:valor` no exite y actualizar si el `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20465783674
}
# actualizar usando el metodo .update tengo dos maneras de usar este metodo
# 1. diccionarios
tienda.update({"ruc":23456789023,"telefono":987654321})
# 2. pares clave=valor.
tienda.updaate(h_atencion="9-12",gerente="kevin")
```

## eliminar elementos
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20465783674
}
el_eliminado=tienda.pop("ruc")
tienda.popitem() # elimina el ultimo elemento
# para limpiar todo el diccionario
tienda.clear()
```
## recorrer un diccionario (tarea)