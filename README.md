# Recordatorio de Mantenimiento de PC

Este programa envía un recordatorio de mantenimiento para tu PC cada 5 meses. Utiliza una ventana emergente para notificarte sobre la necesidad de realizar el mantenimiento.

## Requisitos

- Python 3.x
- Librerías externas:
  - `python-dateutil` (para manejar fechas)

## Instalación

### 1. Clonar el repositorio

Si aún no tienes el repositorio, clónalo usando:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_directorio>
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Para aislar las dependencias del proyecto:

```bash
python -m venv venv
```

### 3. Instalar las dependencias

Instala las dependencias requeridas utilizando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configuración

El programa guarda la próxima fecha de recordatorio en un archivo llamado `recordatorio_config.txt`. Si no existe, el programa lo creará automáticamente al calcular la fecha de recordatorio por primera vez.

### 5. Ejecutar el programa

Ejecuta el script para iniciar el recordatorio:

```bash
python recordatorio.py
```

El programa mostrará una notificación de mantenimiento al iniciar y luego continuará programando recordatorios cada 5 meses.

## Funcionalidad

- **Mostrar notificación**: Al ejecutarse, el programa mostrará una notificación emergente con un mensaje recordatorio.
- **Calcular próxima fecha**: El programa calcula la próxima fecha de mantenimiento sumando 5 meses a la fecha actual.
- **Guardar y cargar la fecha**: El programa guarda la fecha de recordatorio en un archivo de configuración (`recordatorio_config.txt`) y lo utiliza al reiniciar el programa.

## Archivos del proyecto

- `recordatorio.py`: El script principal que ejecuta el programa.
- `recordatorio_config.txt`: Archivo donde se guarda la próxima fecha de mantenimiento.
- `requirements.txt`: Lista de dependencias del proyecto.

## Contribución

Si deseas contribuir, por favor haz un fork de este repositorio y envía un pull request con las mejoras.
