import flask
import gerador
import random
import manager
from flask import request

app = flask.Flask('servidor')
m = manager.manager()

@app.route("/solucao",methods=['POST','GET'])
def solucao():
    sol = m.parseSolution(request.data)
    m.registerSolution(sol)
    #print(m.d[sol["uuid"]])
    return "ok"

@app.route("/")
def index():
    idGrupo = request.args.get("idGrupo")
    p = random.randint(1,3)
    if p==1:
        prob = gerador.geraProblema1()
    elif p==2:
        prob = gerador.geraProblema2()
    else:
        prob = gerador.geraProblema3()

    code = m.registerProblem(prob, idGrupo)
    return flask.jsonify({"uuid": code, "problema": prob})



@app.route("/p1")
def p1():
    return flask.jsonify(gerador.geraProblema1())

@app.route("/p2")
def p2():
    return flask.jsonify(gerador.geraProblema2())

@app.route("/p3")
def p3():
    return flask.jsonify(gerador.geraProblema3())

app.run(use_reloader=True,debug=False,host="0.0.0.0",port=5000)
