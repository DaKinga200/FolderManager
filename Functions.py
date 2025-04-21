import os

def mult_fold(fold):
    n_folders = []
    for i in fold.split(','):
        n_fold = i.strip()
        n_folders.append(n_fold)
    return n_folders

def del_fold(route, list_folders):
    for i in list_folders:
        if os.path.exists(os.path.join(route, i)):
            os.rmdir(os.path.join(route, i))
            print(f'Folder {i} has been deleted from the route {route}')
        else:
            print(f'Tere is no folder with name {i} at route {route}')

def create_fold(route, list_folders):
    for i in list_folders:
        if os.path.exists(os.path.join(route, i)):
            print(f'It already exists a folder called {i} in the path {route}')
        else:
            os.makedirs(os.path.join(route, i))
            print(f'Folder {i} has been created in path {route}')