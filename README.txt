# ######################################################################################################################################################
# ######################################################################################################################################################
#
# APLICACIÓN/APPLICATION:    pass_cerbero
#
# LENGUAJE/LANGUAGE:         PYTHON 3.10.4 & TKINTER GUI
#
# VERSIÓN/VERSION:           1.0
#
# FECHA/DATE:                09/07/2022
#
# AUTOR/AUTHOR:              MANU SALGUEIRO
#
# LICENCIA/LICENSE:          OPEN SOURCE - MIT
#
# SINOPSIS:      UTILIDAD PARA MANTENIMIENTO Y GUARDADO DE CONTRASEÑAS EN FICHERO JSON COMPRIMIDO CON CONTRASEÑA EN RUTA %USERPROFILE% (c:\usuarios...)
#
# SYNOPSIS:      TOOL FOR MAINTENANCE AND SAVING OF PASSWORD ACCESSES IN PASSWORD PROTECTED COMPRESSED FILE IN PATH %USERPROFILE% (c:\users....)
#
# DETALLE:       PANTALLA INICIAL - BOTÓN NUEVA LISTA - PARA CREAR UNA NUEVA LISTA DE ACCESOS. SE DEBE INDICAR LA CONTRASEÑA PARA EL FICHERO
#                                                       COMPRIMIDO QUE SE CREARÁ CON LA LISTA DE ACCESOS.
#                                 - BOTÓN LEER LISTA  - PARA LEER UN FICHERO COMPRIMIDO DE ACCESOS CREADO PREVIAMENTE. SE DEBE INDICAR LA
#                                                       CONTRASEÑA DEL FICHERO COMPRIMIDO (LA QUE SE INDICÓ AL CREAR LA LISTA).
#                PANTALLA LISTA DE ACCESOS:
#                    CONTIENE LOS CAMPOS NECESARIOS PARA REGISTRAR LOS ACCESOS QUE SE QUIERAN GUARDAR EN LA LISTA DE ACCESOS Y BOTONES PARA
#                    CONSULTARLOS, DARLOS DE ALTA, DARLOS DE BAJA O MODIFICARLOS.
#                    CAMPOS:
#                      NOMBRE DE ACCESO:  NOMBRE IDENTIFICATIVO DEL ACCESO  (EJ: USUARIO_AMAZON)
#                      DESCRIPCIÓN ACCESO: DESCRIPCIÓN DETALLADA DEL ACCESO  (EJ: USUARIO PARA HACER COMPRAS EN AMAZON)
#                      URL (OPCIONAL):   URL RELACIONADA CON EL ACCESO  (EJ: https://www.amazon.es)
#                      USUARIO:  USUARIO RELACIONADO CON EL ACCESO   (EJ: <MIusuariodeamazon>@gmail.com)
#                      CONTRASEÑA:  CONTRASEÑA RELACIONADA CON EL ACCESO  (EJ:  Mip@sswordDe@mazon)
#                      LISTA ACCESOS:  MUESTRA LA LISTA DE ACCESOS DEL FICHERO COMPRIMIDO
#                    BOTONES:
#                      ALTA ACCESO: PARA DAR DE ALTA EL ACCESO. SI YA EXISTE UNO CON EL NOMBRE INDICADO EL ALTA FALLARÁ.
#                      BAJA ACCESO: PARA BORRAR UN ACCESO. SE BORRARÁ DE LA LISTA EL ACCESO QUE SE HAYA INDICADO EN EL CAMPO NOMBRE.
#                      MODIFICAR ACCESO: PARA MODIFICAR UN ACCESO. SE MODIFICARÁN LOS DATOS DEL ACCESO SEGÚN LO QUE HAYA INDICADO EN LOS CAMPOS
#                      CONSULTAR ACCESO: PARA MOSTRAR LOS DATOS DEL ACCESO QUE SE SELECCIONE EN LA LISTA
#                      GUARDAR LISTA Y SALIR:  GUARDA LA LISTA DE ACCESOS EN EL FICHERO COMPRIMIDO PROTEGIDO CON CONTRASEÑA Y SALE DE LA VENTANA
#                      SALIR SIN GUARDAR: SALE DE LA VENTANA SIN GUARDAR LOS CAMBIOS QUE SE HAYAN HECHO EN LOS ACCESOS.
#
# DETAIL:        INITIAL WINDOW - NEW LIST BUTTON (NUEVA LISTA) - ALLOWS TO CREATE A NEW ACCESS LIST. A PASSWORD MUST BE ENTERED FOR THE PASSWORD
#                                                                 PROTECTED FILE THAT WILL CONTAIL THE ACCESS LIST.
#                               - READ LIST BUTTON (LEER LISTA) - ALLOWS TO READ A COMPRESSED FILE WITH A LIST OF ACCESSES PREVIOUSLY CREATED. THE
#                                                                 PASSWORD OF THE PASSWORD PROTECTED FILE MUST BE ENTERED (THE ONE INDICATED WHEN
#                                                                 CREATING THE LIST)
#                 ACCESS LIST WINDOW:
#                     IT CONTAINS THE NECESSARY FIELDS TO RECORD THE ACCESSES REQUIRED IN THE ACCESS LIST AND CONTAINS BUTTONS TO QUERY, INSERT,
#                     DELETE AND UPDATE THEM.
#                     FIELDS:
#                        NOMBRE DE ACCESO (ACCESS NAME):  ID NAME OF THE ACCESS (EX: AMAZON_USER)
#                        DESCRIPCIÓN ACCESO (ACCESS DESCRIPTION):  DETAILED DESCRIPTION OF THE ACCESS (EX: USER TO BUY IN AMAZON WEB PAGE)
#                        URL (OPTIONAL):  ACCESS RELATED URL  (EX: https://www.amazon.com)
#                        USUARIO (USER): ACCESS RELATED USER  (EX: <myAmazonUser>@gmail.com)
#                        CONTRASEÑA (PASSWORD):  ACCESS RELATED PASSWORD  (EX: My@mazonp@assword)
#                        LISTA ACCESOS (ACCESS LIST):  IT SHOWS DE ACCESS LIST CONTAINED IN THE PASSWORD PROTECTED FILE
#                     BUTTONS:
#                        ALTA ACCESO (ACCESS INSERT):  TO INSERT A NEW ACCESS. IF THE NAME ALREADY EXISTS IN THE LIST DE INSERT WILL FAIL.
#                        BAJA ACCESO (ACCESS DELETE):  TO DELETE AN EXISTING ACCESS. THE ACCESS WITH THE INDICATED NAME WILL BE ERASED FROM THE LIST
#                        MODIFICAR ACCESO (ACCESS UPDATE):  TO UPDATE AN EXISTING ACCESS WITH THE INFORMATION POPULATED IN THE DIFFERENT FIELDS.
#                        CONSULTAR ACCESO (ACCESS QUERY): TO SHOW THE ACCESS DATA OF THE SELECTED ACCESS IN THE DIFFERENT FIELDS OF THE WINDOW.
#                        GUARDAR LISTA Y SALIR (SAVE LIST AND EXIT):  SAVES THE ACCESS LIST IN THE PASSWORD PROTECTED COMPRESSED FILE AND EXITS.
#                        SALIR SIN GUARDAR (EXIT WITHOUT SAVING):  EXITS THE WINDOWS WITHOUT SAVING ANY CHANGE.
#                      
#                   
# RUTA CON EL/LOS FICHERO/S CON LA/S LISTA/S DE ACCESOS:  C:\USUARIOS\<nombre_usuario_windows>
# NOMBRE DE EL/LOS FICHERO/S CON LA/S LISTA/S DE ACCESOS: fich_acclista_<nombre dado a la lista>.zip  <- fichero zip con contraseña
#
# PATH OF THE FILE/S WITH THE ACCES LIST/S:  C:\USERS\<windows_user_name>
# NAME OF THE FILE/S WITH DE ACCESS LIST/S:  fich_acclista_<name_given_to_the_list>.zip <- password protected zip file
# 
#
# ######################################################################################################################################################
# ######################################################################################################################################################
