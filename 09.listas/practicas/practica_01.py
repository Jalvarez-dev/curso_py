## una ferreteria tiene separada en dos listas los siguiente productos
"""
1. lista de productos de limpieza (10 productos)
2. lista de materiales de construccion (10 productos)
-------------------------------------------------
el dueño desea realizar las siguientes acciones:
1. en su lista de productos de limpieza existe un material de construccion, debes elimarlos y pasar el producto a alista que corresponde.
2. indicar si en la lista de M.C existe cemento.
3. en la lista de P.L buscar el producto lejia y cambiar su valor por lejia sapolio.
4. mostrar un mensaje donde se detalle cual es la lista de M.C y la lista de P.L formateado.
"""

# crear mi lista de productos de limpieza
productos_limpieza:list[str]=['jabon','lejia','escoba','re cojedor','desinfectante','bob esponja','aromatisante','detergente','cemento','bolsa de basura']
# crear mi lista de materiales de construccion
materiales_construccion:list[str]=['fierro','ladrillo','regla','yeso','espatula','clavos','alambre','calaminas','carretilla','tormillos']
# 1.cambiar de lista al cemento

elemento_retirado=productos_limpieza.pop(productos_limpieza.index("cemento"))
materiales_construccion.append(elemento_retirado)
# 2. indicar si existe cemento M.C
existe:bool="cemento" in materiales_construccion
print(f"existe el cemento?: {existe}")
## segunda opcio utilizando un operador ternario
print("cemento si exite" if existe else "cemento no existe")

# 3. cmbiar lejia por lejia sapolio
buscar=productos_limpieza.index("lejia")
productos_limpieza[buscar]="lejia sapolio"

# 4. mostrar mensaje
mensaje:str=f"""
     mi lista de productos de limpieza despues de las
     modificacion queda de la siguiente manera
     {productos_limpieza}
     ------------------------------------------------
     mi lista de materiales de construccion despues de 
     las modificacion queda de la siguiente manera
     {materiales_construccion}
"""
print(mensaje)