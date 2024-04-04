import json

dataJson = {"name": "Minoo"}

with open("data.json", "w") as file:
    json.dump(dataJson, file, indent=4)


def userInput():
    someInput = input("Give Input :")
    anotherInput = input("Give Input :")
    return someInput, anotherInput


def creatData():
    while True:
        key, value = userInput()
        try:
            with open("data.json", "r") as file:
                dataJson = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            dataJson = {}
        dataJson[key] = value
        with open("data.json", "w") as file:
            json.dump(dataJson, file, indent=4)
        print("Update successful")
        exitInput = input("Press 'enter' to continue or 'no' to exit: ")
        if exitInput.lower() in ("no", "n"):
            break

creatData()
