class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = set()
    def asignar_horario(self, horario):
        if horario in self.horarios:
            return f"⚠️ El conductor {self.nombre} ya tiene asignado el horario {horario}."
        self.horarios.add(horario)
        return f"✅ Horario {horario} asignado al conductor {self.nombre}."


class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = set()
        self.conductor = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta
        return f"🛣️ Ruta '{ruta}' asignada al bus {self.id_bus}."

    def registrar_horario(self, horario):
        if horario in self.horarios:
            return f"⚠️ El bus {self.id_bus} ya tiene registrado el horario {horario}."
        self.horarios.add(horario)
        return f"✅ Horario {horario} registrado en el bus {self.id_bus}."

    def asignar_conductor(self, conductor):
        if not self.horarios:
            return f"⚠️ El bus {self.id_bus} no tiene horarios asignados. Registra un horario primero."
        
        # Validación de los horarios con el conductor
        for horario in self.horarios:
            if horario in conductor.horarios:
                return f"⚠️ El conductor {conductor.nombre} ya tiene el horario {horario} asignado, no puede asignarse al bus {self.id_bus}."
        
        self.conductor = conductor
        return f"🚌 Conductor {conductor.nombre} asignado al bus {self.id_bus}."


class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self, id_bus):
        if id_bus in self.buses:
            return f"⚠️ El bus {id_bus} ya existe."
        self.buses[id_bus] = Bus(id_bus)
        return f"🆕 Bus {id_bus} agregado correctamente."

    def agregar_conductor(self, nombre):
        if nombre in self.conductores:
            return f"⚠️ El conductor {nombre} ya existe."
        self.conductores[nombre] = Conductor(nombre)
        return f"👷 Conductor {nombre} agregado correctamente."

    def obtener_bus(self, id_bus):
        return self.buses.get(id_bus, None)

    def obtener_conductor(self, nombre):
        return self.conductores.get(nombre, None)

    def mostrar_menu(self):
        opciones = {
            "1": lambda: self.agregar_bus(input("Ingrese el ID del bus: ")),
            "2": self.agregar_ruta,
            "3": self.registrar_horario_bus,
            "4": lambda: self.agregar_conductor(input("Ingrese el nombre del conductor: ")),
            "5": self.agregar_horario_conductor,
            "6": self.asignar_conductor_a_bus,
            "7": self.salir
        }

        while True:
            print("\n📌 MENÚ DE GESTIÓN DE BUSES 📌")
            print("1. Agregar bus")
            print("2. Agregar ruta a bus")
            print("3. Registrar horario a bus")
            print("4. Agregar conductor")
            print("5. Agregar horario a conductor")
            print("6. Asignar bus a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")
            accion = opciones.get(opcion, self.opcion_invalida)
            print(accion())

    def agregar_ruta(self):
        id_bus = input("Ingrese el ID del bus: ")
        bus = self.obtener_bus(id_bus)
        if not bus:
            return f"🚫 Bus {id_bus} no encontrado."
        ruta = input("Ingrese la ruta del bus: ")
        return bus.asignar_ruta(ruta)

    def registrar_horario_bus(self):
        id_bus = input("Ingrese el ID del bus: ")
        bus = self.obtener_bus(id_bus)
        if not bus:
            return f"🚫 Bus {id_bus} no encontrado."
        horario = input("Ingrese el horario (ejemplo: 08-16, 09-13, 16-20): ")
        return bus.registrar_horario(horario)

    def agregar_horario_conductor(self):
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = self.obtener_conductor(nombre)
        if not conductor:
            return f"🚫 Conductor {nombre} no encontrado."
        horario = input("Ingrese el horario (ejemplo: 08-16, 09-13, 16-20): ")
        return conductor.asignar_horario(horario)

    def asignar_conductor_a_bus(self):
        id_bus = input("Ingrese el ID del bus: ")
        bus = self.obtener_bus(id_bus)
        if not bus:
            return f"🚫 Bus {id_bus} no encontrado."
        
        nombre = input("Ingrese el nombre del conductor: ")
        conductor = self.obtener_conductor(nombre)
        if not conductor:
            return f"🚫 Conductor {nombre} no encontrado."
        
        return bus.asignar_conductor(conductor)

    def opcion_invalida(self):
        return "❌ Opción inválida. Intente nuevamente."

    def salir(self):
        print("🚪 Saliendo del sistema...")
        exit()


# Ejecutar el sistema
if __name__ == "__main__":
    admin = Admin()
    admin.mostrar_menu()