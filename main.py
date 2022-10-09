import base64
from pyfiglet import Figlet

f = Figlet(font='slant')

print(f.renderText("ENADEBASE64"))

bord = """

1 - Encode
2 - Decode
"""

print(bord)
choice = input(": ")

def Encoder():
    x = input("Enter text: ")
    a = base64.b64encode(x.encode("utf-8"))
    print("Output: ",a.decode("utf-8"))


def Decoder():
    x = input("Enter base: ")
    a = base64.b64decode(x.encode("utf-8"))
    print("Output --> ",a.decode("utf-8"))
    input()

def Main():
    if choice == "1":
        Encoder()
    elif choice == "2":
        Decoder()
    else:
        print("Oops")

if __name__ == "__main__":
    Main()