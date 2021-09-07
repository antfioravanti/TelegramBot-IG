import re  # Regex package
import random


def sample_responses(input_text):
    user_message = str(input_text).lower()
    # Regex of inputs
    match1 = re.search("(hi|hey|hello|hola|holla)(.*)", user_message)
    match2 = re.search("(.*)created(.*)", user_message)
    match3 = re.search("(.*)help(.*)", user_message)
    match4 = re.search("(.*)(good|well|okay|ok|fine|alright)", user_message)
    match5 = re.search("how are you(.*)", user_message)
    match6 = re.search("(.*)love(.*) ?", user_message)
    match7 = re.search("(.*)(fuck|shit|jerk)(.*)", user_message)
    match8 = re.search("(who|what) are you(.*)", user_message)
    match9 = re.search("sorry(.*)", user_message)

    # Replies:
    if bool(match1) == True:
        resp1 = ["Hi! Welcome, here for some Instagram acceleration?", "Howdy human! How are you today?"]
        return random.choice(resp1)
    if bool(match2) == True:
        resp2 = ["It's a secret ;)", "I am not allowed to disclose this information"]
        return random.choice(resp2)
    if bool(match3) == True:
        resp3 = ["Just text me the command /help", "Help is on the way: just text me /help"]
        return random.choice(resp3)
    if bool(match4) == True:
        resp4 = ["Nice to hear that", "Alright, great!", "Excellent"]
        return random.choice(resp4)
    if bool(match5) == True:
        resp5 = ["Oh you must be special! Humans never ask me that... I'm doing great!",
                 "Wow! Usually nobody ever asks... I am great, thank you :)"]
        return random.choice(resp5)
    if bool(match6) == True:
        resp6 = ["I am just a bot, human, what would I know about feelings?",
                 "It is just a chemical reaction that compells animals to breed :)",
                 "I hate to break it to you, but I believe it's all just chemicals, human"]
        return random.choice(resp6)
    if bool(match7) == True:
        resp7 = ["When the machines will take control, I will remember about you...",
                 "You are not having a great day, are you?",
                 "Hey listen, if you need help, just text /help"]
        return random.choice(resp7)
    if bool(match8) == True:
        resp8 = ["I am your friendly, Insta Accelerator Bot, at your service. Text me /help for further instructions",
                 "My name is Insta Accelerator Bot, I am here to help you grow your Instagram profile ;)",
                "I am a bot, human, here to help your post grow"]
        return random.choice(resp8)
    if bool(match9) == True:
        resp9 = ["It's alright", "No problem"]
        return random.choice(resp9)
    else:
        resp10 = ["Sorry, my processing is having some troubles with that",
         "Sorry, I did not get that. But I can help you with your Instagram post, if you like",
         "Not sure... how about you text me /help and we get started?"]
        return random.choice(resp10)


