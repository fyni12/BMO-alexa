# Ejercucion en windows

crear el venv

``` bash
python -m venv .venv
```

luego para activar el venv

```bash
.\.venv\Scripts\Activate.ps1
```



# librerias

- uvicorn: servidor para ejecutar fastAPI
- fastAPI: framework para la creacion de la api
- httpx: para hacer peticiones http
- pydantic: para validacion de datos (un poco opcional)

# Ejecucion
para ejecutar la aplicacion

```
python -m src.main
```


en caso de querer ejecutar su contenedor haremos

```
docker compose up
```