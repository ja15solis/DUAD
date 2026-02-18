def list_of_songs (file_path_read):
    songs = []
    try:
        with open(file_path_read,'r') as file:
            songs = []
            for line in file.readlines():
                songs.append(line.strip())  #remove the 'enter at the end'
            songs.sort()
    except FileNotFoundError:
        print(f'The file path {file_path_read} was not found')
    return songs

def create_txt_with_ordered_songs (file_path_read,file_path_write):
    songs = list_of_songs(file_path_read)
    with open(file_path_write,'w',encoding ='utf-8') as file:
        for song in songs:
            file.writelines(song + '\n') ## the enter
    print (f'Correctly sorted the songs to \"{file_path_write}\"')

create_txt_with_ordered_songs('The Division Bell - Album Songs.txt','The Division Bell - Songs Ordered.txt')
