import json

def transliterate_to_bangla(banglish: str) -> str:
    with open('mapping.json', 'r', encoding='utf-8') as file:
        mapping = json.load(file)
    
    words = banglish.split()
    bangla_words = []

    for word in words:
        if word in mapping:
            bangla_words.append(mapping[word]) 
        else:
            bangla_words.append(word)  

    return " ".join(bangla_words)


# banglish_input = "ami khub valo"
# print(transliterate_to_bangla(banglish_input))
