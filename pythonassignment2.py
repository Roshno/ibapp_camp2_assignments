class report:
    @staticmethod
    def get_Int(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Invalid input')

    @staticmethod
    def get_Float(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Invalid input')


class Student_details:
    def __init__(self, name, maths_mark, physics_mark, chemistry_mark, english_mark, programing_mark) -> None:
        self.__name       = name
        self.__maths      = maths_mark
        self.__physics    = physics_mark
        self.__chemistry  = chemistry_mark
        self.__english    = english_mark
        self.__programing = programing_mark
    
    @property
    def name(self):
        return self.__name
    
    @property
    def maths(self):
        return self.__maths
    
    @property
    def physics(self):
        return self.__physics
    
    @property
    def chemistry(self):
        return self.__chemistry
    
    @property
    def english(self):
        return self.__english
    
    @property
    def programing(self):
        return self.__programing
    
    @maths.setter
    def maths(self, newMark):
        self.__maths = newMark
    
    @maths.setter
    def physics(self, newMark):
        self.__physics = newMark
    
    @maths.setter
    def chemistry(self, newMark):
        self.__chemistry = newMark
    
    @maths.setter
    def english(self, newMark):
        self.__english = newMark
    
    @maths.setter
    def programming(self, newMark):
        self.__programming = newMark

    def display(self):
        print('Name :', self.__name)
        print('Marks:')
        print('Maths:', self.__maths)
        print('Physics:', self.__physics)
        print('Chemistry:', self.__chemistry)
        print('English:', self.__english)
        print('Programing:', self.__programing)


class SRCMS:
    students = dict()

    @staticmethod
    def create():
        rollno = report.get_Int('Rollno: ')
        if SRCMS.students.get(rollno):
            print('Student already exist')
        else:
            name = input('Name: ')
            print('Enter marks')
            maths       = report.get_Float('Maths: ')
            physics     = report.get_Float('Physics: ')
            chemistry   = report.get_Float('Chemistry: ')
            english     = report.get_Float('English: ')
            programing  = report.get_Float('Programing: ')
            student  = Student_details(name, maths, physics, chemistry, english, programing)
            SRCMS.students[rollno] = student
            print('Student added successfully')
    
    @staticmethod
    def delete():
        rollno = report.get_Int('Rollno: ')
        if SRCMS.students.get(rollno):
            del SRCMS.students[rollno]
            print('Student deleted successfully')
        else:
            print('Student does not exist')
    
    @staticmethod
    def modify():
        rollno = report.get_Int('Rollno: ')
        if SRCMS.students.get(rollno):
            student = SRCMS.students.get(rollno)
            student.display()
            while(True):
                opt = report.get_Int(f'''
Choose Mark to edit:
    1. Maths
    2. Physics
    3. Chemistry
    4. English
    5. Programing
    6. Exit
    > '''
                )
                match opt:
                    case 1: student.maths = report.get_Float('Maths: ')
                    case 2: student.physics = report.get_Float('Physics: ')
                    case 3: student.chemistry = report.get_Float('Chemistry: ')
                    case 4: student.english = report.get_Float('English: ')
                    case 5: student.programing = report.get_Float('Programing: ')
                    case 6: break
                    case _: print('Invalid input')
        else:
            print('Student does not exist')

    @staticmethod
    def listAllStudents():
        if len(SRCMS.students) > 0:
            print('Student details: ')
            for rollno, student in SRCMS.students.items():
                print('\nRollno: ', rollno)
                student.display()
        else:
            print('No records')

    @staticmethod
    def showStudent():
        rollno = report.get_Int('Rollno: ')
        if SRCMS.students.get(rollno):
            print('\nRollno: ', rollno)
            SRCMS.students[rollno].display()
        else:
            print('Student does not exist')
    

while(True):
    opt = report.get_Int('''
    1. Create Student Record
    2. Delete Student Record
    3. Modify Marks
    4. Display all Students
    5. Display a student record
    6. Exit
    
    > ''')

    match opt:
        case 1: SRCMS.create()
        case 2: SRCMS.delete()
        case 3: SRCMS.modify()
        case 4: SRCMS.listAllStudents()
        case 5: SRCMS.showStudent()
        case 6: break
        case _: print('Invalid input')