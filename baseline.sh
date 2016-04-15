#!/bin/bash

set -eu

# Be sure to set the appropriate path to the bedfiles for $bedfiledir.
# (download http://data.broadinstitute.org/alkesgroup/LDSCORE/baseline_bedfiles.tgz & extract it).
#
# bedfiledir=path/to/baseline_bedfiles
basedir=$(cd $(dirname $0) && pwd)
bedfilelist="$basedir/baseline_bedfiles.txt"

bfile=$1
bim=$bfile.bim
bfilename=$(basename $bfile)
chr=${bfilename##*.}

mkdir -p $bfilename

cat $bim \
  | awk '
BEGIN {
  OFS="\t"
  print "CHR", "BP", "SNP", "CM", "base"
}
{print $1, $4, $2, $3, "1"}
' > $bfilename/base.annot

cat $bedfilelist | tail -n+2 | awk -v d=$bedfiledir '$0{print d"/"$0".bed"}' | parallel $basedir/annotate_snps.py --bfile $bfile --chr $chr --annot-bed {} --only-annot --out $bfilename/{/.}
cat $bedfilelist | awk -v d=$bfilename '$0{print d"/"$0".annot"}' | xargs paste -d$'\t' | gzip -c > baseline.$chr.annot.gz

