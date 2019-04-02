#!/bin/bash
#PATH=/share/CACHEDEV1_DATA/Web/toProRes/watched

for m in $(ls /share/CACHEDEV1_DATA/Web/toProRes/watched/ );

 do
	echo "starting conversion of $m"
	ffmpeg -i /share/CACHEDEV1_DATA/Web/toProRes/watched/"$m" -c:v prores_ks -profile:v 1 -qscale:v 9 -vendor ap10  /share/CACHEDEV1_DATA/Web/toProRes/prores/${m%%.*}.mov

	echo "moving '$m' to origianls folder"
	mv /share/CACHEDEV1_DATA/Web/toProRes/watched/$m /share/CACHEDEV1_DATA/Web/toProRes/original/$m
done
