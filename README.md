
# 🖥️ **Recordatorio de Mantenimiento de PC** 💻

¡No dejes que tu PC se olvide de su mantenimiento! Este programa te enviará un recordatorio cada 5 meses para asegurarte de que tu equipo siga funcionando como un campeón. Y si no puedes hacerlo justo ahora, no te preocupes, ¡puedes posponer el recordatorio con un solo clic!

## 🎯 **Requisitos** 

- Python 3.x
- Librerías externas:
  - `python-dateutil` (para manejar las fechas de manera fácil y sin complicaciones)
  - `tk` (para la ventanita gráfica que te mostrará el recordatorio)

## 📦 **Instalación**

### 1. Clonar el repositorio

Si aún no tienes el proyecto, ¡no hay problema! Clónalo con este comando:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_directorio>
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Para mantener todo organizado y limpio, crea un entorno virtual:

```bash
python -m venv venv
```

### 3. Instalar las dependencias

Instala todo lo que necesitas con un simple comando:

```bash
pip install -r requirements.txt
```

### 4. Configuración

El programa guarda la próxima fecha de recordatorio en un archivo llamado `recordatorio_config.txt`. Si no existe, no te preocupes, el programa lo creará automáticamente la primera vez que lo ejecute.

### 5. Ejecutar el programa

¡Ya casi estás listo! Para que el recordatorio empiece a funcionar, solo ejecuta:

```bash
python recordatorio.py
```

Al iniciar, el programa te mostrará una notificación de mantenimiento y luego continuará programando recordatorios cada 5 meses. ¡Nunca olvides cuidar tu PC! 🚀

## 🚀 **Funcionalidad**

- **Notificación amigable**: El programa te enviará una notificación emergente recordándote que es hora de realizar el mantenimiento de tu PC.
- **Posponer recordatorio**: Si no puedes hacer el mantenimiento en ese momento, ¡solo haz clic en "Posponer 1 mes" y listo! El recordatorio se moverá automáticamente.
- **Próxima fecha**: Calcula la próxima fecha de mantenimiento sumando 5 meses a la fecha actual, así que nunca perderás el hilo.
- **Guardar y cargar fecha**: Guarda la fecha de recordatorio en un archivo de configuración (`recordatorio_config.txt`) y la carga cada vez que reinicies el programa. ¡Siempre sabrás cuándo es el próximo mantenimiento!

## 🗂️ **Archivos del Proyecto**

- `recordatorio.py`: El script principal que se encarga de hacer todo el trabajo.
- `recordatorio_config.txt`: Archivo donde se guarda la fecha de tu próximo mantenimiento.
- `requirements.txt`: Lista de las librerías necesarias para que todo funcione.
- `recordatorio.log`: Archivo donde se registran los eventos y errores del programa, por si alguna vez necesitas saber qué sucedió.

## 🛠️ **Contribución**

¡Nos encantaría que contribuyeras! Si tienes ideas geniales para mejorar este proyecto, haz un fork del repositorio, trabaja en tus cambios y envía un pull request. ¡Toda mejora es bienvenida! 🙌
