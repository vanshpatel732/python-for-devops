import json

class LogAnalyzer():
    def __init__(self, file_name_r, file_name_w):
        self.read_file = file_name_r
        self.write_file = file_name_w
    
    def read_log(self):
        count = {}
        with open(self.read_file, 'r') as file:
            for line in file:
                if 'INFO' in line:
                    count['INFO'] = count.get('INFO' , 0) + 1
                elif 'WARNING' in line:
                    count['WARNING'] = count.get('WARNING', 0) + 1
                elif 'ERROR' in line:
                    count['ERROR'] = count.get('ERROR', 0) + 1
        return count
    
    def write_json(self):
        with open(self.write_file, 'w') as file:
            json.dump(self.read_log(), file)

    def print_log(self):
        print(self.read_log())
        
if __name__ == "__main__":
    log_object = LogAnalyzer('app.log', 'output.json')
    log_object.write_json()
    log_object.print_log()