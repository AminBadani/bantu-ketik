import re;

def open_dataset(file_name: str):
    with open(file_name, 'r') as dataset:
        words = dataset.read().split('\n');
    return words

def update_list(old_list, input_word):
    prefix_pattern = re.compile('^' + input_word) 
    new_list = list();

    for word in old_list:
        if (len(input_word) > len(word)): continue;
        if (prefix_pattern.match(word)): new_list.append(word);
    
    return new_list