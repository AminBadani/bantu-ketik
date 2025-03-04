import re;

# Buka dan baca list kata yang ada di dalam dataset
def open_dataset(file_name: str):
    with open(file_name, 'r') as dataset:
        words = dataset.read().split('\n');
    
    return words


# Update list rekomendasi kata berdasarkan input pengguna
def update_list(old_list, input_word):
    # Cari kata yang awalanya sama dengan input
    prefix_pattern = re.compile('^' + input_word) 
    new_list = list();

    # Cek input dan masukkan ke dalam list jika pola-nya cocok
    if (len(input_word) > 0): 
        for word in old_list:
            if (len(input_word) > len(word)): continue;
            if (prefix_pattern.match(word)): new_list.append(word);
    
    return new_list