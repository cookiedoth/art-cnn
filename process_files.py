import os
import re
import shutil

def separate_files(source, target):
    expr = re.compile('_\d+.jpg')
    os.makedirs(target, exist_ok=True)
    shutil.rmtree(target)
    for filename in os.listdir(source):
        pos = expr.search(filename).span()[0]
        artist = filename[:pos]
        artist_path = os.path.join(target, artist)
        os.makedirs(artist_path, exist_ok=True)
        shutil.copyfile(os.path.join(source, filename), os.path.join(artist_path, filename))

if __name__ == '__main__':
    separate_files('resized/resized', 'data')
