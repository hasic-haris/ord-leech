# Open Reaction Database (ORD) Leech
![](https://raw.githubusercontent.com/Open-Reaction-Database/ord-data/main/badges/reactions.svg)

A project to download and extract reaction data directly from the official ord-data repository.

## Open Reaction Database (ORD)
The [Open Reaction Database](https://docs.open-reaction-database.org/en/latest/) is a 
[published](https://pubs.acs.org/doi/10.1021/jacs.1c09820) open access chemical reaction database. The main goal of 
this project is to support machine learning and related efforts in chemical reaction prediction, chemical synthesis 
planning, and experiment design by:

  - Providing a structured data format for chemical reaction data;
  - Providing an interface for easy browsing and downloading of data;
  - Making the reaction data freely and publicly available for anyone to use;
  - Encouraging the sharing of pre-competitive proprietary data, especially high throughput experimentation data;

It aims to accommodate data relevant to medicinal chemistry, process chemistry, flow chemistry, photochemistry, and 
electrochemistry. Time-course data, unstructured analytical data, and metadata about how the reaction was performed 
will also be accepted. Reactive molecular dynamics simulations, gas-phase reaction kinetics, and electronic structure 
calculations for molecular featurization are being left for other initiatives.

## Git LFS:
Because the ord-data repository handles large data files, it requires the usage of [Git LFS](https://git-lfs.github.com/). 
Thus, in order for this project to work, before cloning anything, you need to have it installed. 
You can follow the installation guidelines [here](https://github.com/git-lfs/git-lfs/wiki/Installation).

## Cloning the Repo:
Step 1: Clone the repository. Update the submodules. Install the environment file. Install the ord-schema requirements.
Step 2: LFS clone the ord-data repository.
Step 3: Run the program.
