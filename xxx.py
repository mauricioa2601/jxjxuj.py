print('ingrese primer angulo')
x= input("grados: ")
y= input("minutos: ")
z= input("segundos: ")
print('ingrese segundo angulo' )
x1= input("grados: ")
y1= input("minutos: ")
z1= input("segundos: ")
xfin = x+x1
yfin = y+y1
zfin= z+z1
if zfin >= 60:
    print('la suma de tus angulos:',xfin,yfin+1,zfin%60)
elif zfin >=60 and yfin >= 60:
    print('la suma de tus angulos:',xfin+1,((yfin + 1)% 60),zfin % 60)
elif zfin == 120 and yfin == 120 :
     print('la suma de tus angulos:', xfin + 2, (yfin + 2) % 120, zfin % 120)
elif zfin == 120 and yfin >60 :
     print('la suma de tus angulos:', xfin + 1, (yfin + 1) % 60, zfin % 120)
elif zfin >=60 and yfin == 120:
    print('la suma de tus angulos:', xfin + 2, (yfin + 1) % 120, zfin % 60)
elif yfin >= 60:
    print('la suma de tus angulos:',xfin+1,yfin&60,zfin)
elif zfin==120:
    print('la suma de tus angulos:',xfin,yfin+2,zfin%60)
elif yfin==120:
    print('la suma de tus angulos:', xfin+2, yfin%60, zfin)
else:
    print('la suma de tyus angulos',xfin,yfin,zfin)
