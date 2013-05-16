import sys
import subprocess
#from time import sleep
#from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

app = QtGui.QApplication(sys.argv) 
texty = QtGui.QTextBrowser()
#texty = QtGui.QTextEdit()
#const QUrl uri

#web = QtWebKit.QWebView()
#local
#web.load(QtCore.QUrl("moonjupitermoons_gibbs_2000.jpg"))
#web.show()
#remoto
#web.load(QtCore.QUrl("http://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png"))
#web.show()
boton =  QPushButton("Click me")
#boton.show()

texto=open("command line ruby cheat sheets.htm").read()
#texty.setText("<a href=\"http://\">Setup<\a> -----\ngit clone &lt;repo&gt;\n  clone the repository specified by &lt;repo&gt;; this is similar to \"checkout\" in\n  some other version control systems such as Subversion and CVS")
texty.setText(texto)
texty.setOpenLinks(False)
#texty.setOpenExternalLinks(True)
texty.show()

def printuri(url):
  #QString uri
  #uri = "kioclient exec man:"+url.toString()
  print "kioclient exec man:"+url.toString()
  #print uri
  #subprocess.call("kioclient exec man:"+url.toString())
  subprocess.call(["kioclient", "exec", "man:"+url.toString()])

QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),printuri)

#def anchorClicked(uri):
#  print uri

sys.exit(app.exec_()) 
