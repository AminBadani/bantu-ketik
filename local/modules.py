import re;

# Buka dan baca list kata yang ada di dalam dataset
def open_dataset(file_name: str):
    with open(file_name, 'r') as dataset:
        words = dataset.read().split('\n');
    
    return words

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

        return list_rekomendasi