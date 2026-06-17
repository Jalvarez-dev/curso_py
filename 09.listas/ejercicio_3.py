alumnos:list[str]=['deduardo','noemi','victor','emerson','yo']
print(alumnos)
# eliminar por valor
alumnos.remove('yo')
print(alumnos)
# eliminar el ltimo valor por defecto
alumnos.pop()
print(alumnos)
## pop tambien elimina elementos por indice
### el metodo pop tiene la caracteristica de recuperar el elemento eliminado eso quiero decir que podemos almacenarlo en na variable
a=alumnos.pop(1)
print(f"elimine: {a}")
print(f"mi lista de desaprobados sera: {alumnos}")

## tengo una lista de marcas de vehiculos(toyota,nissan,datsun,daewod,simo mack,mazda,honda), crear un programa que realize lo siguienteeeeeee:
"""
1. eliminar el 5 elemento.
2. en su lugar agregar la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si existe honda en mi lista de vehiculos
"""
