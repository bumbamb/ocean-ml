CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C     THIS CODE COMPUTES THE FORCING TERM OF THE OMEGA EQUATION AS GIVEN
C                      BY THE Q-VECTOR FORMULATION
C
C	dh(i,j,k) contiene la altura dinamica en cmdyns (aunque
C	st(i,j,k)  contiene la densidad
C
C	Author: Damia Gomis,
C     reformado por Pedro Velez
C	Date:   10th June 1999
C
C     The forcing term is computed in a 3D domain consisting initially
C     of NFxNCxNL grid points, and needs geopotential and sg-t analyses
C     in the standard 3D format (*ST.gr and (*DH.gr or *DT.gr)).
C
C     In a first step, the mean density of each level is computed (from
C     the ST 3D grid) and witten in an output file (ST0.DAT). This file
C     will be required to invert the omega equation (using OMEGAINV.F).
C     Second, the Q-vector components are derived from the ST and DH (or
C     DT) 3D grids, and optionally written as separate files. Finally,
C     the 3D forcing term  2*Div(Q)  is computed and written in the
C     standard 3D format (*QDI.gr).
C
C     ==================================================================
      PARAMETER(NLMAX=100,NFMAX=100,NCMAX=100)
      DIMENSION ST(NLMAX,NFMAX,NCMAX),DH(NLMAX,NFMAX,NCMAX),R0(NLMAX)
      DIMENSION V(9),QU(NLMAX,NFMAX,NCMAX),QV(NLMAX,NFMAX,NCMAX),
     .QDI(NLMAX,NFMAX,NCMAX)
      CHARACTER*3,NA
	CHARACTER*90 filedat,filedh,filest,filequ,fileqv,fileqdi
	CHARACTER*90 filestm
	CHARACTER*1 ans
      PI=3.14159
      RD=PI/180.
      XKGLA=60.*1.852

C(*BEGIN*)
	WRITE(*,'(////,">>>>>>>>>>Programa vectorq.f<<<<<<<<<<")')

C(*Reading Options*)
	WRITE(*,'(a,$)')
     &	'>>>>>Escribe info file info.dat:'
	READ(*,*) filedat
	WRITE(*,*) filedat

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero de altura Dinamica:'
	READ(*,*) filedh
	WRITE(*,*) filedh

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero de densidad:'
	READ(*,*) filest
	WRITE(*,*) filest
	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero de densidad promedio:'
	READ(*,*) filestm
	WRITE(*,*) filestm
	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero Qu:'
	READ(*,*) filequ
	WRITE(*,*) filequ

	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero Qv:'
	READ(*,*) fileqv
	WRITE(*,*) fileqv
	WRITE(*,'(a,$)')
     &	'>>>>>Escribe fichero Qdi:'
	READ(*,*) fileqdi
	WRITE(*,*) fileqdi


C .... Reading fichero de informaci�n
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
      read(99,*) P0,PINT
    3 format(1x/1x)
      close(unit=99)
c
      ALF0=ALF0*RD
c
C .... Latitud del punt central, per a trobar el param. de Coriolis promig
C     (la formulacio de Vector Q el presuposa constant) i escalat de DX,DY
C     en unitats de 1E5 m  per als calculs:

      IF(ALF0.LT.0.01) THEN
         Y00=XLAT1+YARM*REAL(NF-1)/2.
         DY=YARM*XKGLA/100.
         DX0=XARM*XKGLA/100.
      ELSE
         XL=XARM*REAL(NC-1)/2.
         YL=YARM*REAL(NF-1)/2.
         DD=SQRT(XL**2+YL**2)
         AL=ATAN2(YL,XL)
         Y00=XLAT1+DD*SIN(AL+ALF0)/XKGLA
         DY=YARM/100.
         DX=XARM/100.
      ENDIF
      F0=14.5444*SIN(Y00*RD)

	WRITE(*,'(">>>>>F:(*1e-5) ",f6.3)') f0

C .... Fill in the matriz outputs with the absent data value

      do i=1,nl
         do j=1,nf
            do k=1,nc
               qu(i,j,k)=-999.
               qv(i,j,k)=-999.
               qdi(i,j,k)=-999.
            enddo
         enddo
      enddo

C.....Reading Geopotential...
	OPEN(UNIT=1,FILE=filedh,STATUS='OLD')

	READ(1,*) nl
	READ(1,*) nf,nc
	DO k=1,nl
	  DO J=1,nf
	    DO i=1,nc
            READ(1,*) DH(k,j,i)
	     DH(K,J,I)=10.*dh(k,j,i)  !paso dh de unidades internacioanles
						!a cmdyn
           ENDDO
        ENDDO
      ENDDO
      CLOSE(UNIT=1)

C.....Reading Density and computing the mean density...
         OPEN(UNIT=2,FILE=filest,STATUS='OLD')
	READ(2,*) nl
	READ(2,*) nf,nc
	DO k=1,nl
	DO J=1,nf
	DO i=1,nc
		READ(2,*) st(k,j,i)
	ENDDO
	ENDDO
	ENDDO
	CLOSE(UNIT=2)

	DO I=1,NL
	R0(I)=0.
	  DO J=1,NF
	    DO K=1,NC
		R0(I)=R0(I)+ST(I,J,K)
	    ENDDO
	  ENDDO
	R0(I)=R0(I)/FLOAT(NF*NC)
	ENDDO

C
      OPEN(UNIT=3,FILE=filestm,STATUS='unknown')
      DO I=1,NL
         R0(I)=1000.+R0(I)
C         TYPE 15,I,R0(I)
          WRITE(3,*) I,R0(I)
         WRITE (3,17) R0(I)
      ENDDO
      CLOSE(UNIT=3)

   15 FORMAT(1X,'Level',I3,':  mean density ='f10.4)
   17 FORMAT(1X,f10.4)

C.....Computation of Q-vectors:

      DO 45 I=1,NL
         DO 40 J=2,NF-1
            IF(ALF0.LT.0.01) DX=DX0*COS(RD*(XLAT1+YARM*FLOAT(J-1)))
            DO K=2,NC-1
               V(1)=DH(I,J+1,K-1)
               V(2)=DH(I,J+1,K)
               V(3)=DH(I,J+1,K+1)
               V(4)=DH(I,J,K-1)
               V(5)=DH(I,J,K)
               V(6)=DH(I,J,K+1)
               V(7)=DH(I,J-1,K-1)
               V(8)=DH(I,J-1,K)
               V(9)=DH(I,J-1,K+1)
               CALL FINDIF(DX,DY,V)
               DERXY=V(4)
               DERXX=V(5)
               DERYY=V(6)
               V(1)=ST(I,J+1,K-1)
               V(2)=ST(I,J+1,K)
               V(3)=ST(I,J+1,K+1)
               V(4)=ST(I,J,K-1)
               V(5)=ST(I,J,K)
               V(6)=ST(I,J,K+1)
               V(7)=ST(I,J-1,K-1)
               V(8)=ST(I,J-1,K)
               V(9)=ST(I,J-1,K+1)
               CALL FINDIF(DX,DY,V)
C
C(--> m/s): *1E1 si DH ve en m.dyn.  *0.1 si DH ve en cm.dyn.
C(/F0):*1E-5   (/DX**2):*1E10  (/DX):*1E5
C(factor d'escala que resulta hasta ahora):*1E10
C(factor d'escala que quiero):*1E12  entonces multiplico por  *100.
               FACT=100.*0.1*9.81/(F0*R0(I))
C              Q-vector components:
               QU(I,J,K)=1.*FACT*(-DERXY*V(2)+DERXX*V(3))
               QV(I,J,K)=1.*FACT*(-DERYY*V(2)+DERXY*V(3))
            ENDDO
   40    CONTINUE
   45  CONTINUE
	CLOSE(UNIT=1)
	CLOSE(UNIT=2)
	WRITE(*,*) '>>>>>Qu and Qv are scaled as 1E12.'

C ----------------------------------------------------------------------
C.....Computation of Q-vector DIVERGENCE:
      DO 145 I=1,NL
         DO 140 J=3,NF-2
         IF(ALF0.LT.0.01) DX=DX0*COS(RD*(XLAT1+YARM*FLOAT(J-1)))
            do k=3,nc-2
               v(1)=qu(i,j+1,k-1)
               v(2)=qu(i,j+1,k)
               v(3)=qu(i,j+1,k+1)
               v(4)=qu(i,j,k-1)
               v(5)=qu(i,j,k)
               v(6)=qu(i,j,k+1)
               v(7)=qu(i,j-1,k-1)
               v(8)=qu(i,j-1,k)
               v(9)=qu(i,j-1,k+1)
               CALL FINDIF(DX,DY,V)
               DXU=V(2)
               v(1)=qv(i,j+1,k-1)
               v(2)=qv(i,j+1,k)
               v(3)=qv(i,j+1,k+1)
               v(4)=qv(i,j,k-1)
               v(5)=qv(i,j,k)
               v(6)=qv(i,j,k+1)
               v(7)=qv(i,j-1,k-1)
               v(8)=qv(i,j-1,k)
               v(9)=qv(i,j-1,k+1)
               CALL FINDIF(DX,DY,V)
C
C              Q-vector Divergence:
C              (/DX):*1E5    QU,QV:*1E12     TOTAL:*1E17
C              (Escalado de DivQ):*1E16 , entonces multiplico por *0.1
               QDI(I,J,K)=0.1*2.*(DXU+V(3))
            ENDDO
  140    CONTINUE
  145 CONTINUE

C ..... Escribiendo datos
	WRITE(*,*) '>>>>>DivQ is scaled as 1E16.'
	OPEN(UNIT=31,FILE=filequ,STATUS='UNKNOWN')
	OPEN(UNIT=32,FILE=fileqv,STATUS='UNKNOWN')
	OPEN(UNIT=33,FILE=fileqdi,STATUS='UNKNOWN')

	WRITE(31,*) nl
	WRITE(31,*) nf,nc

	WRITE(32,*) nl
	WRITE(32,*) nf,nc

	WRITE(33,*) nl
	WRITE(33,*) nf,nc

         do k=1,nl
            do j=1,nf
		DO i=1,nc
               write(31,*) qu(k,j,i)
               write(32,*) qv(k,j,i)
               write(33,*) qdi(k,j,i)
            enddo
         enddo
	ENDDO
         close(unit=31)
         close(unit=32)
         close(unit=33)

C     ------------------------------------------------------------------
C      valors reals de parametres utilitzats amb unitats corregides:
C      bracos de xarxa:            DX,DY*1E5 m
C      parametre de Coriolis:      F0*1E-5    1/s
C      vector Q:                   Q*1E-12    1/s3
C      divergencia de Q:           QDI*1E-16  1/m s3
C     ------------------------------------------------------------------
      END


CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
C     FINITE DIFFERENCES SCHEME:
      SUBROUTINE FINDIF(DX,DY,V)
      DIMENSION V(9),VV(6)
C
      DO 2005 I=1,9
 2005 VV(1)=VV(1)+V(I)
      VV(1)=VV(1)/9.
      VV(2)=(V(6)-V(4))/(2*DX)
      VV(3)=(V(2)-V(8))/(2*DY)
      VV(4)=(V(3)+V(7)-V(9)-V(1))/(4*DX*DY)
      VV(5)=(V(4)+V(6)-2*V(5))/DX**2
      VV(6)=(V(2)+V(8)-2*V(5))/DY**2
      DO 2010 I=1,6
 2010 V(I)=VV(I)
      DO 2020 I=7,9
 2020 V(I)=0
      RETURN
      END
