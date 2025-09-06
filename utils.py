class TestResult:
    color = {True :"\033[92m",False:"\033[91m"}
    
    def __init__(self,scenarios,):
        self.scenarios = scenarios
        self.executer = None
        

    def find_result(self,result ,params):
        print(f"{self.color[result  == self.executer(params)]}|Function name : {self.executer.__name__} | parameters = {params} | Expected result : {result} | Actual result : {self.executer(params)}\n \033[0m")
        
    def test_all_scenarios(self,executer):
        self.executer = executer
        for ele in self.scenarios:
            self.find_result(ele['result'],ele['param'],)

