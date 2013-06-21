#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----Importar delsistema
import sys
import subprocess
import re
import os
#from time import sleep
#----------/
#-----Importar de PyQt4
#from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebView, QWebPage
#-----Importar adicionales
#----------/

#-----Setear el sistema
#Si leyese información adicional del sistema indispensable para el resto del programa, 
#como argumentos, version de python,etc, debo verlo aquí
os.chdir(sys.path[0])
print sys.version_info
#----------/

#podria usar "apropos git-" para saber las paginas del man que contengan git-etc. (ya lo hago.)

#-----Clases
class FingerTabBarWidget(QtGui.QTabBar):
    def __init__(self, parent=None, *args, **kwargs):
        self.tabSize = QtCore.QSize(kwargs.pop('width',92), kwargs.pop('height',21))
        QtGui.QTabBar.__init__(self, parent, *args, **kwargs)
                 
    def paintEvent(self, event):
        painter = QtGui.QStylePainter(self)
        option = QtGui.QStyleOptionTab()
 
        for index in range(self.count()):
            self.initStyleOption(option, index)
            tabRect = self.tabRect(index)
            tabRect.moveLeft(10)
            painter.drawControl(QtGui.QStyle.CE_TabBarTabShape, option)
            painter.drawText(tabRect, QtCore.Qt.AlignVCenter |\
                             QtCore.Qt.TextDontClip, \
                             self.tabText(index));
        painter.end()
    def tabSizeHint(self,index):
        return self.tabSize
#----------/

#-----Funciones
def man_charge(url):
   #QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),lambda url:(manlist[-1]!=url.toString() and manlist.append(url.toString())  ,taby.setCurrentIndex(taby.indexOf(texty[2])),texty[2].setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[1])))
   #ejecuto el comando
   #Debería poder hacer: subprocess.call(["man", "--troff-device=html", "man:"+url.toString()]) si la version de python>=2.7 (sys.version_info[1]>=7)
   proc_out=subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
   #me aseguro de que no de error
   if proc_out[1]=="":
      #cambio de tab de una vez, ahrro algo de tiempo
      taby.setCurrentIndex(taby.indexOf(texty[2]))
      #cargo la página
      stringo=re.sub("h1      { text-align: center }","h1      { text-align: center; background: #6B72FF; color: white;font: bold 24px;}",proc_out[0])
      stringo=re.sub("h1>","h1><p></p>",stringo)
      #print stringo
      #texty[2].setHtml(proc_out[0])
      texty[2].setHtml(stringo)
      #Si no es repetida, la agrego a la lista
      if manlist[-1]!=url.toString():
	manlist.append(url.toString())
	#si pongo un boton para retroceder, aquí es donde debería activarlo, porque es cuando
	#tendré un historial al cual retroceder
   #chequeo el largo de la lista, y si es muy larga, boto los valores viejos
      if len(manlist)>20:
	del manlist[0]
	
#idea funcion para retroceder:
#cuando quiera retroceder hago 'del manlist[-1]' para borrar el ultimo y
#cargo el nuevo ultimo usando manlist[-1] otra vez. Todo esto solamente si solamente si 'len(manlist)>1'
#y si 'len(manlist)==1' desactivo el boton para retroceder
#Sería un fastidio poner una funcion para avanzar así que no lo haré.

def ref_charge():
    startre = re.compile("^git[^ ]*", re.IGNORECASE | re.MULTILINE);
    #Debería poder hacer: subprocess.call(["apropos", "^git") si la version de python>=2.7 (sys.version_info[1]>=7)
    s = subprocess.Popen(["apropos", "^git"],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    if s[1]=="":
	#print "s"
	#texty[1].setHtml("<!DOCTYPE html><html><head><title>$ Git man pages</title>"\
	#"<link charset=\"utf-8\" href=\"/style.css\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\" />"\
	#"</head>"+'\n'+"<body><div class=\"content\"><pre>"+'\n'+\
	#startre.sub(lambda m:"<a href=\"%(s1)s\">%(s2)s </a>" % {'s1':m.group(0), 's2':m.group(0)} ,s)+\
	#"</pre></div></body></html>")
	texty[1].setHtml("<!DOCTYPE html><html><head><title>$ Git man pages</title><link charset=\"utf-8\" href=\"/style.css\" media=\"screen\" rel=\"stylesheet\" type=\"text/css\" /></head>"+'\n'+\
			 "<STYLE type=\"text/css\">BODY { background: white; color: black;font: 14px;font-family: Consolas;}A:link { font:bold;font-family: Consolas }P {background: #6B72FF; color: white;font: bold 24px;font-family: Consolas;}</STYLE>" 
			 "<body><div class=\"content\">"+"<pre>"+'\n'+"<p ><center>GIT's Commands REFERENCE</center></p>"+\
			 #startre.sub(lambda m:"<br> <a href=\"%(s1)s\">%(s2)s</a>" % {'s1':m.group(0), 's2':m.group(0)} ,s[0])+\
			 startre.sub(lambda m:"<br> <a href=\"%s\">%s</a>" % (m.group(0), m.group(0)) ,s[0])+\
			 "</pre></div></body></html>")
    else:
	print s[1]

#----------/

#------Declaracion de variable
app = QtGui.QApplication(sys.argv) 
manlist = []

#-----|-Widgets
widget_taby1 = QWidget()
ventana= QWidget()
#vgrid = QtGui.QGridLayout()
#-----|-|-Tabs
taby = QTabWidget()
tabu = FingerTabBarWidget()
#tabu = QTabBar()
#taby.setTabPosition(QTabWidget.West)
#tabu.setFixedHeight(60)
#-----|-|-Botones
#Estos botones podrian terminar llendose
boton =  QPushButton("Click me")
boton2 =  QPushButton("Eat me")
boton3 =  QPushButton("Drink me")
#-----|-|-texto
texty = []#0:cheat;1:ref;2:man;3:howto(qwebview)
#texty[0] = QtGui.QTextBrowser()
texty.append(QtGui.QTextBrowser())
texty.append(QtGui.QTextBrowser())
texty.append(QtGui.QTextBrowser())
texty.append(QWebView())
texty[len(texty)-1].find = lambda *args: QWebView.findText(texty[len(texty)-1],args[0],QWebPage.FindWrapsAroundDocument) if len(args)==1 else QWebView.findText(texty[len(texty)-1],args[0],QWebPage.FindWrapsAroundDocument|QWebPage.FindBackward)
texty[len(texty)-1].moveCursor = ()
finder = QtGui.QLineEdit()
#-----|-|-|-botones asociados
finder.next = QPushButton("Next")
finder.prev = QPushButton("Prev.")
#-----|-|-|-----/
finder.label = QtGui.QLabel("Search: ")
#texty[2] = QtGui.QTextBrowser()
#texty[1] = QtGui.QTextBrowser()
#weby=QWebView()
#-----|-|-----/
#-----|-----/
#-----|-Layouts
#layi_taby1 = QHBoxLayout()
layi_taby1 = QGridLayout()
grid=QGridLayout()
#-----|-----/


#-----|-Staticas
anclas = ["Setup","Config.","Info","Add/Del","Ignoring","Staging","Unstage","Commit"
          ,"Branch.","Merging","Cherry-Pick","Squash.","Conflicts","Sharing","Reverting"
          ,"Fix","Plumbing","Stashing","Remotes","Submodules","Patches","Tags","Archive"
          ,"Instaweb","Env vars.","Hist. change"]
          
texto=open("command line ruby cheat sheets.htm").read()
howto=QUrl(QString("https://www.kernel.org/pub/software/scm/git/docs/howto-index.html"))
p=app.palette()
f = taby.font()
#-----|-----/
#----------/

#texty = QtGui.QTextEdit()
#const QUrl uri

#web = QtWebKit.QWebView()
#local
#web.load(QtCore.QUrl("moonjupitermoons_gibbs_2000.jpg"))
#web.show()
#remoto
#web.load(QtCore.QUrl("http://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png"))
#web.show()

#boton.show()


#-----Configuracion inicial de widgets

#texty.setText("<a href=\"http://\">Setup<\a> -----\ngit clone &lt;repo&gt;\n  clone the repository specified by &lt;repo&gt;; this is similar to \"checkout\" in\n  some other version control systems such as Subversion and CVS")

#texty.setOpenExternalLinks(True)
#texty.show()

#vgrid= QVBoxLayout()
#hgrid= QHBoxLayout()

#hgrid.addWidget(boton)
#hgrid.addWidget(boton2)
#hgrid.addWidget(boton3)
ventana.setMinimumSize(150,300)
ventana.resize(650,630)

#-----|-Textos
texty[3].setHtml("<center><p style=\"font-size:300%;color:blue\"><b>Git's How Tos</b></p></center>")
manlist = ["git"]
#Para quitar el marco alrededor de tabby y por tanto de los widgets que contiene.
taby.setDocumentMode(True)

f.setPixelSize(12)
f.setBold(True)
taby.tabBar().setFont(f)

texty[0].setHtml(texto)
texty[0].setOpenLinks(False)
finder.label.setAlignment(Qt.AlignVCenter |Qt.AlignRight)
#finder.label.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)

texty[1].setOpenLinks(False)


#-----|-Tabs
widget_taby1.setStyleSheet(#"QTabBar::tab {font: normal;}"
                           "QTabBar::tab { border: 3px solid ;"
                           "border-bottom-color: #C0C0C0;"
                           "border-right-color: #C0C0C0;"
                           "border-left-color: #DEDEDE;"
                           "border-top-color: #DEDEDE;"
                           #"background: darkgray;"
                           "background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,"
                           "stop: 0 "+p.color(QPalette.Mid).name()+","#ffffff,"
                           "stop: 1.0  "+p.color(QPalette.Light).name()+");" #lightgray);"
                           "color: black;"
                           "padding: 5px;"
                           "border-top-left-radius: 15px;"
                           "border-bottom-right-radius: 10px ;"
                           #"border-top-left-radius: 0px;"
                           #"border-bottom-right-radius: 0px "
                           "}"
                           
                           #"QTabBar::tab:selected { background: gray; } ")
                           "QTabBar::tab:selected {"  
                           "background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,"
                           "stop: 0 "+p.color(QPalette.Dark).name()+","
                           "stop: 1.0  "+p.color(QPalette.Mid).name()+");}"
                           )
                           
tabu.setUsesScrollButtons(True)
tabu.setShape(6)  

#-----|-Layouts
grid.setContentsMargins(0,10,0,5)
layi_taby1.setContentsMargins(0,0,0,0)     
layi_taby1.setSpacing(0)
#-----|-----/
#----------/

#-----Iniciar Widgets
#-----|-Primeras cargas
texty[3].load(howto)

man_charge(QUrl(manlist[0]))
#texty[2].setHtml(subprocess.Popen(["man", "--troff-device=html" , manlist[0]],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0])

ref_charge()

#-----|-Crear tabs de los tabbars y tabwidgets
taby.addTab(widget_taby1,"Cheats")
taby.addTab(texty[1],"Comandos")
taby.addTab(texty[2],"man")
taby.addTab(texty[3],"howtos(Loading...)")
for x in anclas:
    tabu.addTab(x)
#-----|-Llenar layouts
#-----|-|-grid es el Layout principal
grid.addWidget(boton,0,0)
grid.addWidget(boton2,0,1)
grid.addWidget(boton3,0,2)
grid.addWidget(finder.label,1,0,1,1)
grid.addWidget(finder,1,1,1,1)
grid.addWidget(finder.next,1,2,1,1)
grid.addWidget(finder.prev,1,3,1,1)

grid.addWidget(taby,2,0,1,4)
#-----|-|-layi_taby es el Layout asignado a cada tab(1 es el primero)
layi_taby1.addWidget(tabu,1,0)
layi_taby1.addWidget(texty[0],1,1)
#-----|-|-----/
#-----|-----/
#----------/

#-----Asignar layouts
ventana.setLayout(grid)
#-----|-Asignar los de los widgets en los tabs (widget_taby'n' es el widget asignado a al tab 'n')
widget_taby1.setLayout(layi_taby1)
#-----|-----/
#----------/
#def howtos_changing(widget):
  #taby.setTabText(taby.indexOf(texty[3]),"howtos(Loading...)")
  ##print("a")
#def howtos_changed():
  #taby.setTabText(taby.indexOf(texty[3]),"howtos")
  ##print("b")







#taby.addTab("uno")
#taby.addTab("dos")
#taby.addTab(texty,"uno")






#tabu.addTab("a")
#tabu.addTab("b")
#tabu.tabRect(1).setHeight(100)
#tabu.repaint()
#widget_taby1.setStyleSheet("QTabBar{ color: yellow;font: bold 14px;}")
#widget_taby1.setStyleSheet("QTabBar::tab {border: 2px solid #C0C0C0;border-bottom-color: #C0C0C0; border-top-left-radius: 4px;border-top-right-radius: 8px;}")
#widget_taby1.setStyleSheet("QTabBar {border-top-left-radius: 4px}")
#widget_taby1.setStyleSheet("QTabBar::tab { border: 3px solid ;border-top-color: #C0C0C0;border-left-color: #C0C0C0;border-right-color: #DEDEDE;border-bottom-color: #DEDEDE;background: darkgray; color: white; padding: 5px;border-top-left-radius: 15px;border-bottom-right-radius: 10px }QTabBar::tab:selected { background: gray; } ")
#taby.setObjectName("taby")

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

                           
#taby.setBackgroundRole(QPalette.Base)
#taby.setAutoFillBackground(True)
#print widget_taby1.styleSheet()
#p=taby.palette()
#p.setColor(QPalette.Button, Qt.red)
#taby.setPalette(p)


#tabu.setTabPosition(QTabWidget.West)
print tabu.backgroundRole()


#grid.addWidget(taby,0,0,1,3)



#vgrid.addWidget(hgrid.widget())
#vgrid.addWidget(texty)

#grid.addWidget(texty,2,0,1,3)


#grid.addWidget(tabu,1,0,1,1)



#ventana.setLayout(vgrid)
#ventana.setLayout(grid)

#ventana.setMaximumSize(800,800)


#setLayout(vgrid)

#def printuri(url):
  ##QString uri
  ##uri = "kioclient exec man:"+url.toString()
  #if texty.openLinks()==False:
    #print "kioclient exec man:"+url.toString()
  ##print uri
  ##subprocess.call("kioclient exec man:"+url.toString())
    ##subprocess.call(["kioclient", "exec", "man:"+url.toString()])
    ##texty[2].setHtml(subprocess.check_output(["man", "--troff-device=html" , url.toString()]))
    #texty[2].setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE).communicate()[0])
    ##texty.setOpenLinks(True)
    
#def anchory(i):
   #texty.scrollToAnchor(anclas[i])
def busca():
  texty[0].find("git")


#-----Connects
texty[3].loadStarted.connect(lambda : taby.setTabText(taby.indexOf(texty[3]),"howtos(Loading...)"))
texty[3].loadFinished.connect(lambda :taby.setTabText(taby.indexOf(texty[3]),"howtos"))
#QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),printuri)
#QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),lambda url:(manlist[-1]!=url.toString() and manlist.append(url.toString())  ,taby.setCurrentIndex(taby.indexOf(texty[2])),texty[2].setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE).communicate()[0])))
QObject.connect(texty[0],SIGNAL("anchorClicked(QUrl)"),man_charge)
QObject.connect(texty[1],SIGNAL("anchorClicked(QUrl)"),man_charge)

QObject.connect(finder,SIGNAL("returnPressed()"),lambda:texty[taby.currentIndex()].find(finder.text()) or (texty[taby.currentIndex()].moveCursor(QTextCursor.Start),texty[taby.currentIndex()].find(finder.text())))
finder.next.clicked.connect(lambda:texty[taby.currentIndex()].find(finder.text()) or (texty[taby.currentIndex()].moveCursor(QTextCursor.Start),texty[taby.currentIndex()].find(finder.text())))
#bacward está raro
finder.prev.clicked.connect(lambda:texty[taby.currentIndex()].find(finder.text(),QTextDocument.FindBackward) or (texty[taby.currentIndex()].moveCursor(QTextCursor.End),texty[taby.currentIndex()].find(finder.text(),QTextDocument.FindBackward)))

#QObject.connect(boton,SIGNAL("anchorClicked(QUrl)"),printuri)
#boton.clicked.connect(texty[2].backward)
#boton.clicked.connect(busca)
#Este sería el que movería una página hasta el inicio:
boton.clicked.connect(lambda:texty[3].page().mainFrame().setScrollPosition(QPoint()))
boton2.clicked.connect(lambda:texty[3].load(howto))
#tabu.currentChanged.connect(anchory)
tabu.currentChanged.connect(lambda i: texty[0].scrollToAnchor(anclas[i]))
#def anchorClicked(uri):
#  print uri
boton3.clicked.connect(lambda : texty[2].scrollToAnchor(" "))

#def roor():
  #print texty[2].source().toString()
  #for x in manlist:
     #print x
  ##print manlist[0]
  ##print manlist[len(manlist)-1]
#QObject.connect(texty[2],SIGNAL("sourceChanged(QUrl)"),roor)
#----------/
#-----Ultimos pasos
ventana.show()
app.setWindowIcon(QIcon("git-logo.png"))
#----------/
#-----Comenzar la corrida
sys.exit(app.exec_()) 
#----------/
#-----/
#----/
#---/
#--/
#-/
#/