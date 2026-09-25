import random

# Magic 8 ball ASCII art
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
      "⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠞⠛⠋⠉⠉⠉⠉⠙⠛⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀\n"
      "⠀⠀⠀⠀⠀⣠⡾⠋⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀\n"
      "⠀⠀⠀⢀⡾⠋⢠⣾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀\n"
      "⠀⠀⢠⡞⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣶⣦⣄⠀⠀⠀⢳⡄⠀⠀\n"
      "⠀⠀⣾⠁⣰⣿⣿⠏⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⢛⣛⠛⣿⣿⣧⡀⠀⠈⣷⠀⠀\n"
      "⠀⢸⡏⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣇⠻⠿⠠⣿⣿⣿⣧⠀⠀⢹⡇⠀\n"
      "⠀⢸⡇⠀⣿⡟⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡟⢰⣿⣷⠈⣿⣿⡟⠀⠀⢸⡇⠀\n"
      "⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣄⣉⣡⣼⣿⡿⠁⠀⠀⣸⡇⠀\n"
      "⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⣿⡿⠟⠋⠀⠀⠀⢀⡿⠀⠀\n"
      "⠀⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀\n"
      "⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⠀⠀\n"
      "⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀\n"
      "⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⢦⣤⣄⣀⣀⣀⣀⣠⣤⡴⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀\n"
      "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

#Prompt for user to ask Magic 8 ball a question
prompt = input("Please ask a question and the Magic 8 ball will give you an answer, or Q to quit. \n")
def magic_8():
    print(f"The Magic 8 Ball\'s answers: {random.choice(answers)}\n")

while prompt != "Q":

    answers = ["Yes.", "No.", 
               "It is certain.", 
               "It is decidedly so.", 
               "Without a doubt.", 
               "Yes, definitely.", 
               "You may rely on it.", 
               "As I see it, yes.", 
               "Most likely.", 
               "Outlook good.", 
               "Signs point to yes.", 
               "Reply hazy, try again.", 
               "Ask again later", 
               "Better not tell you now", 
               "Cannot predict now.", 
               "Concentrate and ask again.", 
               "Don\'t count on it", 
               "My reply is no.", 
               "My sources say no.", 
               "Outlook not so good.", 
               "Very doubtful."]
    magic_8()
    prompt = input("Please ask a question and the Magic 8 ball will give you an answer, or Q to quit. \n")
    


