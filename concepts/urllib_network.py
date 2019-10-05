import urllib.request

URL = 'http://data.pr4e.org/romeo.txt'


file_hand = urllib.request.urlopen(URL)

for line in file_hand:
    print(line.decode().strip())

