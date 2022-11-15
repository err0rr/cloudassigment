from flask import Flask
from markupsafe import escape
import integration as intigration
from flask import jsonify
import json

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Hello, Lets do some Numerical integral! Go to <a href=/numericalintegralservice/0/3.14159>Integration service</a> "

@app.route("/numericalintegralservice/<lower>/<upper>")
def compute(lower, upper):
    #print("Query with {} and {}".format(lower, upper))

    # Convert string parameters to floats
    lower = float(lower)
    upper = float(upper)
    N_list = [10, 100, 100, 1000, 10000, 100000, 1000000]
    results = []
    html = "<h3>Numerical Integral Service from {} to {} of abs(sin(x))</h3>".format(lower, upper)
    for i in N_list:
        results.append(intigration.intigration(lower, upper, i))
    html +="<h4>Iterations : Values</h4>"
    for i in range(len(results)):
        html+="<h4>{} : {}</h4>".format(N_list[i], results[i])
        html+= "{}".format(jsonify(key1= N_list[i], key2=results[i]))

    return html
