from cliente import Cliente
from producto import Producto
from venta import Venta
from tienda import Tienda

# Crear cliente
cliente1 = Cliente("Pedro", "pedro_hl@mail.com", 1500)
cliente2 = Cliente("Cristina", "cristina_cy@mail.com", 1200)

# Crear producto
produ1 = Producto("Teclado", 450)
produ2 = Producto("Mouse", 250)

produ3 = Producto("Adaptador de red", 500)
produ4 = Producto("Memoria UBS", 150)

# Crear venta y agregar producto
venta1 = Venta(cliente1)
venta1.agregar_producto(produ1)
venta1.agregar_producto(produ2)

venta2 = Venta(cliente2)
venta2.agregar_producto(produ3)
venta2.agregar_producto(produ4)

# Crear tienda y registrar venta
tienda = Tienda("TechStore")
tienda.registrar_venta(venta1)
tienda.registrar_venta(venta2)

# Mostrar resultado
print(cliente1.mostrar_info())
print(f"Total de la venta1: ${venta1.total():.2f}")
print(cliente2.mostrar_info())
print(f"Total de la venta2: ${venta2.total():.2f}")
print(f"Ventas registradas: {len(tienda.ventas)}")