# Instrucciones

### Levantar ambiente

Este trabajo está desarrollado con Docker Compose. Para levantar el ambiente primero hay que construir las imágenes con:

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

Para testear es necesario primero tener corriendo los contenedores con `make up`. Una vez teniendo eso, y dependiendo el sistema operativo se pueden correr los tests unitarios y con Selenium de la forma:

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