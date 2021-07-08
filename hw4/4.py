import os

file_size = {}

file_100 = []
file_1000 = []
file_10000 = []
file_100000 = []

def get_only_files(dir):
    for file in os.listdir(dir):
        if os.path.isdir(f'{dir}/{file}'):
            get_only_files(f'{dir}/{file}')
        else:
            if file.split('.')[-1]:
                size = os.stat(f'{dir}/{file}').st_size
                if size // 100 < 1:
                    file_100.append(file)
                    file_size[100] = len(file_100)
                if size // 100 > 0 and size // 1000 < 1:
                    file_1000.append(file)
                    file_size[1000] = len(file_1000)
                if size // 1000 > 0 and size // 10000 < 1:
                    file_10000.append(file)
                    file_size[10000] = len(file_10000)
                if size // 10000 > 0:
                    file_100000.append(file)
                    file_size[100000] = len(file_100000)

get_only_files("files")
print(file_size)
