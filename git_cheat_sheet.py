# -*- coding: utf-8 -*-
#-----Importar delsistema
import sys
import subprocess
#from time import sleep
#----------/
#-----Importar de PyQt4
#from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebView
#-----Importar adicionales
#----------/

#podria usar "apropos git-" para saber las paginas del man que contengan git-etc.

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
   #QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),lambda url:(manlist[-1]!=url.toString() and manlist.append(url.toString())  ,taby.setCurrentIndex(taby.indexOf(texty_2)),texty_2.setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[1])))
   #ejecuto el comando
   proc_out=subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
   #me aseguro de que no de error
   if proc_out[1]=="":
      #cambio de tab de una vez, ahrro algo de tiempo
      taby.setCurrentIndex(taby.indexOf(texty_2))
      #cargo la página
      texty_2.setHtml(proc_out[0])
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
texty = QtGui.QTextBrowser()
texty_2 = QtGui.QTextBrowser()
weby=QWebView()
#-----|-|-----/
#-----|-----/
#-----|-Layouts
layi_taby1 = QHBoxLayout()
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
weby.setHtml("<center><p style=\"font-size:300%;color:blue\"><b>Git's How Tos</b></p></center>")
manlist = ["git"]
#Para quitar el marco alrededor de tabby y por tanto de los widgets que contiene.
taby.setDocumentMode(True)

f.setPixelSize(12)
f.setBold(True)
taby.tabBar().setFont(f)

texty.setHtml(texto)
texty.setOpenLinks(False)



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
weby.load(howto)
texty_2.setHtml(subprocess.Popen(["man", "--troff-device=html" , manlist[0]],stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()[0])
#-----|-Crear tabs de los tabbars y tabwidgets
taby.addTab(widget_taby1,"uno")
taby.addTab(texty_2,"man")
taby.addTab(weby,"howtos(Loading...)")
for x in anclas:
    tabu.addTab(x)
#-----|-Llenar layouts
#-----|-|-grid es el Layout principal
grid.addWidget(boton,0,0)
grid.addWidget(boton2,0,1)
grid.addWidget(boton3,0,2)
grid.addWidget(taby,1,0,1,3)
#-----|-|-layi_taby es el Layout asignado a cada tab(1 es el primero)
layi_taby1.addWidget(tabu)
layi_taby1.addWidget(texty)
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
  #taby.setTabText(taby.indexOf(weby),"howtos(Loading...)")
  ##print("a")
#def howtos_changed():
  #taby.setTabText(taby.indexOf(weby),"howtos")
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
    ##texty_2.setHtml(subprocess.check_output(["man", "--troff-device=html" , url.toString()]))
    #texty_2.setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE).communicate()[0])
    ##texty.setOpenLinks(True)
    
#def anchory(i):
   #texty.scrollToAnchor(anclas[i])

#-----Connects
weby.loadStarted.connect(lambda : taby.setTabText(taby.indexOf(weby),"howtos(Loading...)"))
weby.loadFinished.connect(lambda :taby.setTabText(taby.indexOf(weby),"howtos"))
#QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),printuri)
#QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),lambda url:(manlist[-1]!=url.toString() and manlist.append(url.toString())  ,taby.setCurrentIndex(taby.indexOf(texty_2)),texty_2.setHtml(subprocess.Popen(["man", "--troff-device=html" , url.toString()],stdout=subprocess.PIPE).communicate()[0])))
QObject.connect(texty,SIGNAL("anchorClicked(QUrl)"),man_charge)
#QObject.connect(boton,SIGNAL("anchorClicked(QUrl)"),printuri)
boton.clicked.connect(texty_2.backward)
boton2.clicked.connect(lambda:weby.load(howto))
#tabu.currentChanged.connect(anchory)
tabu.currentChanged.connect(lambda i: texty.scrollToAnchor(anclas[i]))
#def anchorClicked(uri):
#  print uri
boton3.clicked.connect(lambda : texty_2.scrollToAnchor(" "))

#def roor():
  #print texty_2.source().toString()
  #for x in manlist:
     #print x
  ##print manlist[0]
  ##print manlist[len(manlist)-1]
#QObject.connect(texty_2,SIGNAL("sourceChanged(QUrl)"),roor)
#----------/
#-----Ultimos pasos
ventana.show()
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