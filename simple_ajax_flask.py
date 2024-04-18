from flask import Flask, render_template, jsonify 
from threading import Thread
import time

app = Flask(__name__)

count = 0


def update_count():
    global count
    while True:
        count += 1
        time.sleep(2)

@app.route('/') 
def index():
    return render_template('index.html', count=count)

@app.route('/get_count', methods=['GET'])
def get_count():
    return jsonify({'count': count})

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=update_count)
    t.start()
    app.run(debug=True)
