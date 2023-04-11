#Here I define the main function
def main():
    x_user = input()
    x_user = hello_goodbye(x_user)
    print(x_user)

#The hello_goodbye function replace :) or :( by the emoji
def hello_goodbye(rp):
    rp = rp.replace(":)", "\U0001F642")
    rp = rp.replace(":(", "\U0001F641")
    return rp

#Call main()
main()
