import json

with open("templates/jsonsaiprofiles/profiles.json") as f:
    data = json.load(f)

lengthOfdata = len(data["users"])
print(lengthOfdata)
for i in range(lengthOfdata):
    print(data["users"][i]["name"])
