import json
class ResultsCollector:
    def __init__(self):
        self.results = {}
     

    def add_result(self,key, result):
      
        self.results[key]=result

    def get_results(self):
  
        return self.results
    # Save dictionary results in json file
    def save_results(self):
        with open('results.json', 'w') as fp:
            json.dump(self.results, fp, indent=4)



resultcollector = ResultsCollector()