# Convertir datos de formato JSON a CSV

Este script de Python te permite convertir datos en formato JSON a un archivo CSV. El script lee un archivo JSON, extrae los datos y los guarda en un archivo CSV con los encabezados de columna correspondientes.

## Requisitos

Para ejecutar este script, necesitarás tener instalado Python en tu sistema. También necesitarás tener los siguientes módulos de Python instalados:

- `csv`: Módulo estándar de Python para trabajar con archivos CSV.
- `json`: Módulo estándar de Python para trabajar con datos en formato JSON.

Puedes instalar los módulos faltantes usando el administrador de paquetes `pip`. Ejecuta el siguiente comando en tu terminal para instalarlos:

```
pip install csv json
```

## Uso

1. Coloca el archivo JSON que deseas convertir en la misma carpeta que este script.
2. Ejecuta el script proporcionando la ruta del archivo JSON y la ruta del archivo CSV resultante. Por ejemplo:

```shell
python convertir.py
```

3. Se te pedirá que ingreses la ruta del archivo JSON y la ruta del archivo CSV. Proporciona las rutas correspondientes y presiona Enter.
4. El script convertirá los datos del archivo JSON al formato CSV y guardará el archivo CSV en la ubicación especificada.

Ten en cuenta que el archivo CSV resultante tendrá los mismos nombres de columna que las claves en el archivo JSON.

¡Eso es todo! Ahora puedes convertir fácilmente datos en formato JSON a archivos CSV utilizando este script de Python.

## Notas

- Asegúrate de tener los permisos adecuados para leer el archivo JSON y escribir en el archivo CSV.
- Si el archivo CSV ya existe en la ruta especificada, se sobrescribirá sin previo aviso.

Si tienes alguna pregunta o problema, no dudes en crear un problema en este repositorio.

¡Espero que encuentres útil este script!
