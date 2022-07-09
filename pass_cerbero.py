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
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import json
import subprocess
import pyzipper
import os

# funciones
def abrirFich(plista, ppwlista):    
    try:
        with pyzipper.AESZipFile(dir_base + "fich_acclista_"+plista+".zip") as zip_ref:            
            zip_ref.setpassword(bytes(ppwlista,'utf-8'))            
            zip_ref.extract("fich_acclista_"+plista+".txt",dir_base,bytes(ppwlista,'utf-8'))
            return 0
            
    except:
        print("xxxxxxxxxxxxx An exception occurred extracting with Python ZipFile library.")        
        tkinter.messagebox.showwarning(parent=frm1,title="P A S S   C E R B E R O  -  Lectura fichero " + plista,  message="Excepción ocurrida extrayendo fichero del zip ")
        return 1
# fin abrirFich
        
def creaVacia():
    plista = txt_lista.get()
    ppwlista = txt_pswlista.get()

    if plista == "":
       tkinter.messagebox.showwarning(parent=frm1,title="P A S S   C E R B E R O  -  Crear lista vacía",  message="Error, no se ha indicado ningún nombre para la nueva lista")

    else:
        if ppwlista == "":
            tkinter.messagebox.showwarning(parent=frm1,title="P A S S   C E R B E R O  -  Crear lista vacía",  message="Error, no se ha indicado ninguna contraseña para la nueva lista")
        else:          
            with open(dir_base + "fich_acclista_"+plista+".txt", "w") as f:
                f.write('[]')
                f.close()

            with pyzipper.AESZipFile(dir_base + "fich_acclista_"+plista+".zip",'w',compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
                zf.setpassword(bytes(ppwlista,'utf-8'))
                zf.write(dir_base + "fich_acclista_"+plista+".txt","fich_acclista_"+plista+".txt")

            os.remove(dir_base + "fich_acclista_"+plista+".txt")
            tkinter.messagebox.showinfo(parent=frm1, title="P A S S   C E R B E R O  -  Crear lista vacía",  message="Lista vacía creada para " + plista)
# fin creaVacia
    
def readUsers2(pfich):
    try:       
        with open(pfich,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
# fin readUsers2
    
def readUsers():
    def writeUsers(usr, plista,ppwlista):
        with open(dir_base + "fich_acclista_"+plista+".txt", "w") as f:
            json.dump(usr, f)
            f.close()
        with pyzipper.AESZipFile(dir_base + "fich_acclista_"+plista+".zip",'w',compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(bytes(ppwlista,'utf-8'))
            zf.write(dir_base + "fich_acclista_"+plista+".txt","fich_acclista_"+plista+".txt")
        os.remove(dir_base + "fich_acclista_"+plista+".txt")
        tkinter.messagebox.showinfo(parent=frm1, title="P A S S   C E R B E R O  -  Escribir fichero",  message="Fichero guardado para " + plista)
    # fin writeUsers

    ######################################
    # ALTA ACCESO
    ######################################
    def altaAcceso():
        encontrado = False
        vacceso = txt_acceso.get()

        for i in range(len(varray)):
            if varray[i]["acceso"] == vacceso:
                encontrado=True
                break

        if encontrado == True:
            tkinter.messagebox.showwarning(parent=winacc,title="P A S S   C E R B E R O  -  Alta acceso",  message="Error, código de acceso ya dado de alta")        
        else:
            vusuario=txt_user.get()
            vpsw=txt_psw.get()
            vdesc=txt_desc.get()
            vurl=txt_url.get()

            vreg = dict()
            vreg["acceso"] = vacceso
            vreg["usuario"] = vusuario
            vreg["psw"] = vpsw
            vreg["desc"] = vdesc
            vreg["url"] = vurl

            varray.append(vreg)

            tkinter.messagebox.showinfo(parent=winacc, title="P A S S   C E R B E R O  -  Alta acceso",  message="Acceso registrado. Pendiente de grabar en fichero al salir.")

            txt_acceso.set('')
            txt_user.set('')
            txt_psw.set('')
            txt_desc.set('')
            txt_url.set('')
            listbox.insert("end", vacceso)
    # fin altaAcceso

    def bajaAcceso():
          vacceso = txt_acceso.get()

          if vacceso == "":
              tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Baja acceso",  message="Error, no se ha especificado ningún acceso")
          else:          
              encontrado=False
          
              for i in range(len(varray)):
                  if varray[i]["acceso"] == vacceso:
                      varray.pop(i)
                      encontrado=True
                      for j in range(listbox.size()):
                          if listbox.get(j) == vacceso:
                              listbox.activate(j)
                              listbox.delete(j)
                              break
                      break

              if encontrado == False:
                  tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Baja acceso",  message="Error, código de acceso a dar de baja no encontrado")
    # fin bajaAcceso

    def modificaAcceso():
          vacceso = txt_acceso.get()
          if vacceso == "":
              tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Modificar acceso",  message="Error, no se ha especificado ningún acceso")
          else:
              encontrado=False
          
              for i in range(len(varray)):
                  if varray[i]["acceso"] == vacceso:
                      varray[i]["usuario"] = txt_user.get()
                      varray[i]["psw"] = txt_psw.get()
                      varray[i]["desc"] = txt_desc.get()
                      varray[i]["url"] = txt_url.get()
                      encontrado=True
                      tkinter.messagebox.showinfo(parent=winacc, title="P A S S   C E R B E R O  -  Modificar acceso",  message="Acceso modificado. Pendiente de grabar en fichero al salir.")
                      break

              if encontrado == False:
                  tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Modificar acceso",  message="Error, código de acceso a modificar no encontrado")
    # fin modificaAcceso

    def consultaAcceso():
        if listbox.size() == 0:
            tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Consulta acceso", message="No hay accesos en lista")
        else:
            if listbox.curselection() == ():
                tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Consulta acceso", message="Ningún acceso seleccionado")
            else:
                vacceso = listbox.get(listbox.curselection())
                encontrado = False
                for i in range(len(varray)):
                    if varray[i]["acceso"] == vacceso:
                        txt_acceso.set(varray[i]["acceso"])
                        txt_user.set(varray[i]["usuario"])
                        txt_psw.set(varray[i]["psw"])
                        txt_desc.set(varray[i]["desc"])
                        txt_url.set(varray[i]["url"])
                        encontrado = True
                        tbox_acceso.focus_set()
                        break

                if not encontrado:
                    tkinter.messagebox.showwarning(parent=winacc, title="P A S S   C E R B E R O  -  Consulta acceso",message="Acceso " + vacceso + " no encontrado ")
    # fin consultaAcceso

    def salirGuardar():
        writeUsers(varray,plista,ppwlista)
        winacc.destroy()
    # fin salirGuardar

    def salirNoGuardar():
        if os.path.exists(dir_base + "fich_acclista_"+plista+".txt"):
           os.remove(dir_base + "fich_acclista_"+plista+".txt")
        winacc.destroy()
    # fin salirNoGuardar

    #######  inicio chicha readUsers   #####
    plista = txt_lista.get()
    ppwlista = txt_pswlista.get()
    #destinationDirectory = "C:\MANU\ROOT\ACCLISTA\\"
    
    hayErr = abrirFich(plista,ppwlista)

    #print("Error abrirFich::: " + str(hayErr))

    if hayErr == 0:
        #print("fichero a leer::: " + dir_base + "fich_acclista_"+plista+".txt")
        varray = []
        varray = readUsers2(dir_base + "fich_acclista_"+plista+".txt")

        varray.sort(key=lambda s: s['acceso'])
        #if len(varray) > 0:
        #    print("primer elemento::: " + varray[0]["acceso"])

        winacc=tk.Toplevel(root)
        winacc.title("P A S S    C E R B E R O  -  Lista accesos " + plista)

        frm2 = ttk.Frame(winacc, padding=10)
        frm2.grid()
        frm3 = ttk.Frame(winacc, padding=10)
        frm3.grid()
        txt_acceso = tk.StringVar()
        txt_user = tk.StringVar()
        txt_psw = tk.StringVar()
        txt_desc = tk.StringVar()
        txt_url = tk.StringVar()

        # FRAME 2 Label ACCESO
        ttk.Label(frm2, text ="Nombre acceso").grid(column=0, row=0)  
        tbox_acceso = ttk.Entry(frm2, textvariable=txt_acceso, width=40)
        tbox_acceso.grid(column=1, row=0)
        tbox_acceso.focus_set()

        # FRAME 2 Label DESCRIPCION
        ttk.Label(frm2, text ="Descripción acceso").grid(column=2, row=0)  
        tbox_desc = ttk.Entry(frm2, textvariable=txt_desc, width=40)
        tbox_desc.grid(column=3, row=0)

        # FRAME 2 Label URL
        ttk.Label(frm2, text ="URL (opcional)").grid(column=0, row=1)  
        tbox_url = ttk.Entry(frm2, textvariable=txt_url, width=40)
        tbox_url.grid(column=1, row=1)

        # FRAME 2 Label USUARIO
        ttk.Label(frm2, text ="USUARIO").grid(column=0, row=2)  
        tbox_user = ttk.Entry(frm2, textvariable=txt_user, width=40)
        tbox_user.grid(column=1, row=2)

        # FRAME 2 Label PASSWORD
        ttk.Label(frm2, text ="CONTRASEÑA").grid(column=2, row=2)  
        tbox_psw = ttk.Entry(frm2, textvariable=txt_psw, width=40)
        tbox_psw.grid(column=3, row=2)

        # FRAME 2 Botones alta, baja, modificación    
        ttk.Button(frm2, text="Alta Acceso", command=altaAcceso).grid(column=0, row=3)
        ttk.Button(frm2, text="Baja Acceso", command=bajaAcceso).grid(column=1, row=3)
        ttk.Button(frm2, text="Modificar Acceso", command=modificaAcceso).grid(column=2, row=3)

        # FRAME 3 Lista accesos
        vArrAccesos = []
        numAccesos = 1
        if len(varray) > 1:    
            for i in range(len(varray)):      
                vArrAccesos.append(varray[i]["acceso"])
                numAccesos = numAccesos + 1

        vAccesos_var = tk.StringVar(value=vArrAccesos)

        ttk.Label(frm3, text ="LISTA ACCESOS").grid(column=0, row=5)
        listbox = tk.Listbox(
			  frm3,
			  listvariable=vAccesos_var,
			  height=30,
			  selectmode='browse')
        listbox.grid(column=0, row=6)
        listbox.bind('<Double-Button-1>', lambda x: consultaAcceso())

        # FRAME 3 Botón consulta detalle acceso
        ttk.Button(frm3, text="Consultar\nAcceso", command=consultaAcceso).grid(column=1, row=6)

        # FRAME 3 Botones de salida    
        ttk.Button(frm3, text="Guardar Lista y salir", command=salirGuardar).grid(column=2, row=7)
        ttk.Button(frm3, text="Salir sin guardar", command=salirNoGuardar).grid(column=3, row=7)
        
        winacc.mainloop()
# fin readUsers
    
############# comienzo chicha  #############################
root = tk.Tk()
root.title("P A S S     C E R B E R O")
frm1 = ttk.Frame(root, padding=10)
frm1.grid()
txt_lista = tk.StringVar()
txt_pswlista = tk.StringVar()
dir_base = os.environ['USERPROFILE'] + "\\"


# FRAME 1 Label NOMBRE LISTA
ttk.Label(frm1, text ="Nombre Lista contraseñas").grid(column=0, row=0)  
tbox_lista = ttk.Entry(frm1, textvariable=txt_lista)
tbox_lista.grid(column=1, row=0)
tbox_lista.focus_set()

# FRAME 1 Label Contraseña lista
ttk.Label(frm1, text ="Contraseña lista").grid(column=0, row=11)  
tbox_pswlista = ttk.Entry(frm1, textvariable=txt_pswlista, show='*')
tbox_pswlista.grid(column=1, row=11)

# FRAME 1 Botón leer LISTA
mibotonLeer=ttk.Button(frm1, text="Leer Lista", command=readUsers).grid(column=2, row=0)
mibotonListaVac=ttk.Button(frm1, text="Nueva Lista", command=creaVacia).grid(column=2, row=11)
mibotonSalir=ttk.Button(frm1, text="Salir", command=root.destroy).grid(column=2, row=22)

root.mainloop()

