import os
from os import rename
from natsort import natsorted


def rename_files (path, new_name, extension):
    os.chdir(path)
    for (i, filename) in enumerate(natsorted(os.listdir(path))):
        os.rename(src = filename, dst = '{}{}{}'.format(new_name, i, extension))
        


rename_files('C:\\Users\\veron\\Escritorio\\normal-z-line', 'Normal-z-line', '.jpg')