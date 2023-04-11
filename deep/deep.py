#Get the user input
number = input("The Answer to the Great Question Of Life, the Universe and Everything is...?").strip().lower()

#Verify answer
match number:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")