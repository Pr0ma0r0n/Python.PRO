import time
meme_dict = {
            "KRINGE": "Something very strange or embarrassing",
            "LOL": "Something very funny",
            "ROFL": "a joke",
            "SCHISCH": "approval or delight",
            "CREEPY": "scary, frightening",
            "AGGRANDIZE": "get angry"
            }
name = input("Hello! My name is Explainer! What's your name?")
time.sleep(1)
print("Hello,", name,"!")
time.sleep(1)
print("My task is to explain incomprehensible words")
time.sleep(3)
while True:
    word = input("Enter an incomprehensible word (in capital letters!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        time.sleep(2)
    else:
        print("MISTAKE!!! The word was not found:(")
        time.sleep(2)
