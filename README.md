# Pokemons.
### Aspectos Tenicos.
- Para la modelación de datos se usó [Python](https://docs.python.org/3/).
- Para almacenar los datos se usó [MySQL](https://dev.mysql.com/doc/).

## Descripción


Construir un modelamiento de datos que consuma la API de [Pokemons](https://pokeapi.co/); guardar informacion de interés en una base de datos SQL (imagen oficial, habilidades, estadísticas generales) para luego realizar consultas que responda a preguntas planteadas en la prueba, para finalmente generar un archivo .CSV con los resultados.

## Índice 

- [Preparacion](#Preparacion)
- [Instalación](#instalación)
- [Uso](#uso)

## Preparacion
- Instalar Docker y Docker Compose en su sistema local siguiendo las instrucciones proporcionadas en la   [documentación oficial de Docker ](https://docs.docker.com/) o puedes ver este [video tutorial](https://www.faztweb.com/contenido/doker-desktop-windows) .
- Instalar un editor de código. [Visual Studio Code](https://code.visualstudio.com).
- Tener una cuenta de usuario en [GitHub](https://github.com/).

## Instalación

- Inicie sesión en github e ingrese al siguiente repositorio público. [Inventory](https://github.com/estiven199/pokemons).
- Obtenga la url del repositorio dando click en el botron verde (<> Code ),  en la opcion HTTPS.
- Clone el repositorio en su máquina.  [Siga estos pasos ](https://learn.microsoft.com/es-es/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette).
- Luego de clonar el repositorio, abra una terminal integrade dentro de Visual Studio Code.  Para esto seleccione `Ver>Terminal` en el menú principal.
- Ejecuta los siguientes comandos para crear las imágenes y contenedores necesarios en Docker.
> Nota: Asegúrese de que Docker se está Ejecutando.

```sh
docker compose build "Construye las imágenes de Docker que se especifican en el archivo docker-compose.yml"
docker compose up  "Crea y ejecuta los contenedores de un proyecto a partir de las imágenes de Docker"
```

## Uso
- Una vez creado los contendores de Docker, abrir otra terminal en Visual Studio Code y ejecutar el comando `main.py`, y con esto se ejecutara todo el código.