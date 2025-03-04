import os.path;

# open txt file and store it on a variable
# only call this function on different .py file
def open_txt_different_python_file(file_name: str, stored_var: str = ''):
	
    # check if file is exists by the file_name
    if not os.path.isfile(file_name):
        print("file '" + file_name + "' does not exists");
        return None;

    # stored_var = '';
    with open(file_name, 'r') as file:
        stored_var = file.read().replace('\n', ' ').split(' ')
    print(stored_var)
    return stored_var