from snakebite.client import Client

client = Client('localhost', 54310)
for p in client.mkdir(['/foo/bar', '/input'], create_parent=True):
   print p
