#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()

@app.route('/states_list')
def states_list():
    """Display a HTML page with the list of all State objects."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=sorted(states, key=lambda state: state.name))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
