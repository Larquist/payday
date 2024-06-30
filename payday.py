import json

def main():
    bills = getJSONFromFile("./bills.json")

def getJSONFromFile(path):
    f = open(path, "r")
    return json.loads(f)

main()