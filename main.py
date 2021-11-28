import base64

data = []
with open("./imgcache/Bike 1_0.jpg", "rb") as file:
    string = str(base64.b64encode(file.read()))[2:-1]
    size = len(string)
    for i in range(0, size, 3000):
        data.append(string[i:i + 3000])
    if i < size:
        data.append(string[i:size])

with open('./hello_level.jpeg', 'wb') as decodeit:
    decodeit.write(base64.b64decode(''.join(data)))

# https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/
