import psutil
import time
from pyspectator.processor import Cpu
from datetime import datetime
import random
import numpy as np
# Importing required functions 
from flask import Flask, render_template, jsonify
import numpy as np
import time
# Flask constructor 
app = Flask(__name__)

cpu = Cpu(monitoring_latency=1)

list_cpu =[]
list_temp = []
list_time = []
list_ram =[]

# Формирую отсчёты
time_x = np.linspace(0, 10, 500)
signal_x = np.sin(time_x)

#преобразовываю к типу list.нужно для отрисовки
time_x = time_x.tolist()
signal_x = signal_x.tolist()

def update_count():
    global list_cpu,list_ram,list_temp,list_time,signal_x,time_x
    while(1):
        count = 50
        time_x = np.linspace(0, count, 500)
        signal_x = np.sin(time_x) + random.randrange(10)

        #преобразовываю к типу list.нужно для отрисовки
        time_x = time_x.tolist()
        signal_x = signal_x.tolist()

        list_cpu.append(cpu.load)
        list_temp.append(cpu.temperature)
        current_time = str(datetime.now().time())
        list_time.append(current_time)
        # Потребляет памяти данный процесс
        process = psutil.Process()
        list_ram.append(process.memory_info().rss/1024)

        time.sleep(2)

@app.route('/get_data_system', methods=['GET'])
def get_data_system():
    return jsonify({'data_cpu': list_cpu, 
                    'data_temp':list_temp,
                    'data_time':list_time,
                    'data_ram': list_ram,
                    'data_sin': signal_x,
                    'labels_sin': time_x})

# формирую информацию 
@app.route('/')
def homepage():
    return render_template(template_name_or_list='param_system_sin.html',
                           data_cpu=list_cpu,
                           labels=list_time,
                           data_temp=list_temp,
                           data_ram=list_ram,
                           data_sin=signal_x,
                           labels_sin=time_x)
def runApp():
    app.run(host="127.0.0.1", port=5000, debug=False)

# Main Driver Function 
if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_count)
    t.start()
    app.run(debug=True)

