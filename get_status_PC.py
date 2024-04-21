import psutil
import time
from pyspectator.processor import Cpu
from datetime import datetime

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

def update_count():
    global list_cpu,list_ram,list_temp,list_time
    while(1):
        list_cpu.append(cpu.load)
        list_temp.append(cpu.temperature)
        current_time = str(datetime.now().time())
        list_time.append(current_time)
        # Потребляет памяти данный процесс
        process = psutil.Process()
        list_ram.append(process.memory_info().rss/1024)

#        print("CPU = ",list_cpu)
#        print("Time = ",list_time)
#        print("Ram = ",list_ram)
        time.sleep(5)

@app.route('/get_data_system', methods=['GET'])
def get_data_system():
    return jsonify({'data_cpu': list_cpu, 
                    'data_temp':list_temp,
                    'data_time':list_time,
                    'data_ram': list_ram})

# формирую информацию 
@app.route('/')
def homepage():
    return render_template(template_name_or_list='param_system.html',
                           data_cpu=list_cpu,
                           labels=list_time,
                           data_temp=list_temp,
                           data_ram=list_ram)
def runApp():
    app.run(host="127.0.0.1", port=5000, debug=False)

# Main Driver Function 
if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_count)
    t.start()
    app.run(debug=True)

