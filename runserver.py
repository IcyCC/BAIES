import os

os.system("gunicorn -w 6 -t 10000 -b 0.0.0.0:{} BAIES:app".format(5000))