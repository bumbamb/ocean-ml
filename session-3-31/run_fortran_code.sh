#!/bin/bash

python write_exec_files.py 930106
chmod +x vectorq.exec
chmod +x omegainv.exec
gfortran -O3 -o vectorq.exe vectorq.f
gfortran -O3 -o omegainv.exe omegainv.f
./vectorq.exec
./omegainv.exec