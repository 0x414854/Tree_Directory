import os

def print_directory_tree(folder_path, indent=''):
    num_files = 0
    num_folders = 0
    items = os.listdir(folder_path)
    items.sort()  
    for idx, item in enumerate(items):
        if item == '.DS_Store':
            continue

        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            last_item = idx == len(items) - 1
            print(indent + ('└── ' if last_item else '├── ') + item)
            num_files += 1
        elif os.path.isdir(item_path):
            last_item = idx == len(items) - 1
            print(indent + ('└── ' if last_item else '├── ') + item + '/')
            num_folders += 1
            sub_num_files, sub_num_folders = print_directory_tree(item_path, indent + ('    ' if last_item else '│   '))
            num_files += sub_num_files
            num_folders += sub_num_folders

    return num_files, num_folders


folder_path = '/Path/To/Your/Folder'
print('.')
total_num_files, total_num_folders = print_directory_tree(folder_path)
print('Total directory: {}'.format(total_num_folders))
print('Total files: {}'.format(total_num_files))
