name = input("Type your name: ")
print(name + ", Welcome to the Jungle!\nINSTRUCTION!Choose the UPPER CASE WORDS as inputs.\n")

while True:
    answer = input("While awakening, you are on a jungle road.\nYou can go to LEFT or RIGHT. Choose carefully... ").lower()

    if answer == "left":
        answer = input("\nThere is a endless ocean with merely a glimpse of land.\nThe shore looks endless and dead.\nYou can SWIM or WALK around the shore.\nWhat will you do??? ").lower()

        if answer == "swim":
            print("\nThe ocean took you like the titanic. GAME OVER.")
            break

        elif answer == "walk":
            answer = input("\nAfter several hours of walking you reached to a mystical village.\nThe head of the village gave you two pills.\nLife or Death. RED or BLUE.\nWhat will you take??? ").lower()

            if answer == "red":
                print("\nYou just got upgraded.\n"+ name + ", Welcome to the matrix.\nDOWNLOADING 2.0...")
                break

            elif answer == "blue":
                print("\nThe cyanide took the life out of your body. GAME OVER.\n")
                break

            else:
                print("\nNot a valid option.\n")
                continue

        else:
            print("\nNot a valid option.\n")
            continue

    elif answer == "right":
        answer == input("\nThere is a mountain whose peak is unreachable.\nThe jungle road is full of wild surprises.\nYou can CLIMB or WALK around the mountain.\nWhat will you do??? ").lower()

        if answer == "climb":
            print("\nThe mountain took the breath out of your lungs. GAME OVER.")
            break

        elif answer == "walk":
            answer = input("\nAfter several hours of walking you reached to a mystical village.\nThe head of the village gave you two pills.\nLife or Death. RED or BLUE.\nWhat will you take??? ").lower()

            if answer == "red":
                print("\nYou just got upgraded.\n"+ name + ", Welcome to the matrix.\nDOWNLOADING 2.0...")
                break

            elif answer == "blue":
                print("\nThe cyanide took the life out of your body. GAME OVER.\n")
                break

            else:
                print("\nNot a valid option.\n")
                continue

        else:
            print("\nNot a valid option.\n")
            continue

    else:
        print("\nNot a valid option.\n")
        continue