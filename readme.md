Como automatizar el script `main.py` ubicado en `/ruta-del-script/` en Mac OS:

1. Abre una terminal.

2. Ejecuta el comando `crontab -e` para abrir el archivo de tareas `cron`.

3. Agrega la siguiente línea al archivo `cron`, reemplazando `/ruta-del-script/main.py` con la ruta completa al script de Python que deseas ejecutar:

```
29 11 * * 1-5 /usr/bin/python3 /ruta-del-script/main.py
```

Esta línea especifica que se debe ejecutar el comando `/usr/bin/python3 /ruta-del-script/main.py` todos los días de la semana de lunes a viernes a las 11:29.

4. Guarda y cierra el archivo `cron`.

Una vez que hayas seguido estos pasos, el script `main.py` se ejecutará automáticamente a las 11:29 de lunes a viernes.

Para detener la tarea en algún momento, ejecuta el comando `crontab -e` de nuevo, elimina la línea que acabas de agregar, guarda y cierra el archivo `cron`.

¡Eso es todo!
