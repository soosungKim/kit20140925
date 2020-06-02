import json

def set_charact(name):
    character = {
        "name": name,
        "level" : 1,
        "hp" : 100,
        "item" : ["칼", "주먹", "후레쉬"]
    }
    with open('static/save.txt', 'w', encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4 )
    # print("{0}님 행운을 빕니다. 남은 체력 : {1}".format(character["name"], character["hp"]))
    return character


def save_game(filename, charact):
    f = open(filename, "w", encoding="uft-8")
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
        f.close()