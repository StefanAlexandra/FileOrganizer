import os
import shutil


def menu():
    path = input("Insert the path of press Q to exit the program: ")
    while not path_validation(path):
        if path.lower() == 'q':
            print("exit")
            exit()
        print("Invalid path!")
        path = input("Insert the path of press Q to exit the program: ")
    print("Valid path!")
    return path


def path_validation(path: str) -> bool:
    return os.path.isdir(path)


def map_extension_to_folder(path: str) -> dict:
    extension_mapping = {path + '\\' + folder: FILE_EXT_TYPES[i] for i, folder in enumerate(DIR_TYPES)}
    return extension_mapping


def create_dirs(path: str):
    for folder in DIR_TYPES:
        if not os.path.isdir(path + '\\' + folder):
            os.mkdir(path + '\\' + folder)


def list_all_files(path: str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files


def extract_file_extension(file: str) -> str:
    indexes = [i for i, ch in enumerate(file) if ch == '.']
    if indexes:
        file_extension = file[indexes[-1]::]
        return file_extension.lower()
    else:
        return 'no extension'


if __name__ == '__main__':

    DIR_TYPES = ['Pictures', 'Videos', 'Audio', 'PDF_files', 'Archives', 'Exe_files',
                 'ISO_files', 'Python_files', 'Torrent_files', 'Lightroom_files']

    FILE_EXT_TYPES = [['.png', '.img', '.jpg', '.jpeg'], ['.mp4', '.mov', '.avi'],
                      '.mp3', '.pdf', ['.rar', '.zip'], '.exe', '.iso', '.py', '.torrent',
                      ['.dng', '.xmp', 'lrtemplate']]


pathx = menu()
mapping = map_extension_to_folder(pathx)
create_dirs(pathx)
files = list_all_files(pathx)
for file in files:
    file_extension = extract_file_extension(file)
    for k, v in mapping.items():
        if file_extension in v:
            try:
                shutil.move(pathx + '\\' + file, k)
            except:
                print(f'{file} cannot be moved')
    print('Done!')
