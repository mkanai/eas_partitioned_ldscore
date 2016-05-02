# Partitioned LD Scores for the EAS population

The aim of this repository is to provide a pre-computed partitioned LD Score for the EAS population, which is used in the [`ldsc`](https://github.com/bulik/ldsc) partitioning heritability analysis.

**The files are yet incomplete and still undergoes a validation process.**

## Requirements
These requirements are only for those who want to reproduce our calculations. You can use our pre-computed partitioned LD scores by just downloading them from the [release page](https://github.com/mkanai/eas_partitioned_ldscore/releases).

* [Python](https://www.python.org/)
* [GNU Parallel](http://www.gnu.org/software/parallel/) (to be replaced)
* [ldsc](https://github.com/bulik/ldsc)

### Python packages
* [numpy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [bx-python](https://pypi.python.org/pypi/bx-python)

### Datasets
* The 1000 Genomes Projects Phase 3 (version 5a) dataset
    * The original `.vcf` files were retrieved from their [ftp site](ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/).
    * We then converted them to appropriate PLINK `.bed` format by using `convert2plink.sh`.
    * All PLINK files are provided as `1000G_plinkfiles_EAS.tar.gz`. Users do *not* have to download the original 1000 Genomes Project dataset.

* The original `.bed` files for annotation provided by the authors.
    * Please retrieve them from [here](http://data.broadinstitute.org/alkesgroup/LDSCORE/), and place them appropriately.
    * The `.bed` files for baseline is `baseline_bedfiles.tgz`, and for cell-type/cell-type-group specific annotation is `ct_and_ctg_bedfiles.tgz`.
    * Then, edit the scripts to set the path to these files.

## Usage
You can **download** our pre-computed partitioned LD scores for the EAS population from [here](https://github.com/mkanai/eas_partitioned_ldscore/releases). More detailed usage of those files can be found at the original `ldsc` [wiki](https://github.com/bulik/ldsc/wiki/Partitioned-Heritability).

For those who want to replicate our calculations, you can run the following command for *e.g.* baseline annotations.
```bash
mkdir baseline && cd $_
for chr in $(seq 22); do
    ../baseline.sh ../1000G_plinkfiles_EAS/1000G.mac5asn.$chr
done
```

## Acknowledgements

* The [`ldsc`](https://github.com/bulik/ldsc) was developed by [Brendan Bulik-Sullivan](https://github.com/bulik) and [Hilary Finucane](https://github.com/bulik). The original `.bed` files for the categories were provided by the authors and retrieved from [here](http://data.broadinstitute.org/alkesgroup/LDSCORE/).
    - Bulik-Sullivan, B. K. *et al.* LD Score regression distinguishes confounding from polygenicity in genome-wide association studies. *Nat. Genet.* **47**, 291–295 (2015). [doi:10.1038/ng.3211](http://www.nature.com/doifinder/10.1038/ng.3211).
    - Finucane, H. K. *et al.* Partitioning heritability by functional annotation using genome-wide association summary statistics. *Nat. Genet.* **47**, 1228–1235 (2015). [doi:10.1038/ng.3404](http://www.nature.com/doifinder/10.1038/ng.3404).
* [`chromtree.py`](https://gist.github.com/slowkow/7220475) was written by [Kamil Slowikowski](https://github.com/slowkow).

## Contact
Masahiro Kanai
* masahiro.kanai@riken.jp
* http://mkanai.github.io/
