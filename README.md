# Proyecto Final - Leandro Exequiel Ruzicki

# Descripción

En este sitio la idea es que el usuario pueda ver los eventos deportivos a desarrollarse en la ciudad y en caso de interesarse por alguno, poder registrarse para recibir más detalles vía mail.

# Video demostración

https://drive.google.com/file/d/12DXCuqMUme46UfBuC9PBGGCf_rS88VgD/view?usp=drive_link

# Ingreso: admin

http://127.0.0.1:8000/admin/
usuario: admin
clave: 1234

# Urls activas - funcionalidades

http://127.0.0.1:8000 - vista principal.

Desde aquí accedemos a las demás funcionalidades. Además, se pueden observer la tarjetas con los eventos disponibles.

http://127.0.0.1:8000/about/ - "Acerca de mí"

Una breve presentación sobre mí.

http://127.0.0.1:8000/usuario/register/ - botón "Registrarse"

Vista en la cual el usuario puede darse de alta en la web.
Deberá completar obligatoriamente todos los campos para "Guardar"

    Botón "Inicio": me devuelve a la página principal.

http://127.0.0.1:8000/usuario/login/ - botón "Iniciar sesión"

Si ya estaba registrado, deberá identificarse en ésta sección con usuario y contraseña.
Una vez validado, lo llevará a la web principal.

Una vez iniciado, tendrá la opción de utilizar el botón "Cerrar sesión" (http://127.0.0.1:8000/usuario/logout/)
mostrando el mensaje "Has cerrado sesión".

http://127.0.0.1:8000/lista/buscar/ - botón "Buscar"

Incluído en la vista principal, el cual permite filtrar por nombre del evento.
Se puede filtrar por una fracción de la palabra a buscar o bien, el nombre completo del evento.
    Botón "Inicio": me devuelve a la página principal.
El resultado se mostrará en otra vista con la posibilidad de hacer clic en el botón "Ver más detalles"(http://127.0.0.1:8000/evento/detalle/"id del evento"), el cual llevará al usuario a otra vista que mostrará una descripción más completa del evento.
Allí mismo tendrá la posiblidad de hacer clic en el botón "Me interesa" confirmado su registro al evento en la base de datos o en "Ya no me interesa" en el caso que quiera darse de baja en la suscripción.
A su vez, tendrá la opción de regresar a la web principal con el botón "Volver"

Vista de admin:
    Tiene habilitadas todas las opciones mencionadas anteriormente y además:

    Botón desplegable "Administrar eventos":

        http://127.0.0.1:8000/crear_evento/ - botón "Registrar Evento".
            Botón "Añadir" - http://127.0.0.1:8000/evento/crear_evento/
            Registro de eventos. Formulario para dar de alta un nuevo evento en la base de datos.
            Deberá completar: título, descripción, fecha, categoría (seleccionar una opción) y subir una imagen para la tarjeta.
            Confirmará con el botón "Guardar".

        http://127.0.0.1:8000/evento/lista_categorias/ - botón "Listar categorías"
            Simplemente generará una lista de todas las categorías existentes en la base de datos
            y los eventos relacionados a cada una.
            Tendrá las opciones de:
                Actualizar: podrá modificar los campos mencionados en el registro del evento.
                Eliminar: tendrá la opción de borrar definitivamente el evento con un mensaje de confirmación.

        http://127.0.0.1:8000/registro/lista_usuarios_eventos/ - botón "Listar registros"
            Generará una lista por cada usuario y, dentro de los mismos, mostrará todos los eventos a los que se registraron.
            Tendrá la opción de eliminar el registro si lo desea.
        
        http://127.0.0.1:8000/admin/ - botón "Panel de administración"
            Simplemente es otra forma de ingresar al panel del administrador.
