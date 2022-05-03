tags_dictionary = dict() 

user_input="1"

while user_input != "exit":
    user_input = input('Enter key & value separated by ":" ')
    print(f"User input: {user_input}")
    
    # Need this test to avoid running the code below when user_input="exit" which results in 'list index out of range' error!
    if user_input != "exit":
        key_value = user_input.split(":")
        print(f"key_value: {key_value}") 
        
        # Adds key:value pair to the tags dictionary.
        tags_dictionary[key_value[0]]=key_value[1]
        print(f"tags_dictionary: {tags_dictionary}")    
