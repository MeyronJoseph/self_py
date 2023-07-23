def my_mp3_playlist(file_path):
    """

    :param file_path:
    :return:
    """
    with open(file_path) as file:
        file_list = file.readlines()
    songs_number = len(file_list)
    song_len_list = []
    file_lists = []
    for song in file_list:
        file_lists.append(song.split(";"))
    for length in file_lists:
        song_len_list.append(length[2])
    sorted_length_list = sorted(song_len_list)
    longest_song = sorted_length_list[-1]
    the_longest_song = ""
    for song in file_lists:
        if str(longest_song) in song:
            the_longest_song += song[0]

    singer_list = []
    for singer in file_lists:
        singer_list.append(singer[1])
    times_singer = max(singer_list, key=singer_list.count)
    return the_longest_song, songs_number, times_singer


# Course solution:


# """Displays info of playlist, read from a file: the longest song, number of songs in list, the most frequent singer
# :param: file_path: the path to playlist file
# :type: string
# :return: info about the playlist
# :rtype: tuple
# """
# def my_mp3_playlist(file_path):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	song_lengths, artist_count = {}, {}
# 	length = len(lines)
# 	for line in lines:
# 		line_list = line.split(';')
# 		song_lengths[line_list[0]] = line_list[2]
# 		if line_list[1] in artist_count.keys():
# 			artist_count[line_list[1]] = artist_count[line_list[1]] + 1
# 		else:
# 			artist_count[line_list[1]] = 1
# 	return max(song_lengths, key=song_lengths.get), length, max(artist_count, key=artist_count.get)
