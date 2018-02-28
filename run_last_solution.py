from glob import glob
from os import path

options = sorted([path for path in glob('.' + path.sep + 'Solutions' + path.sep + '*')
                 if '__' not in path])

last = options[-1]

last_name = last.split(path.sep)[-1].split('.')[0]
__import__('Solutions.' + last_name)