def main():
    user_file_input = input("Please enter a file path: ")
    user_action = input("Please enter a task (sort/rev/last:) ")

    user_file_open = open(user_file_input, "r")

    if user_action == "sort":
        fo = user_file_open
        lines = fo.read()
        words = lines.split()
        words = list(dict.fromkeys(words))
        print(sorted(words))

    elif user_action == "rev":
        for line in user_file_open:
            line = line.strip("\n")
            print(line[::-1])
        user_file_open.close()

    elif user_action == "last":
        user_number_choice = int(input("Please enter a number: "))
        file_to_list = user_file_open.readlines()
        needed_lines = file_to_list[-user_number_choice:]
        for line in needed_lines:
            line = line.strip("\n")
            print(line)
        user_file_open.close()


if __name__ == "__main__":
    main()


# Course solution:


# """Applies manipulations on the content of a given file, according to a given command.
# :param: filePath: path of the file to manipulate (user's input)
# :param: Command: the command to apply. Can be sort/reverse/print last n raw's/ (user's input)
# :type filePath: string
# :type Command: int
# """
# filePath = input("Enter file path: ")
# command = input("Enter command: ")
# with open(filePath,'r') as inputFile:
# 	if(command=="sort"):
# 		l=list()
# 		for line in inputFile:
# 			line=line.split()
# 			for word in line:
# 				if(word not in l):
# 					l.append(word)
# 		l.sort()
# 		print (l)
# 	elif(command=="rev"):
# 		for line in inputFile:
# 			print(line[-2::-1])
# 	elif(command=="last"):
# 		fileData=inputFile.read()
# 		l=fileData.split('\n')
# 		num=int(input("Enter real number: "))
# 		for i in range(num):
# 			print(l[-num+i])
