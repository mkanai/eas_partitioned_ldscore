#!/bin/bash

set -eu

ldscdir=~/src/github.com/bulik/ldsc
ldsc=$ldscdir/ldsc.py
snps=$ldscdir/hapmap3_snps

bfile=$1
bim=$bfile.bim
bfilename=$(basename $bfile)
chr=${bfilename##*.}

mkdir -p $bfilename

plink --bfile $bfile \
      --keep-allele-order \
      --extract $snps/hm.$chr.snp \
      --make-bed \
      --out $bfilename/$chr

if [ $chr == 6 ]
then
  plink --bfile $bfilename/$chr \
        --chr $chr \
        --from-mb 25 \
        --to-mb 34 \
        --write-snplist \
        --out $bfilename/hla

  plink --bfile $bfilename/$chr \
        --keep-allele-order \
        --exclude $bfilename/hla.snplist \
        --make-bed \
        --out $bfilename/$chr
fi

$ldsc --l2 --bfile $bfilename/$chr --ld-wind-cm 1 --out weights.$chr
