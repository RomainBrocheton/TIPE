# Étude balistique d'un bloc de glace projeté des pales d'une éolienne

### Romain BROCHETON

Après une prise de contact auprès d'un ingénieur de GRTGaz et une visite de leurs locaux, le projet d'une étude balistique d'un bloc de glace projeté d'une éolienne m'a été confié. Il s'agissait d'étudier si un bloc de glace pouvait tomber sur une canalisation de gaz, et s'il pouvait la percer. Ce projet s'inscrit parfaitement dans le cadre du thème de l'année 2017-2018 : "Milieux". En effet, l'étude finale doit conclure quant à la rupture de la canalisation de gaz lorsque le bloc de glace percute et rentre en interaction avec elle.

## Positionnement thématique
INFORMATIQUE (Informatique pratique), SCIENCES INDUSTRIELLES (Génie Mécanique), PHYSIQUE (Mécanique).

## Mots-clés
Balistique, Portée, Choc, Résistance des matériaux, Éolienne

## Bibliographie commentée

La société GRTGaz s’occupe du transport de gaz sous haute pression à travers des canalisations, età ce jour, 3% des canalisations ne sont pas encore enterrées. Le transport de gaz s’effectuant à 67.7bars, si une canalisation se rompait, il pourrait il y avoir des jets de flammes à près de 200 mètres.

Lors d’épisodes météorologiques froids, des blocs de givre peuvent se former sur les pâles deséoliennes. Certaines éoliennes utilisent des systèmes anti-givre basés sur des résistances chauffantes,mais faire fonctionner ces résistances durant toute la période de froid peut se révéler onéreux. C’estpourquoi de plus en plus d’éoliennes utilisent une méthode afin d’enclencher le système dedégivrage lorsque le bloc de glace est trop important et peut causer des dégâts à l’éolienne. Cettetechnique s’appuie sur des calculs de pertes aérodynamiques et donc sur la perte de puissance del’éolienne [1]. Mais la glace doit d’abord se former, avant d’être détectée puis fondue ; c’estpourquoi un bloc de glace pourrait se détacher de l’éolienne et causer des dégâts au sol,matériellement et humainement. Les blocs de glace qui se décrochent des éoliennes peuvent faire de15 à 30 centimètres de long, sur une dizaine de centimètres d’épaisseur [2], ce qui comme expliquédans les objectifs du TIPE, pourrait être catastrophique s’ils tombaient sur une canalisation de gazaérienne.

La portée balistique est définie comme la distance horizontale parcourue par un projectile entre lemoment où il est lancé et celui où il retombe sur le sol [3]. La portée P est définie comme l'abscissede la position du projectile pour laquelle l'ordonnée est nulle : P = x(t1) avec t1 tel que y(t1) = 0 ,avec P la portée en mètres, x la position horizontale en mètres, y la position verticale en mètres ett1 un temps en secondes.

Pour savoir si le bloc de glace tombé sur une canalisation de gaz pourrait, ou non, la fissurer, jevais m’appuyer sur des principes de dynamique impulsive. Le but de la dynamique impulsive estd’analyser le mouvement sur un système qui subit un événement appelé choc. Le choc est uncontact entre deux corps qui se produit à un instant singulier. Ce contact comporte unediscontinuité des vitesses des deux corps, mais également une continuité dans leurs positions. Lavariation de la vitesse à l’impact est produite par des forces impulsives. Elles sont dues au contactentre les corps [4]. Cette étude (théorique et/ou simulatoire) dépendra de différents paramètres telsque la vitesse et l'angle de collision ainsi que de l'épaisseur, du diamètre et du matériau de lacanalisation de gaz aérienne.

## Problématique retenue
À quelle distance un bloc de glace projeté des pales d’une éolienne peut-il aller et peut-il causer desdégâts à une canalisation de gaz aérienne s’il la percute ?

## Objectifs du TIPE
L’objectif de ce TIPE est d'étudier les conditions permettant de garantir la sécurité des ouvragesgaziers à proximité d'éoliennes.

La première partie de l'étude permettra de savoir si le bloc de glace pourrait atteindre les ouvragesgaziers aériens, en fonction de la vitesse de rotation de l'éolienne, des dimensions de celle-ci et del'angle auquel le bloc de givre est projeté.

La seconde partie consistera à mener une étude de dynamique impulsive, permettant de savoir si,lorsque le bloc de glace rentre en collision avec une canalisation de gaz aérienne, celui-ci peut percerl'ouvrage gazier ou non.

## Abstract
During winter, ice blocks appear on the wind turbine blades. Mechanisms on the basis of heatingconductors exists to avoid this issue, however, it is very expensive to make them workcontinuously. This mechanism is powered on when the ice block is shaped and this creates a hazardfor people and nearby gas pipes. My project, given by Mickael Metzger, a GRTGaz engineer, is tocheck if the ice block could afflict these pipes. I have studied the path of the ice block to know if itcan touch the nearby gas pipes and if it can damage it.

## Références bibliographiques
[1] G. Fortin, J-L. Laforte : Modèle d'accrétion de glace sur un objet bidimensionnel fixe applicable
aux pales d'éoliennes : Vertigo - la revue électronique en sciences de l'environnement, 2004

[2] Ouest-France : Moréac. Quand des blocs de glace tombent des éoliennes : https://www.ouest-
france.fr/bretagne/moreac-56500/moreac-quand-des-blocs-de-glace-tombent-des-eoliennes-4761006,
oct 2017

[3] P. Rebetez : Balistique : http://owl-ge.ch/IMG/pdf/balistique.pdf, jan. 2017

[4] P. Vanucci : Cours de mécanique générale : Université de Nevers, 2002
Références bibliographiques (phase 3)

[5] GRTGaz : Nos chiffres clés : http ://www.grtgaz.com/notre-entreprise/nos-chiffres- cles.html,
juin 2018

## Déroulement Opérationnel du TIPE (DOT)
[1] Septembre 2017 : Premier contact avec Mickael Metzger, un ingénieur chez GRTGaz, visite
des locaux, réception du sujet.

[2] Octobre 2017 : Résolution numérique de la distance de projection en fonction des différents
paramètres. Recherche de documents bibliographiques sur l'étude des chocs.

[3] Novembre-Décembre 2017 : Création du premier code Python (distance de projection en
fonction de l'angle d'éjection, à vitesse fixée). Recherche d'une erreur dans les calculs (distance
trouvée exorbitante), qui se révéla être un problème d'unité.

[4] Janvier 2018 : Création du deuxième code Python (courbes 3D de la distance de projection et
de la vitesse d'impact).

[5] Février 2018 : Nouveau contact avec Mickael Metzger, vérification des résultats. Création du
premier modèle SolidWorks (avec entaille, abandonné suite à la simulation). Création du second
modèle (sans entaille).

[6] Mars-Avril 2018 : Étude de choc à l'aide d'une étude dynamique SolidWorks. Première
simulation avec un maillage uniforme, abandonné (durée des calculs). Seconde simulation avec un
maillage non uniforme (fin sur la zone de contact, grossier ailleurs).
