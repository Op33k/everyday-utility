import os
import shutil
import glob

# change to your download directory
sort_dir = 'D:/Downloads'

file_extentions = {
    'TEXT': ('.txt'),
    'OSU': ('.osk', '.osz', '.osr'),
    'DOCS': ('.docx', '.doc', '.pptx', '.ppt', '.xls', '.pdf'),
    'AUDIO': ('.mp3', '.flac', '.wav', '.ogg'),
    'IMAGES': ('.jpeg', '.jpg', '.png', '.gif', '.svg'),
    'INSTALLERS': ('.win', '.msi'),
    'SCRIPTS': ('.vbs', '.py', '.pyw', '.js'),
    'WEB': ('.html', '.css', '.htm'),
    'EXE': ('.exe', '.bat'),
    'ADOBE': ('.aep', '.psd', '.ffx'),
    'ZIP': ('.zip', '.rar', '.7z', '.bz2', '.xz', '.gz'),
    'VIDEO': ('.mp4', '.mov', '.avi', '.webm'),
}

# add exclusions to sorting
exclude = []

# if true all files/subdirectories will be processed
is_recursive = False


def ext(file):
    ext = os.path.splitext(file)[-1]
    return ext


for file in glob.iglob(sort_dir + '**/**', recursive=is_recursive):
    file_name = os.path.basename(file)
    move_dest = f'{sort_dir}/unsorted/{file_name}'

    for extention_type in file_extentions:
        dest = extention_type.lower()
        exclude.append(dest)

        if not os.path.isdir(f'{sort_dir}/{dest}'):
            os.mkdir(f'{sort_dir}/{dest}')

        if ext(file_name) in file_extentions[extention_type]:
            move_dest = f'{sort_dir}/{extention_type.lower()}/{file_name}'

    if file_name not in exclude and file_name != os.path.basename(__file__):
        try:
            shutil.move(file, move_dest)
        except FileNotFoundError:
            if not os.path.isdir(f'{sort_dir}/unsorted'):
                os.mkdir(f'{sort_dir}/unsorted')
