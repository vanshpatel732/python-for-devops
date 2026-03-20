import argparse

class LogAnalyser():

    def __init__(self):
        self.read_file = self.argument_parser().file
        if self.argument_parser().out is not None:
            self.write_file = self.argument_parser().out
        if self.argument_parser().level is not None:
            self.level = self.argument_parser().level

    def argument_parser(self):
        parser = argparse.ArgumentParser(description="A simple script")
        parser.add_argument("--file", required=True, type=str, help="The name of log")
        parser.add_argument("--out", type=str, help="Output file name")
        parser.add_argument("--level", type=str, help="Level to filter")
        args = parser.parse_args()
        return args
    
    def read_log(self):
        count = {}
        with open(self.read_file, 'r') as file:
            for line in file:
                if self.level in line:
                    count[self.level] = count.get(self.level , 0) + 1
        print(count)
        return count

log_object = LogAnalyser()
log_object.argument_parser()
log_object.read_log()