# greeting.py — starting file (repo owner creates this and pushes to GitHub)

def greet(name):
    message = "Hello, amanda branch" + name + "!"  # ← you and your partner will both edit this line
    return message

def farewell(name):
    return "Goodbye, amanda branch" + name + "!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
