tags_dictionary = dict() 

user_input="1"

while True:   
    user_input = input('Enter key & value separated by ":" or "exit" to finish \n')
    print(f"User input: {user_input}")
    
    if user_input == "exit":
        break

    key_value = user_input.split(":")
    print(f"key_value: {key_value}") 
        
    # Adds key:value pair to the tags dictionary.
    tags_dictionary[key_value[0]]=key_value[1]
    print(f"tags_dictionary: {tags_dictionary}")    
