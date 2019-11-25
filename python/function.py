#my_list = [1, 2, 3, 4, 5]
my_list = "this is list"

def function_name(non_default_value, new_list='this is default'):
    print('non default value:' + str(non_default_value))
    print(new_list)
    return len(my_list)

var = function_name(my_list)  
print(var)  