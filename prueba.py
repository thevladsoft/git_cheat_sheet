# -*- coding: utf-8 -*-
import re
import subprocess


#def changy(t):
#  u = "<a href=\""+t+"\">"+t+" </a>"
#  return u

#s = "git-tig start (foo) giti-tug end poo (8) dend"
#print "<!DOCTYPE html><html><head><title>$ Git man pages</title><link charset=\"utf-8\" href=\"/style.css\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\" /></head>"
#print "<body><div class=\"content\"><pre>"
s = subprocess.Popen(["apropos", "^git"],stdout=subprocess.PIPE).communicate()[0]
#lambda m: "el %s y" % m.group(1)
#s = re.sub("^git",lambda m: "<a href=\"%s\"> " % m.group(1),s)
#endre = re.compile("$", re.IGNORECASE | re.MULTILINE);
startre = re.compile("^git[^ ]*", re.IGNORECASE | re.MULTILINE);
#s = endre.sub("\n\n",s)
#s = re.sub("git$","\n\n",s)
#s = re.sub("(^git[^ ]+)",lambda m:"<a href=\"%(s1)s\"> %(s2)s </a>" % {'s1':m.group(1), 's2':m.group(1)} ,s,re.M)
s = "<!DOCTYPE html><html><head><title>$ Git man pages</title><link charset=\"utf-8\" href=\"/style.css\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\" /></head>"+'\n'+\
    "<body><div class=\"content\"><pre>"+'\n'+\
    startre.sub(lambda m:"<a href=\"%(s1)s\">%(s2)s </a>" % {'s1':m.group(0), 's2':m.group(0)} ,s)+\
    "</pre></div></body></html>"
#s = re.sub("(^git[^ ]+)",changy,s,re.MULTILINE)
#s = re.sub("(^git[^ ]+)","tig",s)

#s = re.sub("(^git[^ ]+)",lambda m:"%(language)s has %(language)s quote types." % {'language':m.group(1), 'bcd':m.group(1)} ,s)
print s

#u = re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', re.IGNORECASE)
#print u ,re.IGNORECASE,re.M
#print changy("ff")
#print "</div></body></html>"
#print '%(language)s has %(#)03d quote types.' % {'language': "Python", "#": 2}

#help(re.sub)