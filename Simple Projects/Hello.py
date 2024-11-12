
def hi():
    name=str(input('''Hi 
What's your name? ''')).strip().title()
    return hello(name)

def hello(who):
    print("Hello",who)

hi()