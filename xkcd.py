import os
from datetime import date

if date.today().weekday() in (0, 2, 4):
    os.system("open /Applications/Google\ Chrome.app http://xkcd.com")
else:
    os.system("open /Applications/Google\ Chrome.app http://dynamic.xkcd.com/random/comic/")