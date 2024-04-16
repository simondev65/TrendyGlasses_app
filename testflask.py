from flask import Flask
from queue import Queue, Empty
from threading import Thread
from time import sleep
import json
import time

app = Flask(__name__, template_folder='templates')
commands = Queue()

def producer_order():
    while True:
        try:
            command = commands.get_nowait()
            print(command)
        except Empty:
            pass
        sleep(5)  # TODO poll other things

Thread(target=producer_order, daemon=True).start()

# Literally the Flask quickstart but pushing to the queue
@app.route("/")
def hello_world():
    commands.put_nowait({ 'action': 'something' })
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)