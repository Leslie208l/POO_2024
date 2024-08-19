import tkinter as tk
from tkinter import messagebox
from empleado import *
from reserva import *
from db_config import *

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.create_main_menu()
        
    def create_main_menu(self):
        self.clear_window()
        
        tk.Label(self.root, text="Menu Principal", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Registro de Cliente", command=self.register_client).pack(pady=5)
        tk.Button(self.root, text="Iniciar Sesión (Empleado)", command=self.login_employee).pack(pady=5)
        tk.Button(self.root, text="Crear Empleado", command=self.create_employee).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def register_client(self):
        self.clear_window()
        
        tk.Label(self.root, text="Registro de Cliente", font=("Arial", 16)).pack(pady=10)
        
        self.client_name_var = tk.StringVar()
        self.client_surname_var = tk.StringVar()
        self.client_email_var = tk.StringVar()
        self.client_phone_var = tk.StringVar()
        
        tk.Label(self.root, text="Nombre").pack(pady=5)
        tk.Entry(self.root, textvariable=self.client_name_var).pack(pady=5)
        
        tk.Label(self.root, text="Apellidos").pack(pady=5)
        tk.Entry(self.root, textvariable=self.client_surname_var).pack(pady=5)
        
        tk.Label(self.root, text="Email").pack(pady=5)
        tk.Entry(self.root, textvariable=self.client_email_var).pack(pady=5)
        
        tk.Label(self.root, text="Teléfono").pack(pady=5)
        tk.Entry(self.root, textvariable=self.client_phone_var).pack(pady=5)
        
        tk.Button(self.root, text="Registrar", command=self.save_client).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.create_main_menu).pack(pady=5)
    
    def save_client(self):
        nombre = self.client_name_var.get()
        apellidos = self.client_surname_var.get()
        email = self.client_email_var.get()
        telefono = self.client_phone_var.get()
        
        resultado = Reserva.registrar_cliente(nombre, apellidos, email, telefono)
        
        if resultado:
            messagebox.showinfo("Registro Exitoso", f"{nombre} {apellidos}, se registró correctamente con el email: {email}")
        else:
            messagebox.showerror("Error", "No fue posible insertar el registro. Inténtelo de nuevo.")
        
    def login_employee(self):
        self.clear_window()
        
        tk.Label(self.root, text="Iniciar Sesión (Empleado)", font=("Arial", 16)).pack(pady=10)
        
        self.employee_email_var = tk.StringVar()
        self.employee_password_var = tk.StringVar()
        
        tk.Label(self.root, text="Email").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_email_var).pack(pady=5)
        
        tk.Label(self.root, text="Contraseña").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_password_var, show='*').pack(pady=5)
        
        tk.Button(self.root, text="Iniciar Sesión", command=self.check_login).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.create_main_menu).pack(pady=5)
    
    def check_login(self):
        email = self.employee_email_var.get()
        password = self.employee_password_var.get()
        
        registro = Empleado.iniciar_sesion(email, password)
        
        if registro:
            empleado_id, nombre, apellidos = registro
            self.open_reservation_menu(empleado_id, nombre, apellidos)
        else:
            messagebox.showerror("Error", "Email y/o contraseña incorrectos. Inténtelo de nuevo.")
    
    def create_employee(self):
        self.clear_window()
        
        tk.Label(self.root, text="Crear Empleado", font=("Arial", 16)).pack(pady=10)
        
        self.employee_name_var = tk.StringVar()
        self.employee_surname_var = tk.StringVar()
        self.employee_email_var = tk.StringVar()
        self.employee_password_var = tk.StringVar()
        
        tk.Label(self.root, text="Nombre").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_name_var).pack(pady=5)
        
        tk.Label(self.root, text="Apellidos").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_surname_var).pack(pady=5)
        
        tk.Label(self.root, text="Email").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_email_var).pack(pady=5)
        
        tk.Label(self.root, text="Contraseña").pack(pady=5)
        tk.Entry(self.root, textvariable=self.employee_password_var, show='*').pack(pady=5)
        
        tk.Button(self.root, text="Crear Empleado", command=self.save_employee).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.create_main_menu).pack(pady=5)
    
    def save_employee(self):
        nombre = self.employee_name_var.get()
        apellidos = self.employee_surname_var.get()
        email = self.employee_email_var.get()
        password = self.employee_password_var.get()
        
        resultado = Empleado.crear_empleado(nombre, apellidos, email, password)
        
        if resultado:
            messagebox.showinfo("Empleado Creado", f"Empleado {nombre} {apellidos} creado exitosamente.")
        else:
            messagebox.showerror("Error", "No fue posible crear el empleado. Inténtelo de nuevo.")
    
    def open_reservation_menu(self, empleado_id, nombre, apellidos):
        self.clear_window()
        
        tk.Label(self.root, text=f"Bienvenido {nombre} {apellidos}", font=("Arial", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Crear Reserva", command=lambda: self.create_reservation(empleado_id, nombre, apellidos)).pack(pady=5)
        tk.Button(self.root, text="Mostrar Reservas", command=lambda: self.show_reservations(empleado_id, nombre, apellidos)).pack(pady=5)
        tk.Button(self.root, text="Modificar Reserva", command=lambda: self.modify_reservation(empleado_id, nombre, apellidos)).pack(pady=5)
        tk.Button(self.root, text="Eliminar Reserva", command=lambda: self.delete_reservation(empleado_id, nombre, apellidos)).pack(pady=5)
        tk.Button(self.root, text="Salir", command=self.create_main_menu).pack(pady=5)
    
    def create_reservation(self, empleado_id, nombre, apellidos):
        self.clear_window()
        
        tk.Label(self.root, text="Crear Reserva", font=("Arial", 16)).pack(pady=10)
        
        self.reservation_client_id_var = tk.StringVar()
        self.reservation_check_in_var = tk.StringVar()
        self.reservation_check_out_var = tk.StringVar()
        self.reservation_room_var = tk.StringVar()
        
        tk.Label(self.root, text="ID del Cliente").pack(pady=5)
        tk.Entry(self.root, textvariable=self.reservation_client_id_var).pack(pady=5)
        
        tk.Label(self.root, text="Fecha de Llegada").pack(pady=5)
        tk.Entry(self.root, textvariable=self.reservation_check_in_var).pack(pady=5)
        
        tk.Label(self.root, text="Fecha de Salida").pack(pady=5)
        tk.Entry(self.root, textvariable=self.reservation_check_out_var).pack(pady=5)
        
        tk.Label(self.root, text="Número de Habitación").pack(pady=5)
        tk.Entry(self.root, textvariable=self.reservation_room_var).pack(pady=5)
        
        tk.Button(self.root, text="Crear Reserva", command=lambda: self.save_reservation(empleado_id, nombre, apellidos)).pack(pady=10)
        tk.Button(self.root, text="Volver", command=lambda: self.open_reservation_menu(empleado_id, nombre, apellidos)).pack(pady=5)
    
    def save_reservation(self, empleado_id, nombre, apellidos):
        cliente_id = self.reservation_client_id_var.get()
        fecha_llegada = self.reservation_check_in_var.get()
        fecha_salida = self.reservation_check_out_var.get()
        habitacion = self.reservation_room_var.get()
        
        resultado = Reserva.crear_reserva(cliente_id, fecha_llegada, fecha_salida, habitacion, empleado_id)
        
        if resultado:
            messagebox.showinfo("Reserva Creada", "La reserva se ha creado exitosamente.")
        else:
            messagebox.showerror("Error", "No se pudo crear la reserva. Inténtelo de nuevo.")
    
    def show_reservations(self, empleado_id, nombre, apellidos):
        self.clear_window()
        
        tk.Label(self.root, text="Mostrar Reservas", font=("Arial", 16)).pack(pady=10)
        
        # Aquí deberías agregar la lógica para mostrar las reservas
        
        tk.Button(self.root, text="Volver", command=lambda: self.open_reservation_menu(empleado_id, nombre, apellidos)).pack(pady=5)
    
    def modify_reservation(self, empleado_id, nombre, apellidos):
        self.clear_window()
        
        tk.Label(self.root, text="Modificar Reserva", font=("Arial", 16)).pack(pady=10)
        
        # Aquí deberías agregar la lógica para modificar una reserva
        
        tk.Button(self.root, text="Volver", command=lambda: self.open_reservation_menu(empleado_id, nombre, apellidos)).pack(pady=5)
    
    def delete_reservation(self, empleado_id, nombre, apellidos):
        self.clear_window()
        
        tk.Label(self.root, text="Eliminar Reserva", font=("Arial", 16)).pack(pady=10)
        
        # Aquí deberías agregar la lógica para eliminar una reserva
        
        tk.Button(self.root, text="Volver", command=lambda: self.open_reservation_menu(empleado_id, nombre, apellidos)).pack(pady=5)

def main():
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
