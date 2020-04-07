# to do
import sys
example_date = '000105'
#vectorq

vectorq= open("vectorq.exec", 'w')
vectorq.write("!/bin/csh")
vectorq.write("set dir = ./ss1/")
vectorq.write("set fileinfo = {$dir}info_pr.dat")
vectorq.write("set filedh =  {$dir}"+ sys.argv[0])
vectorq.write("set filest =  {$dir}"+ sys.argv[0])
vectorq.write("set filestm = {$dir}ss1_st0.dat")
vectorq.write("set filequ =  {$dir}ss1a2qu.gr")
vectorq.write("set fileqv =  {$dir}ss1a2qv.gr")
vectorq.write("set fileqdi = {$dir}ss1a2qdi.gr")
vectorq.write("./vectorq.exe << !")
vectorq.write('$fileinfo	#>>>>>Escribe info file info.dat:')
vectorq.write('$filedh	>>>>>Escribe fichero de altura Dinamica:')
vectorq.write('$filest	#>>>>>Escribe fichero de densidad:')
vectorq.write('$filestm	>>>>>Escribe fichero de densidad promedio:')
vectorq.write('$filequ	#>>>>>Escribe fichero Qu:')
vectorq.write('$fileqv	#>>>>>Escribe fichero Qv:')
vectorq.write('$fileqdi	)#>>>>>Escribe fichero Qdi:')
vectorq.close()

#omegainv

omegainv = open("omegainv.exec", 'w')
omegainv.write('!/bin/csh')
omegainv.write('set dir = ./ss1/')
omegainv.write('set fileinfo = {$dir}info_pr.dat')
omegainv.write('set filestm = {$dir}ss1_st0.dat')
omegainv.write('set fileqdi = {$dir}ss1a2qdi.gr')
omegainv.write('set filew =   {$dir}ss1a2ww.gr')
omegainv.write('./omegainv.exe << !')
omegainv.write('$fileinfo	#>>>>>Escribe info file info.dat:')
omegainv.write('$fileqdi 	#>>>>>Escribe fichero de Div Q:')
omegainv.write('$filestm   	#>>>>>Escribe fichero de densidad promedio:')
omegainv.write('ominput.dat  #>>>>>Escribe fichero parametros (ominput.dat):')
omegainv.write('$filew	#>>>>>Escribe fichero Salida W:')
omegainv.close()



