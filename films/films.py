import csv
import hashlib
import os

MD5_ENABLED = True
FILMS_DIRECTORY = "c:\Zdenek\Films"


def get_content_absolute_path(path):
    content = []
    for item in os.listdir(path):
        content.append(os.path.normpath(path + "/" + item))
    return content


def get_subdirectories(path):
    subdirectories = []
    content = get_content_absolute_path(path)
    while len(content) > 0:
        target = content[0]
        if os.path.isdir(target):
            subdirectories.append(target)
            content.remove(target)
            content += get_content_absolute_path(target)
        else:
            content.remove(target)
    return subdirectories


def get_md5(target):
    if MD5_ENABLED:
        with open(target, "rb") as data_file:
            file_hash = hashlib.md5()
            while chunk := data_file.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    else:
        return None


def get_file_details(path, filename):
    target = os.path.normpath(path + "/" + filename)
    print("Checking {0}".format(target))
    if not os.path.isfile(target):
        return [path, filename, False, None, None]
    file_size = os.stat(target).st_size
    file_md5 = get_md5(target)
    return [path, filename, True, file_size, file_md5]


def main():
    print("Hello, Films")

    films_directory = FILMS_DIRECTORY
    directories = [films_directory] + get_subdirectories(films_directory)

    films = []
    for directory in directories:
        content = os.listdir(directory)
        for item in content:
            target = os.path.normpath(directory + "/" + item)
            if os.path.isfile(target):
                films.append([directory, item])
    # [print(item) for item in films]

    film_details = []
    for item in films:
        film_details.append(get_file_details(item[0], item[1]))
    with open("films.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Path", "Filename", "Valid", "File Size", "File MD5"])
        for row in film_details:
            writer.writerow(row)


if __name__ == "__main__":
    main()
