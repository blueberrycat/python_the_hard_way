from sys import argv
script, name = argv

print "Hi %s, how are you?" % name
answer = raw_input(">>")

print "So, I'm %s too" % answer