vuelta=-1
while vuelta<10:

                 print("\n PROGRAMA CREACION DE NOMINA \n")

                 print('buen dia, digite los siguientes datos para realizar la nomina \n')

                 print("Documento:")

                 D=int(input())

                 print("Nombres:")

                 N=str(input())

                 print("Apellidos:")

                 A=str(input())

                 print("¿cual es su salario?")

                 sl=int(input())

                 print("¿cuantos dias trabajó?")

                 Dt=int(input())

                 print("NOMINA")

                 tr=117100/30
                 sb=tr*Dt
                 vld=sl/30
                 st=vld*Dt
                 dps=st*8/100
                 st_d= int(st+sb-dps)

                 print("El señor/a",N,A,"con numero de documento ",D,",que recibe por contrato el monto de ",sl,"y que trabajó",Dt,"dias el mes de julio, sumado al subsidio transporte por dias trabajados, y restando las prestaciones sociales, se le consigna un total de: ",st_d, "en este momento se le habrá descargado un archivo en la carpeta del programa con la informacion correspondiente.")
                 file=open("nomina.txt" , "w")
                 file.write("\n NOMINA \n \n")
                 file.write("El señor/a : \n ")
                 file.write(N )
                 file.write( A)
                 file.write(" \n con numero de documento: \n")
                 file.write(' % s' %D)
                 file.write("\n que recibe por contrato el monto de: \n ")
                 file.write(' % s'%sl)
                 file.write("\n y que trabajó")
                 file.write(' % s' %Dt)
                 file.write("  dias del presente mes, se le ha sumado el subsidio de transporte, siendo este de 171.100 pesos colombianos por ley, y restado el 8 por ciento de prestaciones sociales, se le realiza la consignacion total de: ")
                 file.write("\n Mil gracias por la atencion prestada, puede guardar este archivo para cualquier reclamacion.")


                 file.close()
