import random

def cid(difficulty):
    cid_list = get_cid_list(difficulty)
    random.shuffle(cid_list)
    for elem in cid_list:
        return elem

def get_cid_list(difficulty):
    if difficulty == "easy":
        return ["1", "2", "3"]
    elif difficulty == "medium":
        return ["4", "5", "6"]
    elif difficulty == "hard":
        return ["7", "8", "9"]
    else:
        print("The difficulty is not defined!")
        return ["error"]
