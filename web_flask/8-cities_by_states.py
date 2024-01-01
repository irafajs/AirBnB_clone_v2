#!/usr/bin/python3
"""
Shebang to make a Py script
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """Teardown method remove SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """Display cities by states"""
    states = storage.all(State).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states_sorted)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
