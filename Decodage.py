#!/usr/bin/python
#Convention utilisee
#   0 : |, \
#   1 : -, /


import argparse
from argparse import RawTextHelpFormatter
import random

#Declaration de la convention
CONVENTION_FALSE_BARRE = 0
CONVENTION_FALSE_ANTISLASH = 1
CONVENTION_TRUE_TIRET = 2
CONVENTION_TRUE_SLASH = 3

#Analyse des arguments
parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description='Simulateur de protocole BB84 [Pierre L - Pierre G]\nConvention utilisee :\n  0 : |, \\\n  1 : -, /')
parser.add_argument('longueur', action="store", type=int, help='Longueur de la chaine')
parser.add_argument("-d", "--debug", help="Mode debug",action="store_true", default=False)
parser.parse_args()
args = parser.parse_args()

#Declaration par defaut des lists
first_pass = []
second_pass = []
third_pass = []
fourth_pass = []
fifth_pass = []
temp_string = ""

print "--- Rappel convention :\n      0 : |, \\\n      1 : -, /"

if args.debug:
  print "[DEBUG] Longueur chaine : "+ str(args.longueur)


#First pass
#Aleatoire de 1 et 0
for x in xrange(0,args.longueur):
  if random.choice([True, False]):
    temp_string += "1"
    first_pass.append(True)
  else:
    temp_string += "0"
    first_pass.append(False)
  pass

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Message binaire : " + temp_string

#Ecriture dans le fichier message.bin
with open('message.bin', 'w') as file_:
  file_.write(temp_string)


temp_string = ""
#Choix de la convention aleatoirement en fonction des bits du message
for x in xrange(0,args.longueur):
  if first_pass[x]:
    if random.choice([True, False]):
      #True et -
      second_pass.append(CONVENTION_TRUE_TIRET)
      temp_string += "-"
    else:
      #True et /
      second_pass.append(CONVENTION_TRUE_SLASH)
      temp_string += "/"
  else:
    if random.choice([True, False]):
      #True et -
      second_pass.append(CONVENTION_FALSE_BARRE)
      temp_string += "|"
    else:
      #True et /
      second_pass.append(CONVENTION_FALSE_ANTISLASH)
      temp_string += "\\"

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Emission : " + temp_string
#Ecriture dans le fichier emission.pol
with open('emission.pol', 'w') as file_:
  file_.write("--- Rappel convention :\n      0 : |, \\\n      1 : -, /\n\n\n")
  file_.write(temp_string)

temp_string = ""
#Choix aleatoire de la convention 
for x in xrange(0,args.longueur):
    random_value = random.choice([CONVENTION_FALSE_BARRE, CONVENTION_FALSE_ANTISLASH, CONVENTION_TRUE_TIRET, CONVENTION_TRUE_SLASH])
    if random_value == CONVENTION_FALSE_BARRE:
      #-
      third_pass.append(CONVENTION_TRUE_TIRET)
      temp_string += "-"
    elif random_value == CONVENTION_FALSE_ANTISLASH:
      #/
      third_pass.append(CONVENTION_TRUE_SLASH)
      temp_string += "/"
    elif random_value == CONVENTION_TRUE_TIRET:
      #-
      third_pass.append(CONVENTION_FALSE_BARRE)
      temp_string += "|"
    elif random_value == CONVENTION_TRUE_SLASH:
      #/
      third_pass.append(CONVENTION_FALSE_ANTISLASH)
      temp_string += "\\"

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Polarisation : " + temp_string
#Ecriture dans le fichier polarisation.pol
with open('polarisation.pol', 'w') as file_:
  file_.write(temp_string)


temp_string = ""
#Decision des bits a utiliser, si les caracteres sont egaux, decales de 90 degres, ou aleatoire
for x in xrange(0,args.longueur):
  if second_pass[x] == third_pass[x]:
    if third_pass[x] == CONVENTION_TRUE_SLASH or third_pass[x] == CONVENTION_TRUE_TIRET:
      fourth_pass.append(True)
      temp_string += "1"
    else:
      fourth_pass.append(False)
      temp_string += "0"
  elif (second_pass[x] == CONVENTION_TRUE_TIRET and third_pass[x] == CONVENTION_FALSE_BARRE) or (second_pass[x] == CONVENTION_FALSE_BARRE and third_pass[x] == CONVENTION_TRUE_TIRET) or (second_pass[x] == CONVENTION_TRUE_SLASH and third_pass[x] == CONVENTION_FALSE_ANTISLASH) or (second_pass[x] == CONVENTION_FALSE_ANTISLASH and third_pass[x] == CONVENTION_TRUE_SLASH):
    if third_pass[x] == CONVENTION_TRUE_SLASH or third_pass[x] == CONVENTION_TRUE_TIRET:
      fourth_pass.append(False)
      temp_string += "0"
    else:
      fourth_pass.append(True)
      temp_string += "1"
  else:
    if random.choice([True, False]):
      if third_pass[x] == CONVENTION_TRUE_SLASH or third_pass[x] == CONVENTION_TRUE_TIRET:
        fourth_pass.append(True)
        temp_string += "1"
      else:
        fourth_pass.append(False)
        temp_string += "0"
    else:
      if third_pass[x] == CONVENTION_TRUE_SLASH or third_pass[x] == CONVENTION_TRUE_TIRET:
        fourth_pass.append(False)
        temp_string += "0"
      else:
        fourth_pass.append(True)
        temp_string += "1"

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Decision : " + temp_string
#Ecriture dans le fichier decision.txt
with open('decision.txt', 'w') as file_:
  file_.write(temp_string)


temp_string = ""
#Choix des incertitudes en rapport au tableau renseigne
for x in xrange(0,args.longueur):
  if second_pass[x] == CONVENTION_TRUE_TIRET and third_pass[x] == CONVENTION_TRUE_TIRET:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_FALSE_BARRE and third_pass[x] == CONVENTION_TRUE_TIRET:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_TRUE_TIRET and third_pass[x] == CONVENTION_FALSE_BARRE:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_FALSE_BARRE and third_pass[x] == CONVENTION_FALSE_BARRE:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_TRUE_SLASH and third_pass[x] == CONVENTION_TRUE_SLASH:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_FALSE_ANTISLASH and third_pass[x] == CONVENTION_TRUE_SLASH:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_FALSE_ANTISLASH and third_pass[x] == CONVENTION_FALSE_ANTISLASH:
    fifth_pass.append(True)
    temp_string += "1"
  elif second_pass[x] == CONVENTION_TRUE_SLASH and third_pass[x] == CONVENTION_FALSE_ANTISLASH:
    fifth_pass.append(True)
    temp_string += "1"
  else:
    fifth_pass.append(False)
    temp_string += "0"

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Incertitudes : " + temp_string

temp_string = ""
#Creation de la clef
for x in xrange(0,args.longueur):
  if fifth_pass[x]:
    if fourth_pass[x]:
      temp_string += "1"
    else:
      temp_string += "0"
  else:
    temp_string += "#"

#Si le mode debug est actif, j'affiche le message
if args.debug:
  print "[DEBUG] Clef : " + temp_string

#Ecriture dans le fichier clef.txt
with open('clef.txt', 'w') as file_:
  file_.write(temp_string)







