import urllib.request,urllib.parse,urllib.error

IMAGE_NAME = 'cover3.jpg'
URL = 'http://data.pr4e.org/' + IMAGE_NAME

image = urllib.request.urlopen(URL)
file_hand = open(IMAGE_NAME,'wb')

size = 0
while True:
    info = image.read(5120)
    if len(info) < 1: break
    size = size + len(info)
    file_hand.write(info)

print(size, 'characters copied')


# file_hand.write(image)
file_hand.close()
