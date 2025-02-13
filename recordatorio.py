import time
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta  # Para manejar la adición de meses

# Nombre del archivo de configuración
CONFIG_FILE = "recordatorio_config.txt"

def mostrar_notificacion():
    """Muestra una notificación en una ventana emergente usando Tkinter."""
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Llama a tu Tecnico", "Es hora de realizar el mantenimiento de tu PC. ¡No lo olvides!")
    root.destroy()

def calcular_proxima_fecha():
    """Calcula la fecha de recordatorio sumando 5 meses a la fecha actual."""
    try:
        fecha_actual = datetime.now()
        proxima_fecha = fecha_actual + relativedelta(months=5)
        return proxima_fecha
    except Exception as e:
        print(f"Error al calcular la próxima fecha: {e}")
        return None

def guardar_proxima_fecha(proxima_fecha):
    """Guarda la próxima fecha de recordatorio en un archivo de configuración."""
    try:
        with open(CONFIG_FILE, "w") as file:
            file.write(proxima_fecha.strftime("%Y-%m-%d"))
    except Exception as e:
        print(f"Error al guardar la próxima fecha: {e}")

def cargar_proxima_fecha():
    """Carga la próxima fecha de recordatorio desde el archivo de configuración."""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                fecha_str = file.read().strip()
                return datetime.strptime(fecha_str, "%Y-%m-%d")
        return None
    except Exception as e:
        print(f"Error al cargar la próxima fecha: {e}")
        return None

def programar_recordatorio():
    """Programa el recordatorio de mantenimiento cada 5 meses."""
    try:
        proxima_fecha = cargar_proxima_fecha()

        if proxima_fecha is None:
            proxima_fecha = calcular_proxima_fecha()
            if proxima_fecha is None:
                print("No se pudo calcular la próxima fecha. Saliendo...")
                return
            guardar_proxima_fecha(proxima_fecha)

        while True:
            if datetime.now() >= proxima_fecha:
                mostrar_notificacion()
                proxima_fecha = calcular_proxima_fecha()
                if proxima_fecha is None:
                    print("No se pudo calcular la próxima fecha. Saliendo...")
                    return
                guardar_proxima_fecha(proxima_fecha)
                print(f"Próxima fecha de recordatorio: {proxima_fecha.strftime('%Y-%m-%d')}")

            time.sleep(86400)  # Esperar 1 día (86400 segundos) antes de volver a verificar

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo...")
    except Exception as e:
        print(f"Error en el programa principal: {e}")

if __name__ == "__main__":
    mostrar_notificacion()  # Mostrar notificación al inicio
    programar_recordatorio()  # Iniciar el ciclo de recordatorios
