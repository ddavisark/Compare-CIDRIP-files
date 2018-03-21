#!/usr/bin/python3
import sys
import os.path

OLD=sys.argv[1]
NEW=sys.argv[2]
COM='/home/proto/psource/com'

fp=open(OLD, "r")
fq=open(NEW, "r")
olist=fp.readlines()
ilist=fq.readlines()

if os.path.exists(COM):
   os.remove(COM)
   
fr=open(COM, "w")
fr.write('*****************************************'+'\n')
fr.write('*\n')
fr.write('*     OLD file Line Count.....: %s\n'% sum(1 for line in olist))
fr.write('*     NEW file Line Count.....: %s\n'% sum(1 for line in ilist))
fr.write('*\n')
fr.write('*   > CIDRIP found in OLD file, not NEW file\n')
fr.write('*   < CIDRIP found in NEW file, not OLD file\n')
fr.write('*   - CIDRIP found in BOTH files\n')
fr.write('*\n')
fr.write('******************************************\n')

num_com = 0
num_old = 0
num_new = 0

for ctr in range(1,3):
   if ctr == 1:
       files = [ olist, ilist ]
   else:
       files = [ ilist, olist ]

   inner = files[0]
   outer = files[1]

   for p in outer:
      p = p.strip()
      found = 0

      for q in inner:
         q = q.strip()
         if p == q:
            found = 1
            if ctr == 1:
               fr.write(' - '+p+'\n')
               num_com += 1
            break

      if found == 0:
         if ctr == 1:
            fr.write(' > '+p+'\n')
            num_old += 1
#            print (" > %s"% (p))
         else:
            fr.write(' < '+p+'\n')
            num_new += 1
#            print (" < %s"% (p))

   del files[:] 

fp.close()
fq.close()

fr.write('\nCIDRIPs common to both files......: %d\n'% num_com)
fr.write('CIDRIPs found only in old file....: %d\n'% num_old)
fr.write('CIDRIPs found only in new file....: %d\n\n'% num_new)
fr.close()

##############################################
# Send the file com's contents to stdout
#

filepath = "/home/proto/psource/com"
with open(filepath) as fp:
   for line in fp:
      print ("%s"% line.strip())


