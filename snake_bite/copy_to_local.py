from snakebite.client import Client

client = Client('localhost', 54310)
for f in client.copyToLocal(['/input/input.txt'], '/tmp'):
   print f
