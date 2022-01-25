# ord-leech
![](https://raw.githubusercontent.com/Open-Reaction-Database/ord-data/main/badges/reactions.svg)

The main goal of this project is to facilitate the large-scale downloading and filtering of the chemical reaction data 
from the Open Reaction Database.


## The Open Reaction Database
The [Open Reaction Database](https://docs.open-reaction-database.org/en/latest/) or ORD is an open access chemical 
reaction database established in 2020 by experts from pharma, academia, and tech. [[1]](#References) According to the 
authors, the main goal of this project is to support machine learning and related efforts in chemical reaction 
prediction, chemical synthesis planning, and experiment design by:
   - Providing a structured data format for chemical reaction data;
   - Providing an interface for easy browsing and downloading of data;
   - Making the reaction data freely and publicly available for anyone to use;
   - Encouraging the sharing of pre-competitive proprietary data, especially high throughput experimentation data; 

The Open Reaction Database is split into four repositories: `ord-data`, `ord-schema`, `ord-editor` and `ord-interface`.


## Setup Instructions
To set up this project, the repository needs to be cloned first by running:

```shell
git clone https://github.com/hasic-haris/ord-leech.git
```

Excluding the submodule requirements, the only additionally required library is `tqdm`. Therefore, a minimalistic 
environment can be set up by running: 

```shell
conda create -c conda-forge -n ord-leech rdkit
conda activate ord-leech

pip install tqdm
```

The Open Reaction Database is designed using [Protocol Buffers](https://developers.google.com/protocol-buffers), which 
is [explained](https://github.com/open-reaction-database/ord-schema/blob/main/README.md) in the original schema 
repository. Accordingly, this project contains this repository as a submodule so that the newest changes to the 
database schema can always be easily updated, if necessary. The submodule library requirements can be set up by running: 

```shell
pip install -r ord-schema/requirements.txt

python ord-schema/setup.py install
```

After the environment is set up, the database files need to be downloaded. Because the original data repository handles 
large data files, it requires the usage of [Git LFS](https://git-lfs.github.com/). These files can always be downloaded 
dynamically using `wget`, but in this project the original data repository is pre-downloaded to enable offline analysis. 
The installation guidelines for Git LFS can be found [here](https://github.com/git-lfs/git-lfs/wiki/Installation) and 
the original data repository is cloned by running:

```shell
git lfs clone https://github.com/open-reaction-database/ord-data.git
```


## Usage Instructions
To run this project, simply run the `main.py` file. For now, there are only five arguments that can be specified:
   - `-in` or `--input-directory-path` - The full path to the `../ord-data/data` directory.
   - `-out` or `--output-directory-path` - The full path to a directory where the processing results can be stored.
   - `-meta` or `--extract-dataset-metadata` - The flag to indicate the extraction of the metadata instead of the 
     contents of all available datasets from the Open Reaction Database.
   - `-merge` or `--merge-datasets` - The flag to indicate the merging of the contents of all available datasets 
     from the Open Reaction Database.
   - `-nc` or `--num-cores` - The number of CPU cores used for processing.

An example command that will run the extraction of the reaction identifier, input, condition and output information and 
store them as pickle files is as follows:

```shell
python main.py -in="../ord-data/data/" -out="../project_output/" -nc=10
```

Additional filtering and formatting arguments will be added soon as the project is expanded.


## References
1. Kearnes, S.M., Maser, M.R., Wleklinski, M., Kast, A., Doyle, A.G., Dreher, S.D., Hawkins, J.M., Jensen, K.F., and 
Coley, C.W. **The Open Reaction Database**. *J. Am. Chem. Soc.* 2021, 143, 45, 18820–18826. 
DOI: https://doi.org/10.1021/jacs.1c09820.


## License Information
This project is published under the [MIT License](https://opensource.org/licenses/MIT). The Open Reaction Database 
project is originally published under the [CC-BY-SA License](https://creativecommons.org/licenses/by-sa/4.0/) for which 
the details can be looked up 
[here](https://docs.open-reaction-database.org/en/latest/overview.html#commitment-to-open-access).


## Contact Information
If you are interested in contributing to this project by voicing your opinion, making new functionality suggestions or 
anything else that you think might be beneficial to share, please feel free to do so via GitHub issues or e-mail at 
[Tokyo Institute of Technology](mailto:hasic@cb.cs.titech.ac.jp) or [Elix, Inc](mailto:haris.hasic@elix-inc.com).
