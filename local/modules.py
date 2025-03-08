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

class ListKata:
    def __init__(self, dataset):
        self.dataset = dataset
        self.cache = {}
        self.list_lama = {}
        self.input_lama = ''

    def update_list(self, input_kata: str):
        prefix = re.compile('^' + input_kata);
        list_rekomendasi = {};

        if ( input_kata in self.cache )                             : return self.cache[input_kata]
        if ( len(input_kata) < len(self.input_lama) )               : self.list_lama = {}
        if ( input_kata[:len(self.input_lama)] != self.input_lama ) : self.list_lama = {}

        if (len(self.list_lama) == 0): 
            list_rekomendasi = [word for word in self.dataset if prefix.match(word)]
        else: 
            list_rekomendasi = [word for word in self.list_lama if prefix.match(word)]

        self.list_lama = list_rekomendasi
        self.input_lama = input_kata
        self.cache[input_kata] = list_rekomendasi;

        print(list_rekomendasi);

        return list_rekomendasi
    
test = ListKata(open_dataset('dataset_eng.txt'));
test.update_list('ba')
test.update_list('bal')
test.update_list('bala')
test.update_list('bla')
test.update_list('bela')