from os import system
from view import Menu_View,print_table
from model import Connector

class App_Controller:
    @staticmethod
    def run():
        system("cls")
        while True:
            main_menu = Menu_View({
                "Professor":Main_Controller.show_menu_professor,
                "Student":Main_Controller.show_menu_student,
                "Curso":Main_Controller.show_menu_course,
                "Periodo":Main_Controller.show_menu_period,
                "Exit":Main_Controller.exit
            },
            title="MENU PRINCIPAL")
            main_menu.ask_option()

class Main_Controller:

    @staticmethod
    def show_menu_professor():
        professor_menu = Menu_View({
            "Crear profesor":lambda:Professor_Controller.create('profesores'),
            "Editar Profesor":lambda:Professor_Controller.edit('profesores'),
            "Eliminar Profesor":lambda:Professor_Controller.delete('profesores'),
            "Listar Profesor":lambda:Professor_Controller.get_all('profesores'),
            
            "Regresar":print
        },
        title='MENU PROFESOR')
        professor_menu.ask_option()
    
    @staticmethod
    def show_menu_student():
        student_menu = Menu_View({
            "Crear Alumno":lambda:Student_Controller.create('alumnos'),
            "Editar Alumno":lambda:Student_Controller.edit('alumnos'),
            "Eliminar Alumno":lambda:Student_Controller.delete('alumnos'),
            "Listar Alumnos":lambda:Student_Controller.get_all('alumnos'),
            "Regresar":print,
        },
        title='MENU ALUMNO')
        student_menu.ask_option()
    
    @staticmethod
    def show_menu_course():
        course_menu = Menu_View({
            "Crear Curso": Course_Controller.create,
            "Editar Curso":Course_Controller.edit,
            "Eliminar Curso":Course_Controller.delete,
            "Regresar":print
        },
        title='MENU CURSO')
        course_menu.ask_option()

    @staticmethod
    def show_menu_period():
        period_menu = Menu_View({
            "Crear Periodo": Period_Controller.create,
            "Editar Periodo":Period_Controller.edit,
            "Eliminar Periodo":Period_Controller.delete,
            "Regresar":print
        },
        title='MENU_PERIODO')
        period_menu.ask_option()

    def show_menu_room():
        room_menu = Menu_View({
            "Crear Salon": Room_Controller.create,
            "Editar Salon":Room_Controller.edit,
            "Eliminar Salon":Room_Controller.delete,
            "Regresar":print
        },
        title='MENU SALON')

    @staticmethod
    def exit():
        exit(1)


#person    
class Person_Controller:
    @staticmethod
    def create(table_name):
        name = input("Ingrese Nombres y Apellidos: ").strip().lower()
        age = input("Ingrese edad: ")
        email = input("Ingrese correo: ").strip()

        connector = Connector()
        if connector.get_data(table_name,'correo','correo=%s',email)  is None:
            connector.register(table_name,nombres=name,edad=age,correo=email)
        else:
            print("El usuario ya ha sido registrado anteriormente")

    @staticmethod 
    def edit(table_name):
        email = input("Ingrese email: ").strip()
        connector = Connector()
        user_data = connector.get_data(table_name,'id,nombres,edad,correo','correo=%s',email)
        if  user_data is None:
            print("El usuario no existe")
        else:
            print("Datos de usuario:",user_data[1:])
            edit_menu = Menu_View({
                'Editar Nombre':lambda:Person_Controller.__action_edit(table_name,email,'nombres'),
                'Editar edad':lambda:Person_Controller.__action_edit(table_name,email,'edad'),
                'Editar Correo':lambda:Person_Controller.__action_edit(table_name,email,'correo')
            },
            title=f"Editar {table_name}")
            edit_menu.ask_option(mss_option="Ingrece Opcion a Editar")

    @staticmethod
    def __action_edit(table_name,email,name_field):
        value = input(f"Ingrese {name_field}: ")
        connector = Connector()
        connector.update(table_name,f'{name_field}=%s','correo=%s',value,email)

    @staticmethod
    def delete(table_name):
        email = input("Ingrese email: ").strip()
        connector = Connector()
        user_data = connector.get_data(table_name,'correo','correo=%s',email)
        if  user_data is None:
            print("El usuario no existe")
        else:
            connector = Connector()
            connector.delete(table_name,'correo=%s',email)

    @staticmethod
    def get_all(table_name):
        connector = Connector()
        all_users = connector.get_all(table_name)
        if len(all_users) == 0:
            print(f"Aún no hay {table_name} registrados")
        else:
            print_table({
                'Id':[i[0] for i in all_users],
                'Nombres':[i[1] for i in all_users],
                'Edad':[i[2] for i in all_users],
                'Correo':[i[3] for i in all_users],
                })
    
class Student_Controller(Person_Controller):
    pass

class Professor_Controller(Person_Controller):
    
    @staticmethod
    def assign_course():
        pass
#person
""" 
class Course_Controller(Object_Controller):
    pass

class Period_Controller(Object_Controller):
    pass

class Room_Controller(Object_Controller):
    pass """