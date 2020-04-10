import threading
import time

from gi.repository import GLib, Gtk, GObject

from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    # GLib.idle_add(update_progess, i)
    return 'Hello, World!'

def flask_thread():
    app.run(debug=True, use_reloader=False, port=8643)
