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
python -m src.main --host 0.0.0.0 --port 8000
```


en caso de querer ejecutar su contenedor haremos

```
docker compose up -d --build
```


# Despliegue local

para realizar un despliegue local es necesario abrir un puerto 
abrir el puerto

```
 New-NetFirewallRule -DisplayName "FastAPI Docker 8000" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow


#solo para red privada (creo)
 Set-NetFirewallRule -DisplayName "FastAPI Docker 8000" -RemoteAddress "192.168.137.0/24"
```

cerrar el puerto
```
Remove-NetFirewallRule -DisplayName "FastAPI Docker 8000"
```