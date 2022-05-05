import random
import math

invisible_characters = "".join(['\u200B', '\u2060', '\u200C', '\u200D'])

def generate_invis_url():
    url = ""
    
    for i in range(25):
        url += invisible_characters[math.floor(random.randint(0, len(invisible_characters) - 1))]

    return url + '\u200B' 

if __name__ == "__main__":
    print(generate_invis_url())