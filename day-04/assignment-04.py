import json

def read_log(filename):
    count = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'INFO' in line:
                count['INFO'] = count.get('INFO' , 0) + 1
            elif 'WARNING' in line:
                count['WARNING'] = count.get('WARNING', 0) + 1
            elif 'ERROR' in line:
                count['ERROR'] = count.get('ERROR', 0) + 1
    return count

def write_json(filename, count):
    with open(filename, 'w') as file:
        json.dump(count, file)


count = read_log('app.log')
print(count)
write_json('output.json', count)
