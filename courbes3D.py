##LIBRAIRIES
import numpy as np
import math as m
import matplotlib.pyplot as plt
import random
import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

##INITIALISATION DES VARIABLES UTILISATEURS
print("Initialisation...")
#longueur d'une pale (m)
rayon = 56  
#hauteur de l'eolienne (m)
H = 80 
#modele eolienne (texte)
nom_eolienne = "SIEMENS"

#acceleration de pesanteur (m/s^-2)
g = 9.81 
#nombre de points pour les graphiques
nbpts=250

##FIN DE L'INITIALISATION DES VARIABLES UTILISATEURS
xf=np.zeros((nbpts,nbpts)) #Longueurs d'impact au sol
vitesses_impact = np.zeros((nbpts,nbpts)) #Vitesses (y)
angles_impact = np.zeros((nbpts,nbpts)) #Vitesses (y)

vitesses=np.linspace(0.1,10,nbpts)
vitrad =vitesses*2*np.pi/60 #conversion de la vitesse en rad/s
angles=np.linspace(0.1,360,nbpts)
anglesrad=angles*np.pi/180


##FONCTIONS
def t0(R, V, a):
    """Renvoi t pour y=0 (temps auquel le bloc de glace est au sol"""
    return (- R * V * m.cos(a) - m.sqrt(R**2 * V**2 * m.cos(a)**2 + 2 * g * (R*m.sin(a) + H))) / (-g)

def position(R, V, a, t):
    """Renvoi le tuple de position (x,y) en fonction du rayon R, de la vitesse V, de l'angle a AU temps t"""
    
    x = -R * V * m.sin(a) * t + R * m.cos(a)
    y = R * V *m.cos(a) * t - (1/2) * g * t**2 + R * m.sin(a) + H
    return (x,y)
    
def vitesse_acceleration(R, V, a, t):
    """Renvoi le tuple de vitesses et d'accelerations(vx,vy, ax, ay) en fonction du rayon R, de la vitesse V, de l'angle a AU temps t"""
    
    vx = -R * a * m.sin(a)
    vy = R * a * m.cos(a) - g * t
    
    ax = 0
    ay = -g
    return(vx,vy,ax,ay)
    
def annotate():
    """Annote les courbes avec les infos de l'eolienne"""
    additional_infos = "R = " + str(rayon) + "m\nH = " + str(H) + "m"
    ax.annotate(additional_infos,
            xy=(0.5, 0), xytext=(0, 10),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=14, ha='center', va='bottom')
    ax2.annotate(additional_infos,
            xy=(0.5, 0), xytext=(0, 10),
            xycoords=('axes fraction', 'figure fraction'),
            textcoords='offset points',
            size=14, ha='center', va='bottom')
    
print("Initialisation terminee") 
##CALCULS
print("Calculs en cours...")
va = (0,0,0,0)
for i in range(len(anglesrad)):
    for j in range(len(vitrad)):
        tpsfinal=t0(rayon,vitrad[j],anglesrad[i])
        xf[i,j]=position(rayon,vitrad[j],anglesrad[i],tpsfinal)[0] #Distance
        
        va = vitesse_acceleration(rayon,vitrad[j],anglesrad[i],tpsfinal)

        vitesses_impact[i,j]=m.sqrt(va[0]**2+va[1]**2) #Normes de vitesse
        if va[0] > 0:
            angles_impact[i,j]=m.pi+m.atan(va[1]/va[0]) #Normes de vitesse
        else:
            angles_impact[i,j]=m.atan(va[1]/va[0])


##TRACE DES COURBES
print("Calculs termines")
print("Creation des courbes 3D...")
#COURBE 1 : DISTANCE D'IMPACT EN FONCTION DE LA VITESSE ET DE L'ANGLE D'eJECTION
anglesmesh,vitessesmesh=np.meshgrid(angles,vitesses,indexing='ij')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

surf=ax.plot_surface(anglesmesh,vitessesmesh,xf, cmap=cm.jet,linewidth=0.2,antialiased =True)

ax.set_xlim3d(0,360)
ax.set_ylim3d(.1,10)
fig.colorbar(surf,shrink=0.5,aspect=10,orientation='vertical')

#Ajout de la projection 2D
cset = ax.contour(anglesmesh,vitessesmesh,xf, zdir='y', offset=0, cmap=cm.coolwarm)

#Ajout des legendes
ax.set_xlabel(r'$\alpha (^\circ)$')
ax.set_ylabel(r'$\omega (tr/min)$')
ax.set_zlabel(r'$D (m)$')
ax.legend()

plt_title = "Distance d'impact d'un bloc de glace projete d'une eolienne " + nom_eolienne
plt.title(plt_title)
            
#COURBE 2 : NORME DE VITESSES D'IMPACT EN FONCTION DE LA VITESSE ET DE L'ANGLE D'eJECTION
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')

surf=ax2.plot_surface(anglesmesh,vitessesmesh,vitesses_impact, cmap=cm.jet,linewidth=0.2,antialiased =True)


ax2.set_xlim3d(0,360)
ax2.set_ylim3d(.1,10)
fig2.colorbar(surf,shrink=0.5,aspect=10,orientation='vertical')

#Ajout des legendes
ax2.set_xlabel(r'$\alpha (^\circ)$')
ax2.set_ylabel(r'$\omega (tr/min)$')
ax2.set_zlabel("Normes de vitesse (m/s)")
ax2.legend()

plt_title = "Norme de vitesse d'impact d'un bloc de glace projete d'une eolienne " + nom_eolienne
plt.title(plt_title)

#COURBE 2 : ANGLE D'IMPACT EN FONCTION DE LA VITESSE ET DE L'ANGLE D'eJECTION
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')

surf=ax2.plot_surface(anglesmesh,vitessesmesh,angles_impact*180/np.pi, cmap=cm.jet,linewidth=0.2,antialiased =True)


ax2.set_xlim3d(0,360)
ax2.set_ylim3d(.1,10)
fig2.colorbar(surf,shrink=0.5,aspect=10,orientation='vertical')

#Ajout des legendes
ax2.set_xlabel(r'$\alpha (^\circ)$')
ax2.set_ylabel(r'$\omega (tr/min)$')
ax2.set_zlabel(r"Angle d'impact ($^\circ$)")
ax2.legend()

plt_title = "Angle d'impact d'un bloc de glace projete d'une eolienne " + nom_eolienne
plt.title(plt_title)


annotate()
print("Creation des courbes terminee")
plt.show()
print("Fin")