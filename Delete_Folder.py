from Functions import mult_fold, del_fold

route = input('Introduce the route where is the folder that you want to delete - ')

while True:
    multiples_folders = input('DO yo uwant to delete more than one folder?Y/N - ')

    if multiples_folders.upper() == 'Y':
        folders = input('Introduce the folders separated by comas: ')
        del_fold(route, mult_fold(folders))
        break
    elif multiples_folders.upper() == 'N':
        folder = input('Introduce the folder that you want to delete - ')
        del_fold(route, mult_fold(folder))
        break
    else:
        print('Introduce "Y" or "N"')
