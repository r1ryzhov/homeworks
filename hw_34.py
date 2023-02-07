import json

data_zxc = {}
with open('zxc.json', 'w') as f:
    json.dump(data_zxc, f)
    
def register (login, passwd):
    with open('zxc.json', 'r') as f:
        data_zxc = json.load(f)
    if login not in data_zxc.keys():
        data_zxc[login] = passwd
        with open('zxc.json', 'w') as f:
            json.dump(data_zxc, f)
    else:
        print('account already exists')