# Overview #

**FiMO** is a Bayesian method for inferring the temporal order of somatic mutations from noisy SCS mutational profiles under tumor evolutionary models that account for mutation recurrence and losses.

# Dependencies #

* [NumPy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
* [ete3](http://etetoolkit.org/)
* [deque](https://docs.python.org/3/library/collections.html#collections.deque)

# Usage #

We have provided two jupyter notebooks *finte_model.ipynb* and *dollo_model.ipynb*  for the Finite-site model and Dollo model, respectively. To run them, use [jupyter notebook](https://jupyter.org/) and use the second cell of each jupyter notebook to configure parameters.

We have also provided sample data files in the *data* folder for both models. *data/s1* is for Finite-site model and *data/s2* for Dollo-model. Configuration of these sample datasets are provided in *config* file inside *s1* and *s2*.

## Input Data Arguments ##

* ```nclones = <Integer>``` Replace <Integer> with the number of clones without including normal clone.

* ```ncells = <Integer>``` Replace <Integer> with the number of cells (columns) in the dataset (without including normal cells).

* ```clonal_mut =  <Double>``` Replace <Double> with rate of clonal mutation.

* ```recc_rate = <Double>``` Replace <Double> with recurrent mutation rate.

* ```fp = <Double>``` Replace <Double> with false positive rate.

* ```fn = <Double>``` Replace <Double> with false negative rate.

* ```d_dollo = <Integer>``` Replace <Integer> with dollo-d parameter d, denotes maximum number of back mutation. This parameter required for Dollo Model only. 

* ```file_tree = <filepath>``` Replace <filename> with the path to the file containing the clonal tree without cells in Newick format with all branches and all names.

* ```file_obs = <filepath>``` Replace <filename> with the path to the file containing the observed binary genotype matrix (without missing data). Columns represent cells, and row represents mutation sites. This file should be in .csv format.

* ```file_map = <filepath>``` Replace <filename> with the path to the file containing the mapping of cells to clones. Columns represent cells, and the first row has the corresponding clone for the cell that belongs to the column. This file should be in .csv format.

# Output

* probabilities.csv: This file contains posterior probabilities for mutations on a particular branch(es).

* predict_loc.csv: This file have the location of mutation on a tree (we gave numbers to branches in pre-order traversal).

* result.csv: This file have the location of mutation on a tree and observed binary genotype.

