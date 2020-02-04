C**********************************************************************
C
C                            OMEGA PROGRAM
C
C   COMPUTES THE 3D VERTICAL VELOCITY FIELD SOLVING THE OMEGA EQ. BY
C   MEANS OF A RELAXATION METHOD. COORDINATES (X,Y,Z) ARE ASSUMED
C
C   It requires the forcing term computed in a 3D domain (*QDI.SNP)
C   consisting of NLxNFxNC grid points (the two outermost gridpoints
C   are usually zero all around the domain), a data file with the
C   mean density at each level (ST0.DAT), and two input files with
C   the domain (INFO.DAT) and some parameters needed to invert the
C   equation (OMINPUT.DAT).
C
C   N2 EST EN DEHORS DU LAPLACIEN
C
C   BOUDARY CONDITIONS ARE SET TO ZERO BY DEFAULT, BUT THE CODE CAN
C   BE EASILY MODIFIED FOR DIFFERENT OPTIONS. (Search for 'Boundary
C   Conditions' to locate the right place...).
C
C**********************************************************************
C
	REAL DX,DY,DZ,DX2,DY2,DZ2,LAT0,F0,F02,WAR,WUD,DIFW
	REAL XLAT1,XLON1,ALF0,XARM,YARM
	REAL EPSILON,FZFAC,OMFAC,BCSENP,N2PARAM,F2PARAM
	REAL RO(0:100,0:100,0:100),FORZ(0:100,0:100,0:100)
	REAL FFORZ(0:100,0:100,0:100),N22(0:100,0:100,0:100)
	REAL W(0:100,0:100,0:100),ZW(0:100,0:100,0:100)
	REAL ROM(0:100),ROMU(0:100),N2(0:100),COEF(0:100)
	REAL C1(0:100),C2(0:100),wf(0:100,0:100,0:100)
	INTEGER NL,NF,NC
        CHARACTER*3,NAME
	CHARACTER*75 filedat,fileqdi,fileww,filestm,filepa
	CHARACTER*1 ans

	OMEGA=7.29E-5
        G=9.81
        PI=3.14159
        RD=PI/180.
        XKGLA=60.*1.852

C(*BEGIN*)
	WRITE(*,'(////,">>>>>>>>>>Programa Omegainv.f<<<<<<<<<<")')

C(*Reading Options*)
	WRITE(*,'(a,$)')
     &	'>>>>>Escribe info file info.dat:'
	READ(*,*) filedat
	WRITE(*,*) filedat

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero de Div Q:'
	READ(*,*) fileqdi
	WRITE(*,*) fileqdi

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero de densidad promedio:'
	READ(*,*) filestm
	WRITE(*,*) filestm


	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero parametros (omegainput.dat):'
	READ(*,*) filepa
	WRITE(*,*) filepa

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero Salida W:'
	READ(*,*) fileww
	WRITE(*,*) fileww



C ..... READ DATA FROM user, 'info.dat' AND 'ominput.dat'

        OPEN(unit=99,file=filedat,status='old')
        read(99,3)
        read(99,3)
        read(99,*) XLON1,xlat1
	WRITE(*,'(">>>>>Lon0,lat0: ",f6.3,x,f6.3)') xlon1,xlat1
        read(99,3)
        read(99,*) alf0
        read(99,3)
        read(99,*) nl,nf,nc
	WRITE(*,'(">>>>>Im,jm,km: ",I3,x,I3,x,I3)') nc,nf,nl
        read(99,3)
        read(99,*) xarm,yarm
	WRITE(*,'(">>>>>xarm,yarm en grados: ",f6.3,f6.3)') xarm,yarm
        read(99,3)
        read(99,*) Z0,dz
    3   format(1x/1x)
        close(unit=99)

        ALF0=ALF0*RD

	OPEN(UNIT=55,FILE=filepa,STATUS='OLD')
	READ(55,*) EPSILON
	READ(55,*) BCSENP
	READ(55,*) N2PARAM
	READ(55,*) F2PARAM
	READ(55,*) FZFAC
	READ(55,*) OMFAC
        CLOSE(UNIT=55)

C ..... Latitud del punt central i DX,DY en metres:
        IF(ALF0.LT.0.01) THEN
           LAT0=XLAT1+YARM*REAL(NF-1)/2.
           DY=YARM*XKGLA*1000.
           DX=XARM*XKGLA*1000.*COS(RD*LAT0)
        ELSE
           XL=XARM*REAL(NC-1)/2.
           YL=YARM*REAL(NF-1)/2.
           DD=SQRT(XL**2+YL**2)
           AL=ATAN2(YL,XL)
           LAT0=XLAT1+DD*SIN(AL+ALF0)/XKGLA
           DY=YARM*1000.
           DX=XARM*1000.
        ENDIF

	Write(*,'(">>>>>dx:",f8.2,1x,"dy:",f8.2)') dx,dy

	F0=2.*OMEGA*SIN(LAT0*RD)
	F02=F0*F0
	DX2=DX*DX
	DY2=DY*DY
	DZ2=DZ*DZ
C
C***********************************************************************
C .....	READ FILES WITH DATA (DENSITY AND FORCING)
C
C       EL RECORRIDO DEL INDICE I ES A LO LARGO DEL PARALELO,  DE W a E
C	                  EL DE J ES A LO LARGO DEL MERIDIANO, DE N a S
C	                  EL DE K SEGUN LA VERTICAL, DE ABAJO A ARRIBA.
C
	OPEN(UNIT=11,FILE=filestm,STATUS='OLD')
	DO K=NL,1,-1
	   READ(11,*) ROM(K)
        ENDDO
	CLOSE(11)


	OPEN(UNIT=11,FILE=fileqdi,STATUS='OLD')
	READ(11,*) nl
	READ(11,*) nf,nc
	DO K=NL,1,-1
	DO j=nf,1,-1
	   DO i=1,nc
	      READ(11,*) FORZ(I,J,K)
	   ENDDO
	ENDDO
	ENDDO
	close(11)

C .....    S'eliminen els valors nuls de les voreres i es queda amb el
C .....    numero efectiu de files i columnes

	DO K=NL,1,-1
	DO I=1,NC
	   DO J=1,NF
	      FORZ(I,J,K)=FORZ(I+2,J+2,K)
	  ENDDO
	ENDDO
	ENDDO

	DO K=NL,1,-1
	DO I=nc-3,NC
	   DO J=nf-3,NF
	      FORZ(I,J,K)=0.
	  ENDDO
	ENDDO
	ENDDO


        NF=NF-4
        NC=NC-4

C
C*********************************************************************
C	CALCULATE PREVIOUS ARRAYS
C
C	N2(K) IS THE BRUNT-VAISALA FREQ.
C	COEF(K) IS THE COEFFICIENT OF OMEGA IN THE DISCRETE FORM OF
C	OMEGA EQUATION.
C	C1(K) AND C2(K) ARE COEFFICIENTS IN OMEGA EQUATION.
C
	DO K=2,NL-1
	   N2(K)=-G*(ROM(K+1)-ROM(K-1))/ROM(K)/(2.*DZ)
	ENDDO
C
C	SE IGUALAN N2 ABAJO Y ARRIBA
C
	N2(1)=N2(2)
	N2(NL)=N2(NL-1)
C
C	SE CALCULAN DENSIDADES FICTICIAS ABAJO Y ARRIBA
C
	ROM(0)=2.*N2(1)*ROM(1)*DZ/G+ROM(2)
	ROM(NL+1)=ROM(NL-1)-2.*N2(NL)*ROM(NL)*DZ/G
C
C	ROMU(K) IS THE AVERAGE DENSITY FOR LEVEL=K+1/2
C
	DO K=0,NL
	   ROMU(K)=.5*(ROM(K+1)+ROM(K))
	ENDDO
C
        IF (N2PARAM.EQ.0) THEN
	   DO K=1,NL
              N2(K)=0.
           ENDDO
        ENDIF
        IF (F2PARAM.EQ.0.) THEN
           F02=0.
        ENDIF

	DO K=1,NL
	   COEF(K)=2.*(N2(K)*(DX2+DY2)/DX2/DY2+F02/DZ2)
C	   COEF(K)=2.*N2(K)*(DX2+DY2)/DX2/DY2+2.*F02/DZ2
C	   COEF(K)=2.*N2(K)*(DX2+DY2)/DX2/DY2+F02*ROM(K)*(ROMU(K)+
C    :	   ROMU(K-1))/DZ2/ROMU(K)/ROMU(K-1)
C
	   C1(K)=N2(K)/COEF(K)
C
	   C2(K)=F02/COEF(K)/DZ2
	ENDDO
	DO K=1,NL
	   DO J=1,NF
	       DO I=1,NC
            	! FZFAC ES DEBIDO A LAS UNIDADES DE FORZ(I,J,K)
		! Notar que fzac debe de estar de acurdo con el programa
		!vector.f !!
		  FFORZ(I,J,K)=FZFAC*FORZ(I,J,K)/COEF(K)
	      ENDDO
	   ENDDO
	ENDDO
C
C**********************************************************************C
C ..... BOUNDARY CONDITIONS:
C
	DO K=0,NL+1
	    DO J=0,NF+1
		DO I=0,NC+1
		    W(I,J,K)=0.
		ENDDO
	    ENDDO
	ENDDO
C
C       Eliminate comment sign to read boundary conditions from a file...
c       OPEN(88,FILE='ombc.dat',STATUS='OLD')
c       READ(88,*) W(0,J,K)
c       READ(88,*) W(NC+1,J,K)
c       READ(88,*) W(I,0,K)
c       READ(88,*) W(I,NF+1,K)
c       READ(88,*) W(I,J,0)
c       READ(88,*) W(I,J,NL+1)
c       CLOSE(88)
c
C       Eliminate comment sign to modify boundary conditions at
c       particular grid points, e.g.,
c
c       W(NC/2,NF/2,0)=1E-4
c
C*********************************************************************
C	CALCULATE VERTICAL VELOCITY W(I,J,K)
C
        M=0
  100	M=M+1
	DO K=0,NL+1
	   DO J=0,NF+1
	      DO I=0,NC+1
		 ZW(I,J,K)=W(I,J,K)
	      ENDDO
	   ENDDO
	ENDDO
C
	DO K=1,NL
	    DO J=1,NF
		DO I=1,NC
		    WAR=(W(I+1,J,K)+W(I-1,J,K))/DX2+
     :		    (W(I,J+1,K)+W(I,J-1,K))/DY2
C
		    WUD=W(I,J,K+1)+W(I,J,K-1)
C		    WUD=ROM(K+1)*W(I,J,K+1)/ROMU(K)+
C    :		    ROM(K-1)*W(I,J,K-1)/ROMU(K-1)
C
		    W(I,J,K)=C1(K)*WAR+C2(K)*WUD-FFORZ(I,J,K)
C
		ENDDO
	    ENDDO
	ENDDO
C
C ..... Check Convergence...
	DIFWM=0.
	DO K=1,NL
	   DO J=1,NF
	      DO I=1,NC
		 DIFW=ABS(W(I,J,K)-ZW(I,J,K))
                 DIFWM=DIFWM+DIFW
		 IF(DIFW.GT.EPSILON) THEN
                    NEVE=(K-1)*NF*NC+(J-1)*NC+I
                    DIFWM=DIFWM/REAL(NEVE)
                    WRITE (6,*) M,DIFWM
                    GOTO 100
                 ENDIF
	      ENDDO
	   ENDDO
	ENDDO
C
C************************************************************************
C ..... CONVERGENCE WAS SUCCESFUL... STORE RESULTS
C
C       Atencio: s'escriuen les condicions de contorn als laterals del
C       domini, aprofitant que tanmateix hem de recuperar per als formats
C       les dues files i columnes que perd 2*DIV.Q . No s'escriuen els
C       dos nivells afegits a dalt i baix.
C

	OPEN(UNIT=33,FILE=fileww)
C	DO K=NL,1,-1
C	   WRITE(33,500) W(0,NF+1,K)/OMFAC,((W(I,NF+1,K)/OMFAC),
C     :                          I=0,NC+1),W(NC+1,NF+1,K)/OMFAC
C	   WRITE(33,500) W(0,NF+1,K)/OMFAC,((W(I,NF+1,K)/OMFAC),
C     :                           I=0,NC+1),W(NC+1,NF+1,K)/OMFAC
C	   DO J=NF,1,-1
C	      WRITE(33,500) W(0,J,K)/OMFAC,W(0,J,K)/OMFAC,((W(I,J,K)/
C     :        OMFAC),I=1,NC),W(NC+1,J,K)/OMFAC,W(NC+1,J,K)/OMFAC
C	   ENDDO
C	   WRITE(33,500) W(0,0,K)/OMFAC,((W(I,0,K)/OMFAC),
C     :                        I=0,NC+1),W(NC+1,0,K)/OMFAC
C	   WRITE(33,500) W(0,0,K)/OMFAC,((W(I,0,K)/OMFAC),
C     :                        I=0,NC+1),W(NC+1,0,K)/OMFAC
C	ENDDO
C  500   FORMAT(8F10.5)



	DO K=1,nl
	DO I=1,nc+4
	   DO J=1,nf+4
	      wf(I,J,K)=-999.0
	  ENDDO
	ENDDO
	ENDDO

	DO K=1,nl
	DO I=1,NC
	   DO J=1,NF
	      wf(I+2,J+2,K)=w(I,J,K)/omfac
	  ENDDO
	ENDDO
	ENDDO

	WRITE(33,*) nl
	WRITE(33,*) nf+4,nc+4
         do k=nl,1,-1
              DO j=nf+4,1,-1
	      DO i=1,nc+4
                 write(33,*) wf(i,j,k)
	      ENDDO
	    ENDDO
	ENDDO


	END
