import json
import datetime
import os



    
def create_task(desc):
    
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as infile:
            try:
                tasks = json.load(infile)
            except json.JSONDecodeError:
                tasks = {}
    else:
        tasks = {}

    datos = {
        "id" : str(len(tasks) + 1),
        "description" : desc,
        "status" : "default",
        "createdAt" : str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")),
        "updatedAt" : str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    }

    task_name = f"tasks{len(tasks)+1}"

    tasks[task_name] = datos

    with open("datos.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)
        
def show_tasks(status=None):
    if not os.path.exists("datos.json"):
        print("No existe el archivo datos.json todavía.")
        return
    
    with open("datos.json", "r") as infile:
        try:
            tasks = json.load(infile)
            
            if not tasks:
                print("No hay tareas registradas.")
                return
            
            print("\nLISTA DE TAREAS\n" + "="*50)
            
            for key, task in tasks.items():
                
                if status and task.get('status') != status:
                    continue
                
                
                desc = task.get('description') or task.get('drescription', 'Sin descripción')
                
                print(f"\n🔹 Tarea: {key}")
                print(f"   ID: {task.get('id')}")
                print(f"   Descripción: {desc}")
                print(f"   Estado: {task.get('status')}")
                print(f"   Creado: {task.get('createdAt')}")
                print(f"   Actualizado: {task.get('updatedAt')}")
            
            print("\n" + "="*50)
            
        except json.JSONDecodeError:
            print("⚠️ El archivo JSON está vacío o corrupto.")
        
def update_task(id, drescription):
    
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as infile:
            try:
                tasks = json.load(infile)
                
                task_key = f"tasks{id}"
                
                if task_key in tasks:
                    tasks[task_key]["description"] = drescription
                    tasks[task_key]["updatedAt"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    print(f"Tarea {id} actualizada con éxito.")
                else:
                    print(f"No existe la tarea con id {id}")    
            except json.JSONDecodeError:
                tasks = {}
    else:
        tasks = {}

    with open("datos.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)

def delete_task(id):
    
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as infile:
            try:
                tasks = json.load(infile)
                
                task_key = f"tasks{id}"
                
                if task_key in tasks:
                    del tasks[task_key]
                    print(f"Tarea {id} eliminada con éxito.")
                else:
                    print(f"No existe la tarea con id {id}")    
            except json.JSONDecodeError:
                tasks = {}
    else:
        print("El archivo JSON está vacío o corrupto.")

    with open("datos.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)

def mark_task(status, id):
    pass
    
while True:
    print("\nTask CLI")
    print("1. Agregar tarea")
    print("2. Listar todas las tareas")
    print("3. Listar tareas por estado")
    print("4. Actualizar tarea")
    print("5. Eliminar tarea")
    print("6. Marcar tarea (todo / in_progress / done)")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        desc = input("Ingrese la descripción de la tarea: ")
        create_task(desc)

    elif opcion == "2":
        show_tasks()

    elif opcion == "3":
        estado = input("Ingrese estado (todo / in_progress / done): ")
        show_tasks()

    elif opcion == "4":
        id = input("Ingrese el ID de la tarea: ")
        desc = input("Nueva descripción: ")
        update_task(id, desc)

    elif opcion == "5":
        id = input("Ingrese el ID de la tarea: ")
        delete_task(id)

    elif opcion == "6":
        id = input("Ingrese el ID de la tarea: ")
        estado = input("Nuevo estado (todo / in_progress / done): ")
        mark_task(id, estado)

    elif opcion == "0":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")