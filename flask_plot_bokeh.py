# Importing required functions 
from flask import Flask, render_template
import numpy as np
import random
import time
from threading import Thread
# Flask constructor 
app = Flask(__name__)

# Формирую отсчёты
time_x = np.linspace(0, 10, 500)
signal_x = np.sin(time_x)

#преобразовываю к типу list.нужно для отрисовки
time_x = time_x.tolist()
signal_x = signal_x.tolist()

# формирую синус 
@app.route('/')
def homepage():
    return render_template(template_name_or_list='chartjs-example.html',
                           data=signal_x,
                           labels=time_x)
def runApp():
    #app.run(host="localhost", port=8086, debug=False)
    app.run(host="127.0.0.1", port=8086, debug=False)

# Main Driver Function 
if __name__ == '__main__':
	app.run(debug=True)

