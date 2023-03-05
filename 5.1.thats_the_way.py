import os


# The function receives a path to a folder and returns all files starting with
# the letter sequence "deep" in that folder
def prefix_deep(path):
    files = []
    string = "deep"
    for filename in os.listdir(path):  # Go through files in a folder
        f = os.path.join(path, filename)
        if os.path.isfile(f):  # Checking that it is a file
            flag = True
            for i in range(len(string)):
                if len(filename) < len(string):  # Checking if the file name is smaller than the fixed string
                    break
                if string[i] != filename[i]:
                    flag = False
                    break

            if flag:  # If a file prefix is found that matches the constant string
                files += [filename]

    return files


print(prefix_deep("C:/Users/Adiel/PycharmProjects/excellentTeam/images"))
