import uuid
import datetime
import json
class manager:
    d = {}
    @staticmethod
    def parseSolution(data):
        j = json.loads(data)
        j["uuid"] = uuid.UUID(j["uuid"])
        return j

    def registerProblem(self, problem, groupId):
        code = uuid.uuid4()
        self.d[code] = {"start": datetime.datetime.now(), "groupId": groupId}
        return code

    def registerSolution(self, solution):
        self.d[solution["uuid"]]["end"] = datetime.datetime.now()
        self.d[solution["uuid"]]["solution"] = solution
        self.d[solution["uuid"]]["delta"] = self.d[solution["uuid"]]["end"] - self.d[solution["uuid"]]["start"] 

    
    