# -*- coding: utf-8 -*-
import sys
import subprocess
#from time import sleep
#from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebView

#podria usar "apropos git-" para saber las paginas del man que contengan git-etc.

        
app = QtGui.QApplication(sys.argv) 
texty = QtGui.QTextBrowser()
texty_2 = QtGui.QTextBrowser()
#vgrid = QtGui.QGridLayout()
taby = QTabWidget()
tabu = QTabBar()
#taby.setTabPosition(QTabWidget.West)
#tabu.setFixedHeight(60)

anclas = ["Setup","Config.","Info","Add/Del","Ignoring","Staging","Unstage","Commit"
          ,"Branch.","Merging","Cherry-Pick","Squash.","Conflicts","Sharing","Reverting"
          ,"Fix","Plumbing","Stashing","Remotes","Submodules","Patches","Tags","Archive"
          ,"Instaweb","Env vars.","History change"]

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

weby=QWebView()

#vgrid= QVBoxLayout()
#hgrid= QHBoxLayout()
grid=QGridLayout()

#hgrid.addWidget(boton)
#hgrid.addWidget(boton2)
#hgrid.addWidget(boton3)
howto=QUrl(QString("https://www.kernel.org/pub/software/scm/git/docs/howto-index.html"))
weby.setHtml("<center><p style=\"font-size:300%;color:blue\"><b>Git's How Tos</b></p></center>")
weby.load(howto)

#def howtos_changing(widget):
  #taby.setTabText(taby.indexOf(weby),"howtos(Loading...)")
  ##print("a")
  
#def howtos_changed():
  #taby.setTabText(taby.indexOf(weby),"howtos")
  ##print("b")

weby.loadStarted.connect(lambda : taby.setTabText(taby.indexOf(weby),"howtos(Loading...)"))
weby.loadFinished.connect(lambda :taby.setTabText(taby.indexOf(weby),"howtos"))

widget_taby1 = QWidget()
layi_taby1 = QHBoxLayout()
widget_taby1.setLayout(layi_taby1)

#taby.addTab("uno")
#taby.addTab("dos")
#taby.addTab(texty,"uno")
taby.addTab(widget_taby1,"uno")
taby.addTab(texty_2,"man")
taby.addTab(weby,"howtos(Loading...)")

for x in anclas:
    tabu.addTab(x)
#tabu.addTab("a")
#tabu.addTab("b")


#tabu.setTabPosition(QTabWidget.West)
print tabu.backgroundRole()
tabu.setUsesScrollButtons(True)

tabu.setShape(6)

#grid.addWidget(taby,0,0,1,3)

grid.addWidget(boton,0,1)
grid.addWidget(boton2,0,2)
grid.addWidget(boton3,0,3)

#vgrid.addWidget(hgrid.widget())
#vgrid.addWidget(texty)

#grid.addWidget(texty,2,0,1,3)
grid.addWidget(taby,1,1,1,3)

#grid.addWidget(tabu,1,0,1,1)
layi_taby1.addWidget(tabu)
layi_taby1.addWidget(texty)

ventana= QWidget()
#ventana.setLayout(vgrid)
ventana.setLayout(grid)
ventana.setMinimumSize(150,300)
#ventana.setMaximumSize(800,800)
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
    #texty_2.setHtml(subprocess.check_output(["man", "--troff-device=html" , url.toString()]))
    texty_2.setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE).communicate()[0])
    #texty.setOpenLinks(True)
    
def anchory(i):
   texty.scrollToAnchor(anclas[i])

QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),printuri)
#QObject.connect(boton,SIGNAL("anchorClicked(QUrl)"),printuri)
boton.clicked.connect(texty_2.backward)
boton2.clicked.connect(lambda:weby.load(howto))
tabu.currentChanged.connect(anchory)
#def anchorClicked(uri):
#  print uri

sys.exit(app.exec_()) 
