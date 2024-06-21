import requests

def get_all_students():
    url = 'http://127.0.0.1:80/students'  # URL для получения списка всех студентов
    response = requests.get(url)
    
    if response.status_code == 200:
        students_list = response.json()  # Получаем список студентов в формате JSON
        return students_list
    else:
        return f'Ошибка: {response.status_code}'

def get_student_info(student_id):
    url = f'http://127.0.0.1:80/students/{student_id}'  # URL для получения информации о конкретном студенте
    response = requests.get(url)
    
    if response.status_code == 200:
        student_info = response.json()  # Получаем информацию о студенте в формате JSON
        return student_info
    else:
        return f'Ошибка: {response.status_code}'

# Пример использования функций
all_students = get_all_students()
print("Список всех студентов:")
print(all_students)

student_id = 1  # Пример: получить информацию о студенте с ID=1
student_info = get_student_info(student_id)
print(f"\nИнформация о студенте с ID={student_id}:")
print(student_info)




def add_new_student(student_data):
    url = 'http://127.0.0.1/students'  # Укажите правильный URL вашего сервера
    response = requests.post(url, json=student_data)
    return response.json()

# Пример использования функции
student_data = {"id": 4, "name": "Новый Студент", "age": 22, "major": "Биология"}
response = add_new_student(student_data)
print(response)



def update_student_info(student_id, updated_data):
    url = f'http://127.0.0.1/students/{student_id}'  # Укажите правильный URL вашего сервера
    response = requests.put(url, json=updated_data)
    return response.json()

# Пример использования функции
student_id = 4
updated_data = {"name": "Новый Студент", "age": 23, "major": "Химия"}
response = update_student_info(student_id, updated_data)
print(response)



def delete_student_info(student_id):
    url = f'http://127.0.0.1/students/{student_id}'  # Укажите правильный URL вашего сервера
    response = requests.delete(url)
    return response.json()

# Пример использования функции
student_id = 4
response = delete_student_info(student_id)
print(response)