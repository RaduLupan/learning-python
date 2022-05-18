# References:
#------------

# 1:Python Tutorial if __name__ == '_main__' -> https://www.youtube.com/watch?v=sugvnHA7ElY

def main():
    print(f"Printing from module 1 - __name__ = {__name__}")

# This ensures the code runs only when Python runs this file directly (not via import).
if __name__ == '__main__' :
    main()
