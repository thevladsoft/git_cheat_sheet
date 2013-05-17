import sys
import subprocess
#from time import sleep
#from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#podria usar "apropos git-" para saber las paginas del man que contengan git-etc.

        
app = QtGui.QApplication(sys.argv) 
texty = QtGui.QTextBrowser()
texty_2 = QtGui.QTextBrowser()
vgrid = QtGui.QGridLayout()
taby = QTabWidget()
tabu = QTabBar()
#taby.setTabPosition(QTabWidget.West)
#tabu.setFixedHeight(60)


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
boton2 =  QPushButton("Eat me")
boton3 =  QPushButton("Drink me")
#boton.show()

texto=open("command line ruby cheat sheets.htm").read()
#texty.setText("<a href=\"http://\">Setup<\a> -----\ngit clone &lt;repo&gt;\n  clone the repository specified by &lt;repo&gt;; this is similar to \"checkout\" in\n  some other version control systems such as Subversion and CVS")
texty.setText(texto)
texty.setOpenLinks(False)
#texty.setOpenExternalLinks(True)
#texty.show()

vgrid= QVBoxLayout()
hgrid= QHBoxLayout()
grid=QGridLayout()

#hgrid.addWidget(boton)
#hgrid.addWidget(boton2)
#hgrid.addWidget(boton3)

#taby.addTab("uno")
#taby.addTab("dos")
taby.addTab(texty,"uno")
taby.addTab(texty_2,"man")

tabu.addTab("a")
tabu.addTab("b")
#tabu.setTabPosition(QTabWidget.West)
tabu.setShape(6)

#grid.addWidget(taby,0,0,1,3)

grid.addWidget(boton,0,1)
grid.addWidget(boton2,0,2)
grid.addWidget(boton3,0,3)

#vgrid.addWidget(hgrid.widget())
#vgrid.addWidget(texty)

#grid.addWidget(texty,2,0,1,3)
grid.addWidget(taby,1,1,1,3)

grid.addWidget(tabu,1,0,1,1)

ventana= QWidget()
#ventana.setLayout(vgrid)
ventana.setLayout(grid)
ventana.show()

#setLayout(vgrid)

def printuri(url):
  #QString uri
  #uri = "kioclient exec man:"+url.toString()
  if texty.openLinks()==False:
    print "kioclient exec man:"+url.toString()
  #print uri
  #subprocess.call("kioclient exec man:"+url.toString())
    #subprocess.call(["kioclient", "exec", "man:"+url.toString()])
    texty_2.setHtml(subprocess.check_output(["man", "--troff-device=html" , url.toString()]))
    #texty.setOpenLinks(True)

QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),printuri)
#QObject.connect(boton,SIGNAL("anchorClicked(QUrl)"),printuri)
boton.clicked.connect(texty.backward)
#def anchorClicked(uri):
#  print uri

sys.exit(app.exec_()) 
