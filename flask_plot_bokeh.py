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

# Генерация рандомного сигнала
def randomSignal():
    global signal_x
    while(1):
        time.sleep(2)
        time_x = np.linspace(0, 10, 500)
        signal_x = np.sin(time_x)*random.randrange(1,7)
        print(signal_x)


# формирую синус 
@app.route('/')
def homepage():
    time.sleep(2)
    time_x = np.linspace(0, 10, 500)
    signal_x = np.sin(time_x)*random.randrange(1,7)
    time_x = time_x.tolist()
    signal_x = signal_x.tolist()

    print(signal_x)
    return render_template(template_name_or_list='chartjs-example.html',
                           data=signal_x,
                           labels=time_x)
#	return render_template(
#		template_name_or_list='chartjs-example.html',
#		data=signal_x,
#		labels=time_x,
#	)
def runApp():
    #app.run(host="localhost", port=8086, debug=False)
    app.run(host="127.0.0.1", port=8086, debug=False)

# Main Driver Function 
if __name__ == '__main__':
	# Run the application on the local development server ##
#    t1 = Thread(target=randomSignal).start()
    t2 = Thread(target=runApp).start()
#	app.run(debug=True)

