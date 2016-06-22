from snakebite.client import Client

client = Client('localhost', 54310)
for p in client.delete(['/foo', '/input'], recurse=True):
   print p
