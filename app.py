#!/usr/bin/python3
"""Module of the APP configuration"""

from Flask import render_template
app = Flask(__name__)


@app_views.route("/", methods=["GET"], strict_slashes=False)
def index():
    return


if __name__ == '__main__':
    
app.run(host='0.0.0.0', port='5000', debug=True)