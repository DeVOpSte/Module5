




def increment(number):
    return str(number)


def value(func):
    def combo(number):
        if number == "0":
            return func(number) + ": John"
        if number == "1":
            return func(number) + ": Bob"
        if number == "2":
            return func(number) + ": Sam"
        if number == "3":
            return func(number) + ": Ana"
        if number == "4":
            return func(number) + ": Julia"
        if number == "5":
            return func(number) + ": Gerald"
        if number == "6":
            return func(number) + ": Frankie"
        if number == "7":
            return func(number) + ": Carly"
        if number == "8":
            return func(number) + ": Jeb"
        if number == "9":
            return func(number) + ": Julio"
        else:
            return func(number) + " is not a valid option"
    return  combo



#total = value(increment)
#final = total(input(" Name Generator: \n Enter a number between 0 and 9: \n"))
#print(final)


# part 2
def madLib(word1, word2,word3,word4):
    return "There was a man named " + word1 +". He worked as a " + word2 + \
    ", in Florida for " + word3 + " years. He has a pet " + word4 +"."

val1 = input("Enter a name: \n")
val2 = input("Enter a weird job: \n")
val3 = input("Enter a random number: \n")
val4 = input("Enter an exotic animal: \n")

print(madLib(val1,val2,val3,val4))


