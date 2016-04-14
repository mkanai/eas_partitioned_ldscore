# Partitioned LD Scores for the EAS population

The aim of this repository is to provide a pre-calculated partitioned LD Score for the EAS population, which is used in the [`ldsc`](https://github.com/bulik/ldsc) partitioning heritability analysis.

**The files are yet incomplete and still undergoes a validation process.**

## Requirements
* Python
* GNU Parallel (to be replaced)

### Python packages
* [numpy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [bx-python](https://pypi.python.org/pypi/bx-python)

## Usage

To generate baseline annotations, I ran the following command. More detailed documentation/help will be added.
```bash
mkdir baseline && cd $_
for chr in $(seq 22); do
    ../baseline.sh ../1000G_plinkfiles_EAS/1000G.mac5asn.$chr
done
```

## Acknowledgements

* The [`ldsc`](https://github.com/bulik/ldsc) was developed by [Brendan Bulik-Sullivan](https://github.com/bulik) and [Hilary Finucane](https://github.com/bulik). The original `.bed` files for the categories were provided by the authors and retrieved from [here](http://data.broadinstitute.org/alkesgroup/LDSCORE/baseline_bedfiles.tgz).
    - Bulik-Sullivan, B. K. *et al.* LD Score regression distinguishes confounding from polygenicity in genome-wide association studies. *Nat. Genet.* **47**, 291–295 (2015). [doi:10.1038/ng.3211](http://www.nature.com/doifinder/10.1038/ng.3211).
    - Finucane, H. K. *et al.* Partitioning heritability by functional annotation using genome-wide association summary statistics. *Nat. Genet.* **47**, 1228–1235 (2015). [doi:10.1038/ng.3404](http://www.nature.com/doifinder/10.1038/ng.3404).
* [`chromtree.py`](https://gist.github.com/slowkow/7220475) was written by [Kamil Slowikowski](https://github.com/slowkow).

## Contact
Masahiro Kanai
* masahiro.kanai@riken.jp
* http://mkanai.github.io/

