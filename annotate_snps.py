#!/usr/bin/env python
import argparse
import os.path
import numpy as np
import pandas as pd
from chromtree import ChromTree


def main(args):
    snps = pd.read_csv(args.bfile + '.bim', header=None, delimiter='\t', names=['CHR', 'SNP', 'CM', 'BP', 'A1', 'A2'])
    n_snp = len(snps)
    n_annot = len(args.annot_bed)
    annot_matrix = np.zeros((n_snp, n_annot), dtype=np.int8)
    annot_names = []

    for i in range(n_annot):
        trees = ChromTree()
        bed = pd.read_csv(args.annot_bed[i], header=None, delimiter='\t')
        annot_name = os.path.basename(args.annot_bed[i])[:-4] if args.annot_name[i] is None else args.annot_name[i]
        annot_names.append(annot_name)
        if args.chr is not None:
            args.chr = trees._format_chrom(args.chr)
            bed = bed[bed[0] == args.chr]
        bed.apply(lambda x: trees.insert(x[0], x[1]-1, x[2]+1, i), axis=1)
        idx = snps.apply(lambda x: trees.find(x[0], x[3], x[3]), axis=1)
        [[annot_matrix.itemset((j, i), 1) for _ in v] for j, v in idx.iteritems()]

    out_fname_annot = args.out + '.annot'
    if not args.only_annot:
        annot_df = pd.concat([snps[['CHR', 'BP', 'SNP', 'CM']], pd.DataFrame(annot_matrix)], axis = 1)
        annot_df.columns = ['CHR', 'BP', 'SNP', 'CM'] + annot_names
    else:
        annot_df = pd.DataFrame(annot_matrix)
        annot_df.columns = annot_names
    annot_df.to_csv(out_fname_annot, sep="\t", header=True, index=False, float_format='%.4f')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default=None, type=str, required=True)
    parser.add_argument('--bfile', default=None, type=str, required=True)
    parser.add_argument('--chr', default=None, type=str)
    parser.add_argument('--annot-bed', default=None, type=str, nargs='+')
    parser.add_argument('--annot-bed-list', default=None, type=str)
    parser.add_argument('--annot-name', default=None, type=str, nargs='+')
    parser.add_argument('--only-annot', default=False, action='store_true')
    args = parser.parse_args()

    if args.annot_bed_list is not None:
        args.annot_bed = []
        with open(args.annot_bed_list, 'r') as f:
            for line in f:
                args.annot_bed.append(line.strip())

    if len(args.annot_bed) != len(args.annot_name):
        raise ValueError('--annot-bed and --annot-name must be the same length.')

    main(args)
