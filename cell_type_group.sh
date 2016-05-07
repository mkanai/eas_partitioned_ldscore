#!/bin/bash

set -eu

# Be sure to set the appropriate path to the bedfiles for $bedfiledir.
# (download http://data.broadinstitute.org/alkesgroup/LDSCORE/baseline_bedfiles.tgz & extract it).
#
bedfiledir=~/src/github.com/bulik/ldsc/ct_and_ctg_bedfiles/cell_type_group_specific
basedir=$(cd $(dirname $0) && pwd)
bedfilelist=$bedfiledir/names.txt

ldscdir=~/src/github.com/bulik/ldsc
ldsc=$ldscdir/ldsc.py
snps=$ldscdir/hapmap3_snps

bfile=$1
bim=$bfile.bim
bfilename=$(basename $bfile)
chr=${bfilename##*.}

cat $bedfilelist | tail -n+2 | awk -v d=$bedfiledir '$0{print d"/"$1".bed", $2}' | parallel --col-sep ' ' $basedir/annotate_snps.py --bfile $bfile --chr $chr --annot-bed {1} --annot-name {2/.} --out {2/.}.$chr

cat $bedfilelist | tail -n+2 | cut -f2 | parallel -j4 $ldsc --l2 --bfile $bfile --ld-wind-cm 1 --annot {.}.$chr.annot.gz --out {.}.$chr --print-snps $snps/hm.$chr.snp
