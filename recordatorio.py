import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
import os

# Nombre del archivo de configuración
CONFIG_FILE = "recordatorio_config.txt"
LOG_FILE = "recordatorio.log"

# Configuración del log
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def mostrar_notificacion():
    """Muestra una ventana emergente con más detalles sobre el mantenimiento."""
    root = tk.Tk()
    root.title("Recordatorio de Mantenimiento")
    root.geometry("350x150")
    
    label = tk.Label(root, text="Es hora de realizar el mantenimiento de tu PC.\n¡No lo olvides!", font=("Arial", 10))
    label.pack(pady=20)
    
    # Botones para cerrar o posponer el recordatorio
    def cerrar():
        root.quit()
    
    def posponer():
        proxima_fecha = calcular_proxima_fecha(1)  # Posponer por un mes
        guardar_proxima_fecha(proxima_fecha)
        root.quit()

    btn_cerrar = tk.Button(root, text="Cerrar", command=cerrar)
    btn_posponer = tk.Button(root, text="Posponer 1 mes", command=posponer)
    
    btn_cerrar.pack(side=tk.LEFT, padx=10)
    btn_posponer.pack(side=tk.RIGHT, padx=10)
    
    root.mainloop()

def calcular_proxima_fecha(meses=5):
    """Calcula la fecha de recordatorio sumando meses a la fecha actual."""
    try:
        fecha_actual = datetime.now()
        proxima_fecha = fecha_actual + relativedelta(months=meses)
        return proxima_fecha
    except Exception as e:
        logging.error(f"Error al calcular la próxima fecha: {e}")
        return None

def guardar_proxima_fecha(proxima_fecha):
    """Guarda la próxima fecha de recordatorio en un archivo de configuración."""
    try:
        with open(CONFIG_FILE, "w") as file:
            file.write(proxima_fecha.strftime("%Y-%m-%d"))
        logging.info(f"Próxima fecha de recordatorio guardada: {proxima_fecha.strftime('%Y-%m-%d')}")
    except Exception as e:
        logging.error(f"Error al guardar la próxima fecha: {e}")

def cargar_proxima_fecha():
    """Carga la próxima fecha de recordatorio desde el archivo de configuración."""
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                fecha_str = file.read().strip()
                return datetime.strptime(fecha_str, "%Y-%m-%d")
        logging.info("No se encontró archivo de configuración, calculando nueva fecha.")
        return None
    except Exception as e:
        logging.error(f"Error al cargar la próxima fecha: {e}")
        return None

def programar_recordatorio():
    """Programa el recordatorio de mantenimiento cada 5 meses."""
    try:
        proxima_fecha = cargar_proxima_fecha()

        if proxima_fecha is None:
            proxima_fecha = calcular_proxima_fecha()
            if proxima_fecha is None:
                print("No se pudo calcular la próxima fecha. Saliendo...")
                logging.error("No se pudo calcular la próxima fecha al inicio.")
                return
            guardar_proxima_fecha(proxima_fecha)

        while True:
            if datetime.now() >= proxima_fecha:
                mostrar_notificacion()
                proxima_fecha = calcular_proxima_fecha()
                if proxima_fecha is None:
                    print("No se pudo calcular la próxima fecha. Saliendo...")
                    logging.error("No se pudo calcular la próxima fecha tras el recordatorio.")
                    return
                guardar_proxima_fecha(proxima_fecha)
                print(f"Próxima fecha de recordatorio: {proxima_fecha.strftime('%Y-%m-%d')}")

            # Esperar 1 día (86400 segundos) antes de volver a verificar
            time.sleep(86400) 

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo...")
        logging.info("Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"Error en el programa principal: {e}")
        logging.error(f"Error en el programa principal: {e}")

if __name__ == "__main__":
    logging.info("El programa ha comenzado.")
    mostrar_notificacion()  # Mostrar notificación al inicio
    programar_recordatorio()  # Iniciar el ciclo de recordatorios
