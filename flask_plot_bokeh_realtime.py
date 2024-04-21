# Importing required functions 
from flask import Flask, render_template, jsonify
import numpy as np
import time
# Flask constructor 
app = Flask(__name__)

# Формирую отсчёты
time_x = np.linspace(0, 10, 500)
signal_x = np.sin(time_x)

#преобразовываю к типу list.нужно для отрисовки
time_x = time_x.tolist()
signal_x = signal_x.tolist()
# Счётчик для инкремента
count = 0
 
# функция обновления счётчика
def update_count():
    global count, signal_x, time_x
    while True:
        time_x = np.linspace(0, count, 500)
        signal_x = np.sin(time_x)

        #преобразовываю к типу list.нужно для отрисовки
        time_x = time_x.tolist()
        signal_x = signal_x.tolist()

        count += 1
        time.sleep(3)

@app.route('/get_count', methods=['GET'])
def get_count():
    return jsonify({'count_n': count, 'data':signal_x,'labels':time_x})

# формирую синус 
@app.route('/')
def homepage():
    return render_template(template_name_or_list='chartjs-example.html',
                           data=signal_x,
                           labels=time_x)
def runApp():
    #app.run(host="localhost", port=8086, debug=False)
    app.run(host="127.0.0.1", port=5000, debug=False)

# Main Driver Function 
if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_count)
    t.start()
    app.run(debug=True)

