from turtle import update
import pyodbc

#create a connection string
myconn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-D2MSN9I\SQLEXPRESS;Database=PMS_db;Trusted_Connection=yes;')
myCursor = myconn.cursor()

def searchName():
    n = input('Enter name to search: ')
    try:
        myCursor.execute(
            'SELECT PatientName, gender, age, bloodGroup FROM Patient_details WHERE patientName LIKE ?',
            (f'%{n}%')
        )
    except:
        print('Failed to fetch patient details')
    else:
        Patient_details= myCursor.fetchall()
        if len(Patient_details) > 0:
            print('Patient Details:')
            #print(Patient_details)
            for patientName, gender, age, bloodGroup in Patient_details:
                print(f'Name: {patientName}')
                print(f'Gender: {gender}')
                print(f'Age: {age}')
                print(f'Blood Group: {bloodGroup}')
        print(f'{len(Patient_details)}  matches {n}')


def add():
    while(True):
        name = input('Enter name: ').strip()
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    while(True):
        patientID=int(input('Enter patient id:'))
        gender = input('Enter gender of patient: ')
        age = int(input("Enter age of patient: "))
        bloodGroup = input('Enter blood group: ').strip()
        break
    try:
        myCursor.execute(
            'INSERT INTO Patient_details VALUES (?,?,?,?,?);',
            (patientID, name, gender, age, bloodGroup )
        )
        myconn.commit()
    except:
        print('Failed to add patient')
    else:
        print('Patient added')

def delete():
    name = input('Enter name to delete: ')
    try:
        myCursor.execute(
            'DELETE FROM Patient_details WHERE patientName=?',
            (name)
        )
        myconn.commit()
    except:
        print('Failed to delete')
    else:
        if myCursor.rowcount > 0:
            print('Deleted')
        else:
            print(f'{name} does not exist')

def sort():
    try:
        myCursor.execute('SELECT patientName, patientID FROM Patient_details ORDER BY patientName;')
    except:
        print('Failed to fetch patient details')
    else:
        Patients = myCursor.fetchall()
        if len(Patients) > 0:
            print('Patients:')
            for name, phone in Patients:
                print(f'Name: {name}')
                print(f'Patient ID: {phone}\n')
        print(f'{len(Patients)} contacts')

        
def update():
    while(True):
        name = input('Enter name: ')
        if ',' in name:
            print(', not allowed in name')
        else:
            break
    try:          
        myCursor.execute("SELECT * FROM Patient_details WHERE patientName = ?",(name))
        cursorn = myCursor.fetchall()
        print(cursorn)
    except Exception:
        print("error")

    else: 
        myCursor.execute('DELETE FROM Patient_details WHERE patientName = ?',(name))
        while(True):
            name = input('Enter name: ').strip()
            patientID=int(input('enter patient id:'))
            gender = input('Enter gender of patient: ')
            age = int(input("Enter age of patient: "))
            bloodGroup = input('Enter blood group: ').strip()
            break
    try:

        myCursor.execute('INSERT INTO Patient_details VALUES (?,?,?,?,?);',(patientID, name, gender, age, bloodGroup)
        )
        
        myconn.commit()
    except:
        print('Failed to update patient')
    else:
        print('Patient details updated')


while(True):
    print('''
    1. Add new patient
    2. Update patient details
    3. Delete patient details
    4. List patients
    5. Search patient name
    6. Exit
    ''')
    opt = int(input('> '))
    match opt:
        case 1: add()
        case 2: update()
        case 3: delete()
        case 4: sort()
        case 5: searchName()
        case 6: break
        case _: print('Invalid input')

myconn.close()
