from clases import *

from datetime import datetime 

# Crear el hotel
hotel = Hotel("Hotel lesmi", "Calle Principal 123", 4, [])

# Crear las habitaciones
habitacion1 = Habitacion(1, "Habitación simple", 50.0, True)
habitacion2 = Habitacion(2, "Habitación doble", 80.0, True)

# Agregar las habitaciones al hotel
hotel.agregarHabitacion(habitacion1)
hotel.agregarHabitacion(habitacion2)

# Crear el cliente
cliente = Cliente("Juan Pérez", "1234567890", "juan.perez@email.com")

# Crear la tarjeta de crédito
tarjetaCredito = TarjetaCredito("1234567890123456", "01/25", "123", "Juan Pérez", "Apellido")

# Crear el pago
pago = Pago(100.0, "Tarjeta de crédito", tarjetaCredito)

# Crear la reserva
fecha_inicio = datetime.strptime("2024-07-01", "%Y-%m-%d")
fecha_fin = datetime.strptime("2024-07-05", "%Y-%m-%d")
reserva = Reserva(fecha_inicio, fecha_fin, 2, 0, habitacion1, cliente, pago)

# Confirmar la reserva
if reserva.confirmarReserva():
    print(f"Reserva confirmada con el código: {reserva.generarCodigoReserva()}")
    print(f"El costo total de la reserva es: {reserva.calcularCostoTotal()}")
else:
    print("No se pudo confirmar la reserva.")

# Cancelar la reserva (opcional)
if reserva.cancelarReserva():
    print("Reserva cancelada.")
else:
    print("No se pudo cancelar la reserva.")

