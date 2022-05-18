# References:
#------------

# 1:Python Tutorial if __name__ == '_main__' -> https://www.youtube.com/watch?v=sugvnHA7ElY

import module1

# Since module1's main function has an if clause that ensures the code does not run via import, we can force it to run by calling it like that.
module1.main()

def main():
    print(f"Printing from module 2 - __name__ = {__name__}")

if __name__ == '__main__' :
    main()
