import tkinter as tk
from tkinter import messagebox
import os
import sys
import docker
import subprocess
from tkinter import ttk 
from tkinter import PhotoImage
# Conexxion al contenedor docker
client = docker.from_env()

# Obtener el contenedor por nombre o ID
try:
    contenedor = client.containers.get("server")
except docker.errors.NotFound:
    contenedor = None
    print("⚠️ Contenedor 'server' no encontrado.")

# Mostrar el estado de los contenedores
def bytes_a_mb(bytes_):
    return round(bytes_ / 1024 / 1024, 2)
def obtener_datos_contenedores():
    datos = []
    for contenedor in client.containers.list(all=True):
        nombre = contenedor.name
        estado = contenedor.status
        try:
            stats = contenedor.stats(stream=False)
            cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
            system_cpu_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]
            num_cpus = len(stats["cpu_stats"]["cpu_usage"].get("percpu_usage", [])) or 1
            cpu_percent = (cpu_delta / system_cpu_delta) * num_cpus * 100 if system_cpu_delta > 0 else 0

            mem_usage = stats["memory_stats"]["usage"]
            mem_limit = stats["memory_stats"]["limit"]
            ram_percent = (mem_usage / mem_limit) * 100 if mem_limit else 0
            memoria_str = f"{bytes_a_mb(mem_usage)} / {bytes_a_mb(mem_limit)}"
        except Exception:
            cpu_percent = 0
            ram_percent = 0
            memoria_str = "N/A"

        datos.append((nombre, estado, f"{cpu_percent:.2f}", memoria_str, f"{ram_percent:.2f}"))
    return datos

def actualizar_monitor():
    # Borrar filas actuales
    for item in tree_monitor.get_children():
        tree_monitor.delete(item)

    # Insertar datos nuevos
    for fila in obtener_datos_contenedores():
        tree_monitor.insert("", "end", values=fila)

def mostrar_monitor():
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_monitor.pack(fill=tk.BOTH, expand=True)
    actualizar_monitor()
    frame_monitor.after(1000, actualizar_monitor)
# Funcion para cambiar el valor del dominio
dominio_w = os.path.join('ejecutables', 'dominio.txt')
def escribir_valor(nuevo_valor, archivo=dominio_w):
    with open(archivo, 'w') as f:  # 'w' sobreescribe el archivo
        f.write(str(nuevo_valor))
    print(f"Se escribió '{nuevo_valor}' en {archivo}")


# Ejemplo de uso

# Control de entorno de grafana
def encender_grafana():
    encender_grafana = os.path.join('ejecutables', 'encender_grafana.sh')
    subprocess.run(['bash', encender_grafana])
    python = sys.executable
    os.execl(python, python, *sys.argv)
def apagar_grafana():
    apagar_grafana = os.path.join('ejecutables', 'apagar_grafana.sh')
    subprocess.run(['bash', apagar_grafana])

# Funcion para encender entorno de desarrollo

def encender_entorno():
    encender_entorno = os.path.join('ejecutables', 'encender_entorno.sh')
    subprocess.run(['bash', encender_entorno])
    python = sys.executable
    os.execl(python, python, *sys.argv)

def apagar_entorno():
    apagar_entorno= os.path.join('ejecutables', 'apagar_entorno.sh')
    subprocess.run(['bash', apagar_entorno])


def mostrar_power():
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_power.pack(pady=10)

def mostrar_terminal():
    try:
        contenedor = client.containers.get("server")
        if contenedor.status != "running":
            messagebox.showinfo("Estado", "Contenedor 'server' está apagado")
            return
    except docker.errors.NotFound:
        messagebox.showinfo("Estado", "Contenedor 'server' no encontrado")
        return

    # Aquí va el código para mostrar la terminal
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_terminal.pack(fill=tk.BOTH, expand=True)

# 🔄 Reiniciar el script silenciosamente
def reinicio_api():
    python = sys.executable
    os.execl(python, python, *sys.argv)
# Funiones de la seccion DNS
def guardar_dns():
    # Variable del nombre de la pagina web
    web_name = entry_nombre.get()

    # Variables para modificar los ficheros
    # Variable para named.conf.local
    base_dir_1 = os.path.dirname(os.path.abspath(__file__))
    ruta_named = os.path.join(base_dir_1,'entornos', 'desarrollo_web','disco_duro', 'server_m', 'datos', 'bind', 'named.conf.local')
    # Variable para db.web
    base_dir_2 = os.path.dirname(os.path.abspath(__file__))
    ruta_web = os.path.join(base_dir_2,'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos', 'bind', 'db.web')
    # Variable para modificar apache2
    #http
    base_dir_3 = os.path.dirname(os.path.abspath(__file__))
    ruta_http = os.path.join(base_dir_3, 'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos', 'apache2', 'www.http.conf')
    #https
    base_dir_4 = os.path.dirname(os.path.abspath(__file__))
    ruta_https = os.path.join(base_dir_4,'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos', 'apache2', 'www.https.conf')
    # Funcion para modificar el fichero
    def modificar_dns():
        # Para modifificar named.conf.local
        with open(ruta_named, 'r') as named:
            contenido = named.read()
        contenido_modificado = contenido.replace(f'zone "" ', f'zone "{web_name}" ')
        with open(ruta_named, 'w') as named:
            named.write(contenido_modificado)
        # Para modificar db.web
        with open(ruta_web, 'r') as web:
            contenido = web.read()
        contenido_modificado = contenido.replace(f'. root..', f'{web_name}. root.{web_name}.')
        with open(ruta_web, 'w') as web:
            web.write(contenido_modificado)
    def modificar_apache2():
        # Para modifificar www.http.conf
        with open(ruta_http, 'r') as http:
            contenido = http.read()
        contenido_modificado = contenido.replace(f'www.', f'www.{web_name}')
        with open(ruta_http, 'w') as http:
            http.write(contenido_modificado)
        # Para modifificar www.https.conf
        with open(ruta_https, 'r') as https:
            contenido = https.read()
        contenido_modificado = contenido.replace(f'www.', f'www.{web_name}')
        with open(ruta_https, 'w') as http:
            http.write(contenido_modificado)

    def modificar_contenedor():
        contenedor.exec_run("cp datos/bind/named.conf.local /etc/bind")
        contenedor.exec_run("cp datos/bind/db.web /etc/bind")
        contenedor.exec_run("supervisorctl restart bind9")
        contenedor.exec_run("cp datos/apache2/www.http.conf /etc/apache2/sites-available")
        contenedor.exec_run("cp datos/apache2/www.https.conf /etc/apache2/sites-available")

    # Condicional para evitar tener valores nulos en el nombre de la web
    if web_name:
        messagebox.showinfo("Guardado", f"Nombre de la web guardado: {web_name}")
        entry_nombre.config(state='disabled')  # Bloquear campo
        modificar_dns()
        modificar_apache2()
        modificar_contenedor()
        escribir_valor(f"{web_name}")
        
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre de la web.")

def borrar_dns():
    web_name = entry_nombre.get()

    # Variables para modificar los ficheros
    # Variable para named.conf.local
    base_dir_1 = os.path.dirname(os.path.abspath(__file__))
    ruta_named = os.path.join(base_dir_1, 'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos',  'bind', 'named.conf.local')
    # Variable para db.web
    base_dir_2 = os.path.dirname(os.path.abspath(__file__))
    ruta_web = os.path.join(base_dir_2, 'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos',  'bind', 'db.web')
     # Variable para modificar apache2
    #http
    base_dir_3 = os.path.dirname(os.path.abspath(__file__))
    ruta_http = os.path.join(base_dir_3, 'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos', 'apache2', 'www.http.conf')
    #https
    base_dir_4 = os.path.dirname(os.path.abspath(__file__))
    ruta_https = os.path.join(base_dir_4, 'entornos', 'desarrollo_web', 'disco_duro', 'server_m', 'datos', 'apache2', 'www.https.conf')

    def modificar_apache2():
        cargar_valor()
        # Para modifificar www.http.conf
        with open(ruta_http, 'r') as http:
            contenido = http.read()
        contenido_modificado = contenido.replace(f'www.{web_name}', f'www.')
        with open(ruta_http, 'w') as http:
            http.write(contenido_modificado)
        # Para modifificar www.https.conf
        with open(ruta_https, 'r') as https:
            contenido = https.read()
        contenido_modificado = contenido.replace(f'www.{web_name}', f'www.')
        with open(ruta_https, 'w') as http:
            http.write(contenido_modificado)

    # Funcion para modificar el fichero
    def modificar_dns():
        cargar_valor()
        # Para modifificar named.conf.local
        with open(ruta_named, 'r') as named:
            contenido = named.read()
        contenido_modificado = contenido.replace(f'zone "{web_name}" ', f'zone "" ')
        with open(ruta_named, 'w') as named:
            named.write(contenido_modificado)
        # Para modificar db.web
        with open(ruta_web, 'r') as web:
            contenido = web.read()
        contenido_modificado = contenido.replace(f'{web_name}. root.{web_name}.', f'. root..')
        with open(ruta_web, 'w') as web:
            web.write(contenido_modificado)
           
    modificar_apache2()
    modificar_dns()
    var = ""
    escribir_valor(f"{var}")
    
    entry_nombre.config(state='normal')  # Desbloquear campo
    entry_nombre.delete(0, tk.END)
# Funciones para http y https
def activar_http():
        script_path = "/a_http.sh"
        command = f"bash {script_path}"
        contenedor.exec_run(command)
        btn_http.config(state="disabled")   # Desactiva boton1
        btn_https.config(state="normal")     # Activa boton2

def activar_https():
    script_path = "/a_https.sh"
    command = f"bash {script_path}"
    contenedor.exec_run(command)
    btn_http.config(state="normal")
    btn_https.config(state="disabled")
# Funciones de la barra de menú
def mostrar_todo():
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_dns.pack(pady=10)
    frame_http.pack(pady=10)

def mostrar_dns():
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_dns.pack(pady=10)

def mostrar_http():
    for widget in frame_contenedor.winfo_children():
        widget.pack_forget()
    frame_http.pack(pady=10)

def apagar():
    borrar_dns()
    root.quit()

def ayuda():
    ayuda = os.path.join('ejecutables', 'ayuda.txt')
    subprocess.Popen(['gedit', ayuda])

# Ventana principal
root = tk.Tk()
root.title("TOR")
root.geometry("300x300")
# Cargar un archivo de imagen como ícono
icono = PhotoImage(file="emoticono.png")  
root.iconphoto(True, icono)

# Variable para valor por defecto de dominio
var = tk.StringVar()
# Valor por defecto en el dominio

def cargar_valor():
    try:
        dominio_r = os.path.join('ejecutables', 'dominio.txt')
        with open(dominio_r, "r") as f:
            contenido = f.read().strip()  # Quita espacios y saltos
        var.set(contenido)
    except FileNotFoundError:
        var.set("")
# Llamamos a la funcion 
cargar_valor()
# Barra de menú
menu_bar = tk.Menu(root)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Todas", command=mostrar_todo)
menu_opciones.add_command(label="DNS", command=mostrar_dns)
menu_opciones.add_command(label="HTTP/HTTPS", command=mostrar_http)

menu_bar.add_cascade(label="Opciones", menu=menu_opciones)
menu_bar.add_command(label="Apagar/Encender", command=mostrar_power)
menu_bar.add_command(label="Terminal", command=mostrar_terminal)
menu_bar.add_command(label="Contenedores", command=mostrar_monitor)
menu_bar.add_command(label="Reiniciar", command=reinicio_api)
#menu_bar.add_command(label="Apagar", command=apagar)
menu_bar.add_command(label="Ayuda", command=ayuda)

root.config(menu=menu_bar)

# Contenedor para secciones
frame_contenedor = tk.Frame(root)
frame_contenedor.pack(fill=tk.BOTH, expand=True)

# --- Sección DNS ---
frame_dns = tk.Frame(frame_contenedor)

label_dns = tk.Label(frame_dns, text="DNS", font=("Arial", 14, "bold"))
label_dns.pack(pady=5)

frame_input = tk.Frame(frame_dns)
frame_input.pack()

label_nombre = tk.Label(frame_input, text="Nombre de la Web:")
label_nombre.pack(side=tk.LEFT)

entry_nombre = tk.Entry(frame_input, textvariable=var, width=20)
entry_nombre.pack(side=tk.LEFT, padx=5)

# Si ya tiene información, lo bloqueamos
if entry_nombre.get():
    entry_nombre.config(state='readonly')



frame_botones = tk.Frame(frame_dns)
frame_botones.pack(pady=10)

btn_borrar = tk.Button(frame_botones, text="Borrar", bg="red", fg="white", command=borrar_dns)
btn_borrar.pack(side=tk.LEFT, padx=10)

btn_guardar = tk.Button(frame_botones, text="Guardar", bg="cyan", command=guardar_dns)
btn_guardar.pack(side=tk.LEFT, padx=10)

# --- Sección HTTP/HTTPS ---
frame_http = tk.Frame(frame_contenedor)

label_http = tk.Label(frame_http, text="HTTP / HTTPS", font=("Arial", 14, "bold"))
label_http.pack(pady=20)

btn_http = tk.Button(frame_http, text="http", bg="red", fg="white", width=10, command=activar_http)
btn_http.pack(pady=5)

btn_https = tk.Button(frame_http, text="https", bg="green", fg="white", width=10, command=activar_https)
btn_https.pack(pady=5)

# Mostrar ambas al inicio

# --- Sección Apagar/Encender ---
frame_power = tk.Frame(frame_contenedor)
# Control de entorno de desarrollo web
label_power = tk.Label(frame_power, text="Control de entorno de desarrollo web", font=("Arial", 14, "bold"))
label_power.pack(pady=20)

btn_apagar = tk.Button(frame_power, text="Apagar", bg="red", fg="white", width=10, command=apagar_entorno)
btn_apagar.pack(pady=5)

btn_encender = tk.Button(frame_power, text="Encender", bg="green", fg="white", width=10, command=encender_entorno)
btn_encender.pack(pady=5)
# Control de desarrollo de grafana
label_power = tk.Label(frame_power, text="Control de entorno de grafana", font=("Arial", 14, "bold"))
label_power.pack(pady=20)

btn_apagar = tk.Button(frame_power, text="Apagar", bg="red", fg="white", width=10, command=apagar_grafana)
btn_apagar.pack(pady=5)

btn_encender = tk.Button(frame_power, text="Encender", bg="green", fg="white", width=10, command=encender_grafana)
btn_encender.pack(pady=5)

# --- Terminal del contenedor ---


def ejecutar_comando(event=None):
    comando = entrada_comando.get().strip()
    if not comando:
        return
    consola.config(state="normal")
    consola.insert(tk.END, f"$ {comando}\n")
    consola.see(tk.END)
    entrada_comando.delete(0, tk.END)

    # Validar comandos no soportados
    if comando in ["bash", "/bin/bash", "python", "python3"]:
        consola.insert(tk.END, "⚠️ Comando interactivo no soportado en esta terminal.\n", "error")
        consola.see(tk.END)
        consola.config(state="disabled")
        return

    try:
        output = contenedor.exec_run(cmd=comando, stdout=True, stderr=True, demux=True)
        stdout, stderr = output.output if hasattr(output, 'output') else output
        if stdout:
            consola.insert(tk.END, stdout.decode('utf-8'))
        if stderr:
            consola.insert(tk.END, stderr.decode('utf-8'), "error")
    except Exception as e:
        consola.insert(tk.END, f"❌ Error al ejecutar el comando: {e}\n", "error")
    consola.insert(tk.END, "\n")
    consola.see(tk.END)
    consola.config(state="disabled")

# --- Frame Terminal ---
frame_terminal = tk.Frame(frame_contenedor)

label_terminal = tk.Label(frame_terminal, text="Terminal del server", font=("Arial", 14, "bold"))
label_terminal.pack(pady=5)

consola = tk.Text(frame_terminal, bg="black", fg="white", insertbackground="white", height=15)
consola.tag_config("error", foreground="red")
consola.insert(tk.END, "$ ")
consola.config(state="disabled")
consola.pack(fill=tk.BOTH, expand=True, padx=10)

entrada_comando = tk.Entry(frame_terminal, bg="white")
entrada_comando.pack(fill=tk.X, padx=10, pady=5)
entrada_comando.bind("<Return>", ejecutar_comando)

# --- Frame Monitor Docker ---
frame_monitor = tk.Frame(frame_contenedor)

tree_monitor = ttk.Treeview(frame_monitor, columns=("Nombre", "Estado", "CPU (%)", "Memoria (MB)", "RAM (%)"), show='headings')
tree_monitor.heading("Nombre", text="Nombre")
tree_monitor.heading("Estado", text="Estado")
tree_monitor.heading("CPU (%)", text="CPU (%)")
tree_monitor.heading("Memoria (MB)", text="Memoria (MB)")
tree_monitor.heading("RAM (%)", text="RAM (%)")
tree_monitor.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

mostrar_todo()

root.mainloop()

# composer create-project laravel/laravel /var/www/html/laravelf
#chown -R www-data:www-data /var/www/html/laravelf
#chmod -R 775 /var/www/html/laravelf
#php artisan migrate /var/www/html/laravelf