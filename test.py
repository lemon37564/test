import random
import string

for i in range(1000000):
    file_name = "".join(random.choice(string.ascii_letters) for i in range(10))
    with open("test/" + file_name, "w") as f:
        f.write(file_name)
