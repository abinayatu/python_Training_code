"""
Web server:
flask has builtin web server, we can use it for development purpose
"""

"""
In this release, creating API for providing access to
read existing records from our table my_table
"""

# -----------
# Create APP
#############
import flask
my_rest_api_app = flask.Flask(__name__) # __name__, file name will print
########################

# -----------
# END POINT - 1: http://127.0.0.1:5000/getdbdata Mapped to route("/getdbdata")
#############
@my_rest_api_app.route("/getdbdata", methods=["GET"])
def get_db_data_function():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    # import json
    # return json.dumps(my_db_result)
    return flask.jsonify(my_db_result)
########
#
#################

@my_rest_api_app.route("/getip", methods=["GET"])

def get_db_data_function2():
    import sqlite3
    my_db_connection = sqlite3.connect("my_database.sqlite3")
    my_db_cursor = my_db_connection.cursor()
    my_db_cursor.execute("SELECT * FROM MY_TABLE")
    my_db_result = my_db_cursor.fetchall()
    # import json
    # return json.dumps(my_db_result)

    data_n_json= flask.jsonify(my_db_result)
# -----------
# Run the builtin server
#############
my_rest_api_app.run() # default IP=127.0.0.1 port=5000
# my_rest_api_app.run(host='192.168.1.4', port=5000)
########################