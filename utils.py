class TestResult:
    color = {
        True: "\033[92m",  # green
        False: "\033[91m"  # red
    }

    def __init__(self, scenarios: list,) -> None:
        self.scenarios = scenarios
        self.executer = None

    def show_result(self, result, params):
        print(f"{self.color[result == self.executer(**params)]}Function name : {self.executer.__name__} | parameters = {params} | Expected result : {result} | Actual result : {self.executer(**params)} \033[0m")

    def test_all_scenarios(self, executer):
        self.executer = executer
        for ele in self.scenarios:
            self.show_result(ele['result'], ele['params'],)
