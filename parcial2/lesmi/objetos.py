from clases import *


hotel = Hotel("Hotel lesmi", "Calle Principal 123", 4, [])


habitacion1 = Habitacion(1, "Habitación simple", 50.0, True)
habitacion2 = Habitacion(2, "Habitación doble", 80.0, True)
hotel.agregarHabitacion(habitacion1)
hotel.agregarHabitacion(habitacion2)


cliente = Cliente("Juan Pérez", "1234567890", "juan.perez@email.com")


tarjetaCredito = TarjetaCredito("1234567890123456", "01/25", "123", "Juan Pérez", "Apellido")


pago = Pago(100.0, "Tarjeta de crédito", tarjetaCredito)

