from Analizadores.Sintactico import parser, getListaEstudiantes, getListaTareas

if __name__ == '__main__':
    f = open('Estudiantes.txt', "r", encoding="utf-8")
    mensaje = f.read()
    f.close()
    parser.parse(mensaje)
    lista_estudiantes = getListaEstudiantes()
    lista_tareas = getListaTareas()

    print("\n\n------------------------ LISTADO DE OBJETOS ESTUDIANTE ------------------------\n")
    for estudiante in lista_estudiantes:
        print("Carnet: ", estudiante.getCarnet())
        print("Nombre: ", estudiante.getNombre())
        print("Carrera: ", estudiante.getCarrera())
        print("Password: ", estudiante.getPassword())
        print("Creditos: ", estudiante.getCreditos())
        print("Edad: ", estudiante.getEdad())
        print("Correo: ", estudiante.getCorreo(), "\n")
        print()


    print("\n\n------------------------ LISTADO DE OBJETOS TAREA ------------------------\n")
    for tarea in lista_tareas:
        print("Carnet: ", tarea.getCarnet())
        print("Nombre: ", tarea.getNombre())
        print("Descripcion: ", tarea.getDescripcion())
        print("Materia: ", tarea.getMateria())
        print("Fecha: ", tarea.getFecha())
        print("Hora: ", tarea.getHora())
        print("Estado: ", tarea.getEstado(), "\n")
