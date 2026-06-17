# utilizar tecnicas para unir string en un solo
## concatenacion
## para esto usamos el operador de concatenacion +
# cuando este operador se encuentra entre dos texto se convierte en el operador de concatenacion y cuando esta entre dos numero es el operador de adicion(suma).
nombre:str = "noemi"
apellido:str = "noseprofesor"
nombre_completo:str = nombre+" "+apellido
print(nombre_completo)#salida: noemi noseprofesor

## opcion mas optima de concatenacion
print(nombre,apellido)

## f-strings (tarea)
# formato de string esto sirve para formatear string con variables de python y para sus se requiere de un f antes de escribir un string, si se desea incluir condigo python en el string se debrr encerrar entre llaves {}
nombre:str = "Gianfranca"
edad:int = 14
# mesnaje de salida me diga hola mi nombre es {} y tengo {}
print(f"hola mi nombre es {nombre} y tengo {edad}")

## plantillas de string
nombre_cliente:str=input("ingrese tu nombre: ")
ruc_cliente:int=int(input("ingresa ruc: "))
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrese codigo producto: ")
nombre_producto:str=input("ingrese nombre producto: ")
precio_unidad:float=float(input("el precio del producto: "))
cantidad_producto:float=float(input("cantidad a comprar: "))
precio_total:float=precio_unidad*cantidad_producto

plantilla:str=f"""
cliente: {nombre_cliente}........RUC: {ruc_cliente}
Direccion: {direccion_cliente}

codigo producto   |  nombre producto | p_unidad  | cantidad
-----------------------------------------------------------
{codigo_producto}       {nombre_producto}    {precio_unidad}  {cantidad_producto}
-----------------------------------------------------------
El precio total de su compra es de: {precio_total}
"""
print(plantilla)