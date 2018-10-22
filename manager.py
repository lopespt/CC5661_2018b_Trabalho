import uuid
import datetime
import json
class manager:
    d = {}
    check = []

    @staticmethod
    def correcao(usuario, correto):
        if(usuario["problema"]["tipo"]=="grafo"):
            print("problema Grafo")
            #print( correto["solucao"])
            #print(usuario["solucao"])
            return True #any([usuario["solucao"] == x for x in correto["solucao"]["solucoes"]])
        elif usuario["problema"]["tipo"]=="multiplicacao_matrizes":
            print("multiplicacao")       
            return usuario["solucao"] == correto["solucao"]
        elif usuario["problema"]["tipo"]=="ordenacao":
            print("ordenacao")
            return usuario["solucao"] == correto["solucao"]


    @staticmethod
    def parseSolution(data):
        j = json.loads(data)
        j["uuid"] = uuid.UUID(j["uuid"])
        return j

    def registerProblem(self, problem, groupId):
        code = uuid.uuid4()
        self.d[code] = {"start": datetime.datetime.now(), "groupId": groupId, "problema": problem}
        return code

    def registerSolution(self, solution):
        self.d[solution["uuid"]]["end"] = datetime.datetime.now()
        self.d[solution["uuid"]]["solucao"] = solution["solucao"]
        self.d[solution["uuid"]]["delta"] = self.d[solution["uuid"]]["end"] - self.d[solution["uuid"]]["start"]
        self.check.append(solution["uuid"]) 

    
    def nextCorrection(self):
        if(len(self.check)==0):
            return None
        code = self.check.pop(0)
        return {"problema": self.d[code]["problema"], "uuid": code}
   
    def registerCorrection(self, resposta):
        if manager.correcao(self.d[resposta["uuid"]], resposta ):
            self.d[resposta["uuid"]]["correto"] = True
            print("correto")
        else:
            self.d[resposta["uuid"]]["correto"] = False
            print("errado")

        return "ok"
