from time import sleep
import requests
import json

def get_champ_data():
    with open("champions.json", "r", encoding="utf8") as champs:
        data = json.load(champs)
        champions = {}
        for champ in data["data"]:
            entry = {
                "enemy_tips": champ['enemy_tips'],
                "ally_tips": champ['ally_tips']
                }
            champions[champ["name"].lower()] = entry

    with open("champions_data.json", "w", encoding="utf8") as champion_dataset:
        json.dump(champions, champion_dataset, indent=4)

def get_champ_list():
    with open("champions_data.json", "r", encoding="utf8") as ch:
        data = json.load(ch)
        champions = list(data.keys())
        return champions
