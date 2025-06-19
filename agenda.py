
# agenda.py

def crear_tarea():
    with open('agenda.txt', 'a') as f:
        nombre = input('Introduce el nombre de la tarea: ')
        descripcion = input('Introduce la descripción de la tarea: ')
        fecha = input('Introduce el deadline de la tarea (dd/mm/aaaa): ')
        mas = input('Añade datos relevantes para la tarea: ')
        f.write(f'{nombre}\n{descripcion}\n{fecha}\n{mas}\n---\n')
        print(f"Tarea '{nombre}' añadida a la agenda.")


def modificar_tarea():
    nombre_buscar = input('Introduce el nombre de la tarea a modificar: ')
    with open('agenda.txt', 'r') as f:
        lineas = f.readlines()

    nueva_lineas = []
    i = 0
    encontrada = False
    while i < len(lineas):
        if lineas[i].strip() == nombre_buscar:
            encontrada = True
            print('Tarea encontrada:')
            print(''.join(lineas[i:i+5]))

            nueva_tarea = input('Nuevo nombre de la tarea: ')
            nueva_desc = input('Nueva descripción: ')
            nueva_fecha = input('Nueva fecha (dd/mm/aaaa): ')
            nueva_mas = input('Nuevos datos relevantes: ')
            nueva_lineas.extend([
                f'{nueva_tarea}\n',
                f'{nueva_desc}\n',
                f'{nueva_fecha}\n',
                f'{nueva_mas}\n',
                '---\n'
            ])
            i += 5  # saltar la tarea original
        else:
            nueva_lineas.append(lineas[i])
            i += 1

    if encontrada:
        with open('agenda.txt', 'w') as f:
            f.writelines(nueva_lineas)
        print('Tarea modificada con éxito.')
    else:
        print('Tarea no encontrada.')


def eliminar_tarea():
    nombre_buscar = input('Introduce el nombre de la tarea a eliminar: ')
    with open('agenda.txt', 'r') as f:
        lineas = f.readlines()

    nueva_lineas = []
    i = 0
    encontrada = False
    while i < len(lineas):
        if lineas[i].strip() == nombre_buscar:
            encontrada = True
            print('Tarea eliminada:')
            print(''.join(lineas[i:i+5]))
            i += 5  # saltar la tarea
        else:
            nueva_lineas.append(lineas[i])
            i += 1

    if encontrada:
        with open('agenda.txt', 'w') as f:
            f.writelines(nueva_lineas)
        print('Tarea eliminada con éxito.')
    else:
        print('Tarea no encontrada.')


def ver_tareas():
    with open('agenda.txt', 'r') as f:
        contenido = f.read()
        if not contenido.strip():
            print('No hay tareas en la agenda.')
        else:
            print('Tareas en la agenda:\n')
            print(contenido)

if __name__ == "__main__":
    crear_tarea()
