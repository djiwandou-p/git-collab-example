# greeting.py — starting file (repo owner creates this and pushes to GitHub)

def greet(name):
    message = "Hello, " + name + "!"  # ← you and your partner will both edit this line
    return message

def farewell(name):
    return "Goodbye, " + name + "!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
