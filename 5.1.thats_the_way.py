import os


def prefix_deep(path):
    """
    Retrieves all files in the specified path that start with the prefix "deep".

    Args:
        path (str): The path to the folder.

    Returns:
        list: A list of filenames starting with the prefix "deep".

    """
    return [filename for filename in os.listdir(path) if
            os.path.isfile(os.path.join(path, filename)) and filename.startswith("deep")]


print(prefix_deep("C:/Users/Adiel/PycharmProjects/excellentTeam/EX1/images"))
