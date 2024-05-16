import requests                                                         # Инструмент для отправки HTTP-запросов с использованием API
import random                                                           # Модуль Python для генерации случайных чисел

'''Раздел 1'''

test_3_1_1=requests.get('http://127.0.0.1:5000/number/?param=5')        # Отправляем GET запрос на указанный URL
print(test_3_1_1.text)                                                  # Выводим текст ответа от сервера, который содержится в переменной

test_3_1_2=requests.post(                                               # Отправка POST-запроса на указанный URL
    'http://127.0.0.1:5000/number/',                                    # URL, на который отправляется запрос
    json={'jsonParam': 10}                                              # передача данных в формате JSON с параметром 'jsonParam' равным 10
)
print(test_3_1_2.text) 

test_3_1_3=requests.delete('http://127.0.0.1:5000/number/')             # Отправляем DELETE запрос по указанному URL
print(test_3_1_3.text) 

'''Раздел 2'''

try_3_2_1=requests.get('http://127.0.0.1:5000/number/?param=' + str(random.randint(1, 10)))
                                                    # Отправляем GET-запрос на локальный сервер с параметром, который является случайным числом от 1 до 10
data_2_1 = try_3_2_1.json()                         # Получаем данные из ответа в формате json и сохраняем их в переменную
num_2_1 = data_2_1['result']                        # Извлекаем значение из полученных данных и сохраняем его в переменную
print(data_2_1)


json_data = {"jsonParam": random.randint(1, 10)}    # Создаем словарь с данными json_param, где значение будет случайным числом от 1 до 10
headers = {'content-type': 'application/json'}      # Задаем заголовок для запроса, указывая тип контента как application/json
try_3_2_2 = requests.post('http://127.0.0.1:5000/number/', json=json_data, headers=headers)
data_2_2 = try_3_2_2.json()                         # Получаем данные из ответа в формате json и сохраняем их в переменную
num_2_2 = data_2_2['result']                        # Извлекаем значение из полученных данных и сохраняем его в переменную
operation_2_2 = data_2_2['operation']
print(data_2_2)


try_3_2_3=requests.delete('http://127.0.0.1:5000/number/')
data_2_3 = try_3_2_3.json()
num_2_3 = data_2_3['rand']
operation_2_3 = data_2_3['operation']
print(data_2_3)
print('\n','Первое число:',num_2_1,'\n','Второе число:',num_2_2,'\n','Первая операция',operation_2_2,'\n','Третье число:',num_2_3,'\n','Вторая операция:',operation_2_3)

if operation_2_2 == 'sum':
    op_1 = '+'
    result_1 = num_2_1 + num_2_2
elif operation_2_2 == 'sub':
    op_1 = '-'
    result_1 = num_2_1 - num_2_2
elif operation_2_2 == 'mul':
    op_1 = '*'
    result_1 = num_2_1 * num_2_2
else:
    op_1 = '/'
    result_1 = num_2_1 / num_2_2

if operation_2_3 == 'sum':
    op_2 = '+'
    result_2 = result_1 + num_2_3
elif operation_2_3 == 'sub':
    op_2 = '-'
    result_2 = result_1 - num_2_3
elif operation_2_3 == 'mul':
    op_2 = '*'
    result_2 = result_1 * num_2_3
else:
    op_2 = '/'
    result_2 = result_1 / num_2_3

print('\n',num_2_1,op_1,num_2_2,'=',result_1,'\n',result_1,op_2,num_2_3,'=',result_2,'\n','Результат:',result_2)
