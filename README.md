# Instrucciones

### Levantar ambiente

Este trabajo está desarrollado con Docker Compose. Para levantar el ambiente primero se sugiere descargar el repo de la siguiente forma:

```
git clone https://github.com/DevOps-Usach-Group-3/TrabajoFinalM4SWD.git && cd TrabajoFinalM4SWD 
```

Posteriormente construir las imágenes (dentro de la carpeta TrabajoFinalM4SWD) con:

```
make build
```

Luego, si todo salió bien el ambiente se levanta con

```
make up
```

Nota: esto dejará 2 contenedores corriendo en background `back` y `front`.

Por último ir a http://localhost:8000/retiro para probar la app.


### Testear

Para testear es necesario primero tener corriendo los contenedores corriendo con `make up`.  Dependiendo el sistema operativo se pueden correr los tests unitarios y con Selenium según:

##### Windows

```
make test-windows
```

##### Linux

```
make test-linux
```

##### Mac

```
make test-mac
```