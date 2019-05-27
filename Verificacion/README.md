# Práctica Final
Repositorio para la práctica final de la asignatura.

## Autores
<a href="https://github.com/pablogrubio">Pablo García Rubio</a><br>
<a href="https://github.com/AlphaQueens">Álvaro Reina Abascal</a><br>
<a href="https://github.com/steelXz">Alfonso Barrena Romero</a><br>

## Funcionalidad
Página web sencilla que nos permite introducir por pantalla el nombre de un usuario de twitter y nos devuelve una lista con las 10 palabras más utilizadas en los últimos 7 días de sus tweets y respuestas, la frecuencia con la que aparecen y una lista con los tweets donde aparece esa palabra.

## Instrucciones de instalación
1. Clonar el repositorio git.
2. Instalar las librerias listadas en <a href=https://github.com/pablogrubio/PracticaFinalVerificacion/blob/master/Verificacion/requirements.txt">requirements.txt</a>

## Instrucciones para ejecutar el servidor
1. Abrir la consola de comandos.
2. Situarse en la ruta: <i><localizaciónProyecto\Verificación></i>.
3. Ejecutar el siguiente comando para correr el servidor:
    ```
    <ruta> python manage.py runserver
    ```
4. Abrir en el navegador la dirección: http://127.0.0.1:8000/
        
## Instrucciones para ejecutar los tests unitarios
1. Una vez corriendo el servidor, abrir otra consola de comandos.
2. Situarse en la ruta: <i><localizaciónProyecto\Verificación></i>.
3. Ejecutar el siguiente comando para ejecutar los tests realizados hasta ahora:
    ```
    <ruta> python manage.py test
    ```
   
## Instrucciones para ejecutar los tests funcionales (BDD + Selenium)
1. Una vez corriendo el servidor, abrir otra consola de comandos.
2. Situarse en la ruta: <i><localizaciónProyecto\Verificación></i>.
3. Ejecutar el siguiente comando para ejecutar los tests de Selenium:
    ```
    <ruta> python manage.py behave
    ```
        
NOTA: En caso de ejecutar el comando y aparecer el siguiente error: <i>'geckodriver' executable needs to be in PATH</i>. Debemos hacer lo siguiente:
- Copiar la ruta: <i><localizaciónProyecto\Verificacion\geckodriver></i> y añadirla al "Path" en nuestras "Variables del Sistema" de nuestro PC y reiniciarlo.
- Si persiste el error, deberá abrir los ficheros: <i>test_auto_web.py</i> y <i>environment.py</i>, y en las líneas 12 y 4 (respectivamente), sustituir el path existente por: <i><localizaciónProyecto\Verificacion\geckodriver\geckodriver.exe></i>.
