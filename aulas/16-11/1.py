import yaml

with open("c002.yaml",'r') as f:
    for data in yaml.load_all(f):
        print(data)
