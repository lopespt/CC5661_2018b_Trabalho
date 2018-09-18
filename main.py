import flask
import gerador
import random

app = flask.Flask('servidor')

@app.route("/")
def index():
    p = random.randint(1,3)
    if p==1:
        return flask.jsonify(gerador.geraProblema1())
    elif p==2:
        return flask.jsonify(gerador.geraProblema2())
    else:
        return flask.jsonify(gerador.geraProblema3())



@app.route("/p1")
def p1():
    return flask.jsonify(gerador.geraProblema1())

@app.route("/p2")
def p2():
    return flask.jsonify(gerador.geraProblema2())

@app.route("/p3")
def p3():
    return flask.jsonify(gerador.geraProblema3())

app.run(use_reloader=True,host="0.0.0.0")