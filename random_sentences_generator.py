import random
names = ["Peter", "Kiril", "Anton", "Ivan", "Ioana", "Simona", "Alexander"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Sandanski", "Ahtopol", "Paris"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["strawberry", "car", "stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "far away the home", "in the office", "on the beach"]

def get_random_word(words):
    return random.choice(words)
input("Helo, this is your first random sentence! Please click [Enter].")


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    input("Click [Enter] to generate a new one.")
