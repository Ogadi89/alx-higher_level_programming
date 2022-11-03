#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
<<<<<<< HEAD
        print("[{}] {}".format(e.__class__.__name__, e)
=======
        print("[{}] {}".format(e.__class__.__name__, e))
>>>>>>> b2967ac8697e5b5fd9e1d1fc2bd6778fa607a2c1
