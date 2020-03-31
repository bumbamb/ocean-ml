import sys

base = '/Users/helenfellow/Documents/Education /example-writing-to-file/'
vectorq = base+'vectorq.exec'
omegainv = base+'omegainv.exec'

file_number = sys.argv[1]

f_v = open(vectorq,"w+")
f_o = open(omegainv,"w+")




f_o.write("#!/bin/csh\n\n\nset dir = ./test/\n")
f_o.write("set outdir = /Users/brownscholar/Desktop/fortran_files/omega/\n")
f_o.write("set auxdir = /Users/brownscholar/Desktop/fortran_files/aux/\n")
f_o.write("set fileinfo = {$dir}info_pr.dat\n")
f_o.write("set filestm = {$auxdir}/st0/"+str(file_number)+"_st0.dat\n")
f_o.write("set fileqdi = {$auxdir}/qdi/"+str(file_number)+"_qdi.gr\n")
f_o.write("set filew =   {$outdir}w/"+str(file_number)+"_ww.gr\n\n")
f_o.write("./omegainv.exe << !\n")
f_o.write("\'$fileinfo\' 	#>>>>>Escribe info file info.dat:\n")
f_o.write("\'$fileqdi\' 	#>>>>>Escribe fichero de Div Q:\n")
f_o.write("\'$filestm\'   	#>>>>>Escribe fichero de densidad promedio:\n")
f_o.write("\'ominput.dat\'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
f_o.write("\'$filew\'	#>>>>>Escribe fichero Salida W:\n")

f_v.write("#!/bin/csh\n\n\nset dir = ./test/\n")
f_v.write("set indir = /Users/helenfellow/Documents/cnn_paper/data/\n")
f_v.write("set auxdir = /Users/brownscholar/Desktop/fortran_files/aux/\n")
f_v.write("set outdir = /Users/brownscholar/Desktop/fortran_files/omega/\n") 
f_v.write("set fileinfo = {$dir}info_pr.dat\n")
f_v.write("set filedh =  {$indir}/dh/dh_"+str(file_number)+".gr\n")
f_v.write("set filest =  {$indir}/density/density_"+str(file_number)+".gr\n")
f_v.write("set filestm = {$auxdir}/st0/"+str(file_number)+"_st0.dat\n")
f_v.write("set filequ =  {$outdir}/u/"+str(file_number)+"_qu.gr\n")
f_v.write("set fileqv =  {$outdir}/v/"+str(file_number)+"_qv.gr\n")
f_v.write("set fileqdi = {$auxdir}/qdi/"+str(file_number)+"_qdi.gr\n\n")

f_v.write("./vectorq.exe << !\n")
f_v.write("\'$fileinfo\'	#>>>>>Escribe info file info.dat:\n")
f_v.write("\'$filedh\'	#>>>>>Escribe fichero de altura Dinamica:\n")
f_v.write("\'$filest\'	#>>>>>Escribe fichero de densidad:\n")
f_v.write("\'$filestm\'	#>>>>>Escribe fichero de densidad promedio:\n")
f_v.write("\'$filequ\'	#>>>>>Escribe fichero Qu:\n")
f_v.write("\'$fileqv\'	#>>>>>Escribe fichero Qv:\n")
f_v.write("\'$fileqdi\'	#>>>>>Escribe fichero Qdi:\n")



f_o.close()
f_v.close()














