# to do
print(#!/bin/csh


set dir = ./ss1/
set fileinfo = {$dir}info_pr.dat
set filedh =  {$dir}dh000105.gr
set filest =  {$dir}density000105.gr
set filestm = {$dir}ss1_st0.dat
set filequ =  {$dir}ss1a2qu.gr
set fileqv =  {$dir}ss1a2qv.gr
set fileqdi = {$dir}ss1a2qdi.gr

./vectorq.exe << !
'$fileinfo'	#>>>>>Escribe info file info.dat:
'$filedh'	#>>>>>Escribe fichero de altura Dinamica:
'$filest'	#>>>>>Escribe fichero de densidad:
'$filestm'	#>>>>>Escribe fichero de densidad promedio:
'$filequ'	#>>>>>Escribe fichero Qu:
'$fileqv'	#>>>>>Escribe fichero Qv:
'$fileqdi'	#>>>>>Escribe fichero Qdi:
!)