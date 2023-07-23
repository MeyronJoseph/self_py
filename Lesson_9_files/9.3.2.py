def my_mp4_playlist(file_path, new_song):
    """

    :param file_path:
    :param new_song:
    :return:
    """
    with open(file_path) as file:
        file_list = file.readlines()
    new_file_list = []
    for song in file_list:
        new_file_list.append(song.split(";"))
    new_file_list_len = len(new_file_list)
    if new_file_list_len > 3:
        new_file_list[2][0] = new_song
    elif new_file_list_len == 0:
        new_file_list.append(["\n"])
        new_file_list.append(["\n"])
        new_file_list.append([new_song + ";"])
    elif new_file_list_len == 1:
        new_file_list.append(["\n"])
        new_file_list.append([new_song + ";"])
    else:
        new_file_list.append([new_song + ";"])

    with open(file_path, "w") as file:
        for songs in new_file_list:
            file.writelines(";".join(songs))

    with open(file_path) as file:
        print(file.read())


# Course solution:


# """Changes the content of a playlist, read from a given file. The changed playlist is writen back to the same file.
# :param: file_name: the path of the file contains the playlist
# :param: new_song: a new name, to change the name of a song from the list
# :type: strings
# """
# def my_mp4_playlist(file_path, new_song):
# 	fid = open(file_path, "r")
# 	lines = fid.readlines()
# 	fid.close()
# 	if len(lines) >= 3:
# 		lines[2] = new_song + lines[2][lines[2].find(';'):]
# 		#open(file_path, "w").writelines(lines)
# 	else:
# 		for n in range(2 - len(lines)):
# 			lines.append("\n")
# 		lines.append(new_song+ ";")
# 		#open(file_path, "w").writelines(lines)
# 	#print(open(file_path, "r").read())
# 	text=''
# 	for i in range(len(lines)):
# 		text=text+lines[i]
# 	print(text)
