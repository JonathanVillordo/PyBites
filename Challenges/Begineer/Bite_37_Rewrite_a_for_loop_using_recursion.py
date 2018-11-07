def countdown_for(start=10):
    countdown_recursive(start)

def countdown_recursive(start=10):
    if start > 0:
        print(start)
        countdown_recursive(start - 1)
    else:
        print("time is up")


countdown_for()
