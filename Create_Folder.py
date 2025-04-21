import os
from Functions import create_fold, mult_fold

while True:
    input1 = input('You want to create a new folder?(Y/N)').upper()
    if input1 == 'Y':
        while True:
            loc_route = input(f'You want to create the folder in the present location: {os.getcwd()}?Y/N ').upper()
            if loc_route == 'Y':
                folder_name = input('Introduce the name of the folder. If multiple folders, each folder must be separated by a coma - ')
                n_folder_name = mult_fold(folder_name)
                create_fold(os.getcwd(), n_folder_name)
                break
            elif loc_route == 'N':
                route = input('Introduce the route where you want to create the folder')
                folder_name = input('Introduce the name of the folder. If multiple folders, each folder must be separated by a coma')
                n_folder_name = mult_fold(folder_name)
                create_fold(route, n_folder_name)
                break
            else:
                print('Introduce "Y" or "N"')
    elif input1 == 'N':
        print('Goodbye')
        exit()
        break
    else:
        print('Introduce "Y" or "N"')











