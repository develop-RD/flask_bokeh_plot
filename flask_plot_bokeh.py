# Importing required functions 
from flask import Flask, render_template
import numpy as np
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
	# Return the components to the HTML template 
	return render_template(
		template_name_or_list='chartjs-example.html',
		data=signal_x,
		labels=time_x,
	)


# Main Driver Function 
if __name__ == '__main__':
	# Run the application on the local development server ##
	app.run(debug=True)

