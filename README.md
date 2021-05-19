
# Dunder API

Dunder API es un API RESTful escrito en python utlizando Flask y SQLAlchemy como base, es un proyecto divertido y meramente académico para aplicar distintas prácticas, patrones de diseño y ampliar mi conocimiento de herramientas que pueden servir para el próximo reto utilizando python.

## Requisitos
El proyecto requiere de algunas dependencias del sistema, una vez cumplidas el resto de requerimientos se cumple utilizando el archivo **requirements.txt**

 - Python 3.7+
 - [Pip](https://pip.pypa.io/en/stable/)
 - [Venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Instalación

Clonar repo
```bash
git clone git@github.com:garaekz/dunder-api.git
```

Entramos a la carpeta del repo clonado
```bash
cd dunder-api
```

Inicializamos nuestro nuestro ambiente virtual, el siguiente código creará una carpeta en el path en el que nos encontremos actualmente (en éste caso dentro de la carpeta del proyecto clonado)
```bash
python -m venv venv
```

Activamos nuestro ambiente virtual según el tipo de sistema en el que estemos
```bash
source venv/bin/activate # En plataformas POSIX
source venv/Scripts/activate # En sistemas Windows
```

Instalamos nuestras dependencias utilizando [pip](https://pip.pypa.io/en/stable/)

```bash
pip install -r requirements.txt
```

Debes asegurarte de renombrar el archivo **.env.example** a solamente **.env** y modificarlo:

```bash
DEBUG=True  #Quitar esta linea para deshabilitar modo debug
PORT=8080 # El puerto que desees utilizar para correr el servicio
DSN="mysql://user:pass@localhost/db"  # DSN string de tu preferencia
```
En el ejemplo **mysql** es el tipo de DB, **user** es el nombre de usuario que utilizará la conexión, **pass** es la contraseña correspondiente al usuario y **db** es el nombre de la base de datos o schema.

El siguiente paso no funciona con SQLite, ejecutamos las migraciones en la DB que establecimos con el DSN en el paso anterior.
```bash
flask db upgrade
```

## Uso

Lo ejecutamos directamente
```python
python -m run
```

## Pendientes
Terminar el README con un roadmap, crear CHANGELOG y explicar los endpoints disponibles actualmente
