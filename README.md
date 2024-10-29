# Flask Device Usage API

Este proyecto es una API desarrollada con Flask que permite obtener el uso de dispositivos y ejecutar scripts específicos.

## Estructura del Proyecto

app.py Dockerfile requirements.txt src/ init.py scripts/ init.py script.py

## Endpoints

### Obtener Uso de un Dispositivo

- **URL:** `/usage/<device_id>`
- **Método:** `GET`
- **Descripción:** Obtiene el porcentaje de uso de un dispositivo específico.
- **Ejemplo de Respuesta:**

  ```json
  {
      "device_id": "1",
      "usage_percent": 75
  }

### Obtener Uso de Todos los Dispositivos
- **URL:** /usage/all
- **Método:** GET
- **Descripción:** Obtiene el porcentaje de uso de todos los dispositivos.
- **Ejemplo de Respuesta:**

    ```json
    [
        {
            "device_id": "1",
            "usage_percent": 75
        },
        {
            "device_id": "2",
            "usage_percent": 50
        }
    ]

### Ejecutar Script
- **URL:** /execute
- **Método:** POST
- **Descripción:** Ejecuta un script específico.
- **Ejemplo de Respuesta:**


    ```json
    {
        "message": "Script executed successfully"
    }

### Ejecución del Proyecto
Para ejecutar el proyecto, sigue los siguientes pasos:

1. Clona el repositorio.
2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:

    ```bash
    python app.py
    ```

La aplicación estará disponible en http://localhost:5000.

### Prueba del Endpoint de Ejecución de Script
Puedes probar el endpoint de ejecución de script utilizando curl:

    ```bash
    curl -X POST http://localhost:5000/execute
    ```

### Docker
También puedes ejecutar la aplicación utilizando Docker. Asegúrate de tener Docker instalado y ejecuta los siguientes comandos:

1. Construye la imagen de Docker:

    ```bash
    docker build -t flask-device-usage-api .
    ```

2. Ejecuta el contenedor:

    ```bash
    docker run -p 5000:5000 flask-device-usage-api
    ```

La aplicación estará disponible en http://localhost:5000.

### Autor
Este proyecto fue desarrollado por Edwin Sarmiento.