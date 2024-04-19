from flask import Flask         # фреймворк для создания веб-приложений на языке Python
from flask import request       # модуль Flask для обработки запросов, пришедших к серверу
from flask import jsonify       # функция Flask для преобразования объектов Python в JSON
import random                   # модуль Python для генерации случайных чисел

app = Flask(__name__)           # создание объекта приложения Flask


@app.route('/number/', methods=['GET'])                                 # декоратор route() создает маршрут для обработки HTTP-запроса
def lab3_1():                                                           
    param=int(request.args.get('param'))                                # получение значения параметра из GET-запроса
    rand = random.randint(1,100)                                        # генерация случайного числа от 1 до 100
    print(rand)                                                         
    result = rand*param                                                 # вычисление результата, произведение параметра и случайного числа
    return jsonify()    # возврат результата в виде JSON-объекта


@app.route('/number/', methods=['POST'])                                # обработка POST запроса
def lab3_2():
    data = request.get_json()                                           # получаем данные, отправленные с запросом
    json_param = data['jsonParam']                                      # получаем значение параметра jsonParam из отправленных данных
    rand = random.randint(1, 100)                                       # создаем случайное целое число от 1 до 100

    operation = random.choice(['sum', 'sub', 'mul', 'div'])             # выбираем случайную операцию

    if operation == 'sum':                                              # если выбрана операция сложения
        result = rand + json_param                                      # выполняем сложение случайного числа и параметра jsonParam
    elif operation == 'sub':
        result = rand - json_param
    elif operation == 'mul':
        result = rand * json_param
    else:
        result = rand / json_param
    
    response = {                                                         # создаем словарь с результатами
        'rand': rand,
        'json_param': json_param,
        'operation': operation,
        'result': result
    }
    return jsonify(response)                                            # возвращаем результат операции в формате JSON


@app.route('/number/', methods=['DELETE'])                              # метод 'DELETE' используется для удаления ресурса или данных по указанному URL-адресу
def lab3_3():
    rand = random.randint(1, 100)                                       # создаем случайное целое число от 1 до 100
    operation = random.choice(['sum', 'sub', 'mul', 'div'])             # выбираем случайную операцию
    return jsonify({'rand': rand, 'operation': operation})              # возвращаем результат операции в формате JSON



if __name__ == '__main__':      # если файл выполняется как отдельный скрипт
    app.run(debug=True)         # запустить веб-сервер Flask в режиме отладки

    

