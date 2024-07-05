class Hotel:
    def __init__(self, nombre, direccion, numeroDeEstrellas, habitaciones):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__numeroDeEstrellas = numeroDeEstrellas
        self.__habitaciones = habitaciones

    def consultarHabitacionesDisponibles(self, fechainicio, fechafin):
        disponibles = []
        for habitacion in self.__habitaciones:
            if habitacion.consultarDisponibilidad(fechainicio, fechafin):
                disponibles.append(habitacion)
        return disponibles

    def agregarHabitacion(self, habitacion):
        self.__habitaciones.append(habitacion)


class Habitacion:
    def __init__(self, id, descripcion, precioPorNoche, disponible):
        self.__id = id
        self.__descripcion = descripcion
        self.__precioPorNoche = precioPorNoche
        self.__disponible = disponible

    def consultarDisponibilidad(self, fechainicio, fechafin):
        return self.__disponible

    def reservar(self):
        self.__disponible = False


class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo

    def realizarPago(self, pago):
        return pago.realizarPago()

    def cancelarPago(self, pago):
        return pago.cancelarPago()


class Pago:
    def __init__(self, montoPago, metodoPago, tarjetaCredito):
        self.__montoPago = montoPago
        self.__metodoPago = metodoPago
        self.__tarjetaCredito = tarjetaCredito

    def realizarPago(self):
        return True

    def cancelarPago(self):
        return True


class Reserva:
    def __init__(self, fechainicio, fechafin, numAdultos, numNinos, habitacionSeleccionada, cliente, pago):
        self.__fechainicio = fechainicio
        self.__fechafin = fechafin
        self.__numAdultos = numAdultos
        self.__numNinos = numNinos
        self.__habitacionSeleccionada = habitacionSeleccionada
        self.__cliente = cliente
        self.__pago = pago
        self.__codigoReserva = None

    def calcularCostoTotal(self):
        num_noches = (self.__fechafin - self.__fechainicio).days
        return num_noches * self.__habitacionSeleccionada._Habitacion__precioPorNoche

    def generarCodigoReserva(self):
        import random
        self.__codigoReserva = random.randint(10000, 99999)
        return self.__codigoReserva

    def confirmarReserva(self):
        if self.__cliente.realizarPago(self.__pago):
            self.__habitacionSeleccionada.reservar()
            self.generarCodigoReserva()
            return True
        return False

    def cancelarReserva(self):
        if self.__cliente.cancelarPago(self.__pago):
            self.__habitacionSeleccionada._Habitacion__disponible = True
            self.__codigoReserva = None
            return True
        return False


class TarjetaCredito:
    def __init__(self, numero, fechavencimiento, codigoSeguridad, nombreTitular, apellidoTitular):
        self.__numero = numero
        self.__fechavencimiento = fechavencimiento
        self.__codigoSeguridad = codigoSeguridad
        self.__nombreTitular = nombreTitular
        self.__apellidoTitular = apellidoTitular

    def validarTarjeta(self):
        return True

    def procesarPago(self, monto):
        return True
