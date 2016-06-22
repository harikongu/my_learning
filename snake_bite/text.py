from snakebite.client import Client

client = Client('localhost', 54310)
for l in client.text(['/input/input.txt']):
   print l
