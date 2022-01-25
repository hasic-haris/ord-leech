# ord-leech
![](https://raw.githubusercontent.com/Open-Reaction-Database/ord-data/main/badges/reactions.svg)

The main goal of this mini-project is to facilitate the large-scale downloading and filtering of the chemical reaction 
data from the Open Reaction Database (ORD) repositories.


## The Open Reaction Database (ORD)
The [Open Reaction Database](https://docs.open-reaction-database.org/en/latest/) or ORD is an open access chemical 
reaction database established in 2020 by experts from pharma, academia, and tech. [[1]](#References) According to the 
authors, the main goal of this project is to support machine learning and related efforts in chemical reaction 
prediction, chemical synthesis planning, and experiment design by:
  - Providing a structured data format for chemical reaction data;
  - Providing an interface for easy browsing and downloading of data;
  - Making the reaction data freely and publicly available for anyone to use;
  - Encouraging the sharing of pre-competitive proprietary data, especially high throughput experimentation data;


## Setup Instructions
To start using the `ord-leech`, the project repository needs to be cloned by running:

```shell
git clone https://github.com/hasic-haris/ord-leech.git
```

Excluding the `ord-schema` submodule library requirements, the only additionally required library is `tqdm`. Therefore, 
a minimalistic environment can be set up by simply running: 

```shell
conda create -c conda-forge -n ord-leech rdkit
conda activate ord-leech

pip install tqdm
```

The database itself is designed using [Protocol Buffers](https://developers.google.com/protocol-buffers), which is 
explained and handled in the `ord-schema` repository 
[instructions](https://github.com/open-reaction-database/ord-schema/blob/main/README.md). Accordingly, this project 
contains this repository as a submodule so that the newest changes to the schema can always be easily updated, if 
necessary. The `ord-schema` submodule library requirements can be set up by simply running: 

```shell
pip install -r ord-schema/requirements.txt

python ord-schema/setup.py install
```

After the environment is set up, the database files need to be downloaded. Because the `ord-data` repository handles 
large data files, it requires the usage of [Git LFS](https://git-lfs.github.com/). These files can always be downloaded 
dynamically, but in this project the full `ord-data` repository is pre-downloaded to enable offline analysis. The 
installation guidelines for Git LFS can be found [here](https://github.com/git-lfs/git-lfs/wiki/Installation). The 
repository is cloned by running:

```shell
git lfs clone https://github.com/open-reaction-database/ord-data.git
```

This concludes the setup instructions for this project.


## References
1. Kearnes, S.M., Maser, M.R., Wleklinski, M., Kast, A., Doyle, A.G., Dreher, S.D., Hawkins, J.M., Jensen, K.F., and 
Coley, C.W. **The Open Reaction Database**. *J. Am. Chem. Soc.* 2021, 143, 45, 18820–18826. 
DOI: https://doi.org/10.1021/jacs.1c09820.


## License Information
This project is published under the [MIT License](https://opensource.org/licenses/MIT) meaning that it is just a simple 
open-source extension without warranty of any kind. The ORD project is originally published under the 
[CC-BY-SA license](https://creativecommons.org/licenses/by-sa/4.0/) for which the details can be looked up 
[here](https://docs.open-reaction-database.org/en/latest/overview.html#commitment-to-open-access).


## Contact Information
If you are interested in contributing to this project by voicing your opinion, making new functionality suggestions or 
anything else that you think might be beneficial to share, please feel free to do so via GitHub issues or e-mail at 
[Tokyo Institute of Technology](mailto:hasic@cb.cs.titech.ac.jp) or [Elix, Inc](mailto:haris.hasic@elix-inc.com).
