
from typing import Optional, Tuple, Dict, List


class Student:
    def __init__(self, firstName: str, lastName: str, idNumber: str, semester: int, program: str):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.semester = semester
        self.program = program
        self.next: Optional['Student'] = None

    def __repr__(self):
        return (f"Student({self.firstName} {self.lastName}, id={self.idNumber}, "
                f"sem={self.semester}, prog={self.program})")


class Class:
    def __init__(self, class_id: str, name: str, credits: int):
        if credits <= 0:
            raise ValueError("Los créditos deben ser un número positivo.")
        self.id = class_id
        self.name = name
        self.credits = credits
        self.head: Optional[Student] = None

    def __repr__(self):
        return f"Class(id={self.id}, name='{self.name}', credits={self.credits})"

    # -----------------------
    # Operaciones sobre alumnos (lista enlazada simple)
    # -----------------------

    def find_student(self, idNumber: str) -> Tuple[Optional[Student], Optional[Student]]:
        """
        Recorre la lista y devuelve una tupla (prev, current) donde current.idNumber == idNumber si existe.
        prev es None si current es head.
        """
        prev = None
        current = self.head
        while current:
            if current.idNumber == idNumber:
                return prev, current
            prev = current
            current = current.next
        return None, None

    def student_exists(self, idNumber: str) -> bool:
        _, node = self.find_student(idNumber)
        return node is not None

    def insert_student(self, new_student: Student) -> bool:
        """
        Inserta el estudiante en la lista. Estrategia: mantener la lista ordenada por lastName (asc),
        y ante empate por lastName, ordenar por idNumber (asc).
        Justificación: permite búsquedas por orden alfabético y genera un orden estable y reproducible.
        """
        if self.student_exists(new_student.idNumber):
            print(f"[ERROR] Inscripción duplicada: el idNumber {new_student.idNumber} ya existe en la clase {self.id}.")
            return False

        # caso lista vacía -> head = new_student
        if self.head is None:
            self.head = new_student
            print(f"[OK] Estudiante {new_student.idNumber} insertado como head en clase {self.id}.")
            return True

        # Si debe ir antes del head por orden
        if (new_student.lastName.lower(), new_student.idNumber) < (self.head.lastName.lower(), self.head.idNumber):
            new_student.next = self.head
            self.head = new_student
            print(f"[OK] Estudiante {new_student.idNumber} insertado al inicio (nuevo head) en clase {self.id}.")
            return True

        # insertar en posición ordenada
        prev = None
        current = self.head
        while current and (current.lastName.lower(), current.idNumber) <= (new_student.lastName.lower(), new_student.idNumber):
            prev = current
            current = current.next

        # insertar entre prev y current
        prev.next = new_student
        new_student.next = current
        print(f"[OK] Estudiante {new_student.idNumber} insertado después de {prev.idNumber} en clase {self.id}.")
        return True

    def list_students(self) -> List[Student]:
        result = []
        current = self.head
        while current:
            result.append(current)
            current = current.next
        return result

    def update_student(self, idNumber: str, **updates) -> bool:
        prev, node = self.find_student(idNumber)
        if node is None:
            print(f"[INFO] Actualización: estudiante con id {idNumber} no encontrado en clase {self.id}.")
            return False

        # Actualizar campos permitidos
        for key, value in updates.items():
            if key in ('firstName', 'lastName', 'semester', 'program', 'idNumber'):
                # Si cambian idNumber hay que comprobar duplicado (si es distinto)
                if key == 'idNumber' and value != node.idNumber and self.student_exists(value):
                    print(f"[ERROR] No se pudo actualizar idNumber a {value}: ya existe otro estudiante con ese id.")
                    return False
                setattr(node, key, value)
        print(f"[OK] Estudiante {idNumber} actualizado en clase {self.id}.")
        # Si se modificó lastName o idNumber, para mantener orden hay que reubicar el nodo.
        if 'lastName' in updates or 'idNumber' in updates:
            # remover y volver a insertar conservando el objeto (para mantener referencia)
            # Primero desconectar node de la lista
            self._remove_node(prev, node)
            # Reiniciar next antes de reinsertar
            node.next = None
            # Insertar con la lógica de ordenamiento
            self.insert_student(node)
            print(f"[INFO] Nodo reubicado para mantener orden en clase {self.id}.")
        return True

    def _remove_node(self, prev: Optional[Student], node: Student) -> None:
        if prev is None:
            # quitar head
            if self.head is node:
                self.head = node.next
        else:
            prev.next = node.next
        node.next = None

    def remove_student(self, idNumber: str) -> bool:
        prev, node = self.find_student(idNumber)
        if node is None:
            print(f"[INFO] Retiro: estudiante con id {idNumber} no encontrado en clase {self.id}.")
            return False

        self._remove_node(prev, node)
        print(f"[OK] Estudiante {idNumber} eliminado de la clase {self.id}.")
        # Comprobar integridad: recorrer la lista y asegurarse de que no haya referencias fantasmas
        self._verify_integrity()
        return True

    def _verify_integrity(self) -> None:
        # Recorre y confirma que no hay ciclos y que next es coherente (simple check)
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # ciclo detectado
                print(f"[CRITICAL] Ciclo detectado en la lista de la clase {self.id}.")
                return
        # Si no hay ciclo, imprime número de nodos y head actual
        n = len(self.list_students())
        print(f"[CHECK] Integridad OK en clase {self.id}. Head = {self.head.idNumber if self.head else 'None'}, total estudiantes = {n}.")

    def find_students_by_lastname(self, lastName: str) -> List[Student]:
        matches = []
        current = self.head
        while current:
            if current.lastName.lower() == lastName.lower():
                matches.append(current)
            current = current.next
        return matches

    def clear_students(self) -> None:
        """
        Libera la lista enlazada: desconecta nodos y deja head = None.
        Aunque Python tiene recolector, hacemos la desconexión explícita para evidenciar la liberación.
        """
        current = self.head
        count = 0
        while current:
            nxt = current.next
            # opcional: borrar campos para evidenciar liberación
            current.next = None
            count += 1
            current = nxt
        self.head = None
        print(f"[OK] Lista de estudiantes de la clase {self.id} liberada. {count} nodos eliminados.")


# -----------------------
# Gestión global de clases (puede usar un dict/colección para las clases)
# -----------------------

class AcademicManager:
    def __init__(self):
        # Aquí sí usamos una colección para mantener las clases (no está prohibido en el enunciado)
        self.classes: Dict[str, Class] = {}

    # CRUD para las clases
    def create_class(self, class_id: str, name: str, credits: int) -> bool:
        if class_id in self.classes:
            print(f"[ERROR] La clase con id {class_id} ya existe.")
            return False
        try:
            new_class = Class(class_id, name, credits)
        except ValueError as e:
            print(f"[ERROR] No se pudo crear la clase: {e}")
            return False
        self.classes[class_id] = new_class
        print(f"[OK] Clase creada: {new_class}")
        return True

    def get_class(self, class_id: str) -> Optional[Class]:
        return self.classes.get(class_id)

    def update_class(self, class_id: str, name: Optional[str] = None, credits: Optional[int] = None) -> bool:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[INFO] No existe la clase con id {class_id}.")
            return False
        if credits is not None:
            if credits <= 0:
                print("[ERROR] Los créditos deben ser positivos.")
                return False
            cl.credits = credits
        if name is not None:
            cl.name = name
        print(f"[OK] Clase actualizada: {cl}")
        return True

    def delete_class(self, class_id: str) -> bool:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[INFO] No existe la clase con id {class_id}.")
            return False
        # liberar lista enlazada correctamente
        cl.clear_students()
        # eliminar la clase del registro
        del self.classes[class_id]
        print(f"[OK] Clase {class_id} eliminada del sistema.")
        return True

    def list_classes(self) -> List[Class]:
        return list(self.classes.values())

    # Métodos de ayuda para operar alumnos desde el manager (encapsulan llamadas a Class)
    def enroll_student(self, class_id: str, firstName: str, lastName: str, idNumber: str, semester: int, program: str) -> bool:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[ERROR] No existe la clase {class_id}.")
            return False
        # validar credits positivos (requisito en registrar alumno)
        if cl.credits <= 0:
            print(f"[ERROR] No se puede inscribir: la clase {class_id} tiene créditos no válidos ({cl.credits}).")
            return False
        new_student = Student(firstName, lastName, idNumber, semester, program)
        return cl.insert_student(new_student)

    def update_student(self, class_id: str, idNumber: str, **updates) -> bool:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[ERROR] No existe la clase {class_id}.")
            return False
        return cl.update_student(idNumber, **updates)

    def remove_student(self, class_id: str, idNumber: str) -> bool:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[ERROR] No existe la clase {class_id}.")
            return False
        return cl.remove_student(idNumber)

    def find_student(self, class_id: str, idNumber: str) -> Optional[Student]:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[ERROR] No existe la clase {class_id}.")
            return None
        _, node = cl.find_student(idNumber)
        if node:
            print(f"[FOUND] {node} en clase {class_id}.")
        else:
            print(f"[NOT FOUND] Estudiante con id {idNumber} no encontrado en clase {class_id}.")
        return node

    def list_students_in_class(self, class_id: str) -> List[Student]:
        cl = self.get_class(class_id)
        if not cl:
            print(f"[ERROR] No existe la clase {class_id}.")
            return []
        students = cl.list_students()
        if not students:
            print(f"[INFO] No hay estudiantes inscritos en la clase {class_id}.")
        return students


# -----------------------
# Ejemplo de uso / pruebas simples
# -----------------------

def demo():
    manager = AcademicManager()

    # Crear clases
    manager.create_class("CS101", "Introducción a la Programación", 3)
    manager.create_class("MAT201", "Cálculo II", 4)

    # Intento crear clase con créditos inválidos
    manager.create_class("BAD1", "Clase mala", 0)

    # Inscribir estudiantes en CS101
    manager.enroll_student("CS101", "Ana", "Zapata", "1001", 1, "Sistemas")
    manager.enroll_student("CS101", "Luis", "Álvarez", "1002", 2, "Sistemas")
    manager.enroll_student("CS101", "Beatriz", "Álvarez", "1003", 1, "Sistemas")  # mismo lastName -> orden por id
    manager.enroll_student("CS101", "Carlos", "Mendoza", "1004", 3, "Sistemas")

    # Intento duplicado
    manager.enroll_student("CS101", "Duplicado", "Perez", "1002", 1, "Sistemas")

    # Listar alumnos (debería estar ordenado por lastName, idNumber)
    print("\nLista alumnos CS101:")
    for s in manager.list_students_in_class("CS101"):
        print("  ", s)

    # Buscar estudiante
    manager.find_student("CS101", "1003")
    manager.find_student("CS101", "9999")  # no existe

    # Actualizar estudiante (cambiar apellido y forzar reubicación)
    manager.update_student("CS101", "1004", lastName="Alarcón", firstName="Carlos R.")
    print("\nLista alumnos CS101 tras actualización:")
    for s in manager.list_students_in_class("CS101"):
        print("  ", s)

    # Eliminar primer nodo, nodo intermedio y último
    # Primero eliminar head actual
    head_id = manager.list_students_in_class("CS101")[0].idNumber
    manager.remove_student("CS101", head_id)

    # Eliminar un intermedio
    manager.remove_student("CS101", "1003")

    # Eliminar no existente
    manager.remove_student("CS101", "0000")

    print("\nLista alumnos CS101 tras eliminaciones:")
    for s in manager.list_students_in_class("CS101"):
        print("  ", s)

    # Eliminar clase completa (libera lista)
    manager.delete_class("CS101")
    # Intentar listar estudiantes de clase eliminada
    manager.list_students_in_class("CS101")

    # Mostrar clases restantes
    print("\nClases en el sistema:")
    for c in manager.list_classes():
        print("  ", c)


if __name__ == "__main__":
    demo()
