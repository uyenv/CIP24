"""
TODO: Loop over a dictionary with 
    keys as English words
    values as Spanish words 
Execution: 
1. Check if user input was the same as Spanish word
2. Print correct/ incorrect each check
3. After the loop stops, print count of correct words
"""
def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
  
#Set up the count variable to count the times the user has answered correct answers
    correct_count = 0

#Loopover the dictionary
    for eng_word, spa_word in translations.items():
        #print("What is the Spanish translation for", eng_word, "? ")
        user_input = input(f"What is the Spanish translation for {eng_word}? ")
#Check user's answer
        if (user_input == spa_word):
            print("That is correct!")
            correct_count += 1
        else:
            print("That is incorrect, the Spanish translation for " + eng_word + " is " + spa_word + ".")
        print(" ")

    print("You got " + str(correct_count) + "/8 words correct, come study again soon!")
  
if __name__ == '__main__':
    main()
