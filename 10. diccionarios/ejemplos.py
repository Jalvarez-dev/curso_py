# modulos y libreria estandar
# libreria estandar typing tipar datos a listas y diccionarios para hacer mas optimo el codigo
# modulo es una porcion de codigo utilizable, para poder usarlo necesitamos inporta la parte del codigo que deseamos utilizar.

# ente codigo estoy importando desde l libreria typing la funcion Union,
# Union me permite tipar una coleccion de tipos, que si no sbes el tipo de dato con union le podemos pasar una lista de los posibles tipod de datos que puede tener mi valor.
from typing import Union
#sin libreria
#alumno:dict[str:str|int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":78654328,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
# acceder
## clasica
print(alumno["dni"])
# codigo erroneo print(alumno["tricula"])
## metodos
print(alumno.get("edad","valor no encontrado"))

# crear/modificar un valor
print(alumno)
alumno["nombre"]="otro" # si existe laa clave actualiza el valor
alumno["ruc"]=90876543267 # si no existe la clave lo crea
print(alumno)

# crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
# eliminar
eliminado=alumno.pop("carrera")
print(f"el elemento eliminado es: {eliminado}")
print(f"mi nuevo diccionario {alumno}")