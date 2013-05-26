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
f = taby.font()
f.setPixelSize(12)
f.setBold(True)
taby.setFont(f)

for x in anclas:
    tabu.addTab(x)
#tabu.addTab("a")
#tabu.addTab("b")
#tabu.tabRect(1).setHeight(100)
#tabu.repaint()
#widget_taby1.setStyleSheet("QTabBar{ color: yellow;font: bold 14px;}")
#widget_taby1.setStyleSheet("QTabBar::tab {border: 2px solid #C0C0C0;border-bottom-color: #C0C0C0; border-top-left-radius: 4px;border-top-right-radius: 8px;}")
#widget_taby1.setStyleSheet("QTabBar {border-top-left-radius: 4px}")
#widget_taby1.setStyleSheet("QTabBar::tab { border: 3px solid ;border-top-color: #C0C0C0;border-left-color: #C0C0C0;border-right-color: #DEDEDE;border-bottom-color: #DEDEDE;background: darkgray; color: white; padding: 5px;border-top-left-radius: 15px;border-bottom-right-radius: 10px }QTabBar::tab:selected { background: gray; } ")
#taby.setObjectName("taby")
p=app.palette()
print p.color(QPalette.Window).name()
#app.setStyleSheet("QTabBar::tab { border: 3px solid ;border-bottom-color: "+p.color(QPalette.Window).name() +";"##C2C7CB;"
                           #"border-right-color: "+p.color(QPalette.Window).name() +";"#C0C0C0;"
                           #"border-left-color: "+p.color(QPalette.Window).name() +";"#DEDEDE;"
                           #"border-top-color: "+p.color(QPalette.Window).name() +";"#DEDEDE;"
                           #"background: "+p.color(QPalette.Window).name() +";"
                           #"color: "+p.color(QPalette.Window).name() +";"#white;"
                           #" padding: 5px;"
                           #"border-top-left-radius: 15px;"
                           #"border-bottom-right-radius: 10px }QTabBar::tab:selected { background: gray; } ")
#taby.setStyleSheet("QTabBar::tab { border: 2px solid ;"
                           
                           #"border-bottom-color: "+p.color(QPalette.Mid).name() +";"##C2C7CB;"
                           ##"border-bottom-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           ##"stop: 0 "+p.color(QPalette.Mid).name()+","
                           ##"stop: 1.0  "+p.color(QPalette.Button).name()+");"
                           
                           #"border-right-color: "+p.color(QPalette.Mid).name() +";"#C0C0C0;"
                           #"border-left-color: "+p.color(QPalette.Button).name() +";"#DEDEDE;"
                           
                           #"border-top-color: "+p.color(QPalette.Button).name() +";"#DEDEDE;"
                           ##"border-top-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           ##"stop: 0 "+p.color(QPalette.Mid).name()+","
                           ##"stop: 1.0  "+p.color(QPalette.Button).name()+");"
                           
                           #"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           #"stop: 0 "+p.color(QPalette.Mid).name()+","#ffffff,"
                           #"stop: 1.0  "+p.color(QPalette.Button).name()+");" #lightgray);"
                                 
                           #"color: white;"
                           ##"font: bold;"
                           #" padding: 5px;"
                           
                           ##"border-top-left-radius: 15px;"
                           #"border-top-right-radius: 15px;"
                           ##"border-bottom-right-radius: 10px }QTabBar::tab:selected { background: gray; } ")
                           #"border-bottom-left-radius: 10px }"
                           ##"QTabBar::tab:selected { background: gray; } "
                           #"QTabBar::tab:selected { background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           #"stop: 0 "+p.color(QPalette.Dark).name()+","
                           #"stop: 1.0  "+p.color(QPalette.Mid).name()+");}"
                           
                           #"font: bold;"
                           #)
#taby.setStyleSheet("padding: 6px")
                           
widget_taby1.setStyleSheet(#"QTabBar::tab {font: normal;}"
                           "QTabBar::tab { border: 3px solid ;"
                           "border-bottom-color: #C0C0C0;"
                           "border-right-color: #C0C0C0;"
                           "border-left-color: #DEDEDE;"
                           "border-top-color: #DEDEDE;"
                           #"background: darkgray;"
                           "background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           "stop: 0 "+p.color(QPalette.Mid).name()+","#ffffff,"
                           "stop: 1.0  "+p.color(QPalette.Button).name()+");" #lightgray);"
                           "color: black;"
                           "padding: 5px;"
                           "border-top-left-radius: 15px;"
                           "border-bottom-right-radius: 10px ;"
                           #"border-top-left-radius: 0px;"
                           #"border-bottom-right-radius: 0px "
                           "}"
                           
                           #"QTabBar::tab:selected { background: gray; } ")
                           "QTabBar::tab:selected {"  
                           "background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,"
                           "stop: 0 "+p.color(QPalette.Dark).name()+","
                           "stop: 1.0  "+p.color(QPalette.Mid).name()+");}"
                           )
                           
#taby.setBackgroundRole(QPalette.Base)
#taby.setAutoFillBackground(True)
#print widget_taby1.styleSheet()
#p=taby.palette()
#p.setColor(QPalette.Button, Qt.red)
#taby.setPalette(p)


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
