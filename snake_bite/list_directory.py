from snakebite.client import Client

client = Client('localhost', 54310)
for x in client.ls(['/user/hduser/']):
   print x
