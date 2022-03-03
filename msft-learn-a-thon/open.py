def main():
    try:
        open("config.txt")
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    # Grouping similar errors under the same error message.
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

# Python helper that tells the interpreter to execute the function main() when it's called on the terminal.
if __name__ =='__main__' :
    main()