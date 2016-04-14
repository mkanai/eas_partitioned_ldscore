"""
chromtree.py
Kamil Slowikowski
October 30, 2013

This module is a simple extension of

    bx.intervals.intersection.IntervalTree

to neatly handle a dictionary of interval trees.


Here's a usage example:

    from chromtree import ChromTree

    trees = ChromTree()

    # A BED file with intervals on many different chromosomes.
    for line in open("file.bed"):
        chrom, begin, end, name = line.rstrip().split("\t")[:4]
        trees.insert(chrom, int(begin), int(end), name)

    # Retrieve some intervals.
    trees.find("chr1", 1000000, 1100000)

    # Output: ['54991', '254173']


Alternatively, you can avoid using the ChromTree class:

    from bx.intervals.intersection import IntervalTree
    from collections import defaultdict

    trees = defaultdict(IntervalTree)

    for line in open("file.bed"):
        chrom, begin, end, name = line.rstrip().split("\t")[:4]
        trees[chrom].insert(int(begin), int(end), name)

    trees["chr1"].find(1000000, 1100000)

"""


from bx.intervals.intersection import IntervalTree
from collections import defaultdict


class ChromTree(object):
    """A slight extension to bx.intervals.intersection.IntervalTree to
    handle intervals on separate chromosomes."""
    def __init__(self):
        self.trees = defaultdict(IntervalTree)

    def insert(self, chrom, beg, end, value):
        chrom = self._format_chrom(chrom)
        return self.trees[chrom].insert(beg, end, value)

    def find(self, chrom, beg, end):
        chrom = self._format_chrom(chrom)
        return self.trees[chrom].find(beg, end)

    def _format_chrom(self, chrom):
        """Enforce consistent chromosome names."""
        if not type(chrom) == str or not chrom.startswith('chr'):
            chrom = 'chr' + str(chrom)
        return chrom


