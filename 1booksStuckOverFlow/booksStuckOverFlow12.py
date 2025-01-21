
from random import SystemRandom
import base64

secure_rand_gen = SystemRandom()
print([secure_rand_gen.randrange(10) for i in range(10)])

s = "hello world"
b = s.encode('utf-8')
print(b)
e = base64.b64encode(b)
print(e)
r = base64.b64decode(e)
print(r)