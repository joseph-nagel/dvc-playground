# DVC playground

A small playground for learning how to do data versioning with [DVC](https://dvc.org/) is established.
Version control for data sets tries improve the reproducibility of ML workflows.
It allows for more controlled experimentation and development.


## Instructions

DVC can be easily installed through `pip install dvc`.
Running the script `./make_data.sh` creates a directory of example dummy data.
Following that, DVC is intialized by calling `dvc init`
and the data can be added for tracking by `dvc add data/`.

```
pip install dvc
./make_data.sh
dvc init
dvc add data/
```
