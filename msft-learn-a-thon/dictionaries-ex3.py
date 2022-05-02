tags = dict() 
user_input=""

while user_input != "exit": 
    user_input = input('Enter key & value separated by ":" ') 
    key_value = user_input.split(':')
    print(key_value) 
    tags[key_value[0]]=key_value[1]
    print(tags)    

