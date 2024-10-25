import time

def output(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    print()

output("Hi, I am a mohamed")
time.sleep(1)
output("I am a python developer")
time.sleep(1)
output("I looking for learn assembly")
time.sleep(1)
output("Python is awesome")
time.sleep(1)
print("for learn python vist https://learnpython.org")
