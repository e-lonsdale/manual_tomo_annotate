## About
This repository hosts the necessary scripts to create labeled data for tomograms to be used in model training. This data can range from segmenting entire bacteria to labeling flagellar motors. This [log](https://docs.google.com/spreadsheets/d/1-osjVjA0YVw-CQIwIVUC7IbxnDa7ZMKbNN8waf8KUxg/edit?gid=0#gid=0) keeps track of which tomograms have been labeled and which ones we want to do next.

#### What you need
- Conda
- Python
- ITK-SNAP

#### Set up/Installation
1. Install conda if you haven't. I recommend using miniforge, as it has mamba built in which is a faster package management algorithm. On Mac, this can be installed with homebrew. However, any version of conda should work.
    1. Install homebrew with `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    2. Install miniforge using `brew install --cask miniforge`.
2. Install ITK-SNAP, the GUI used to actually annotate (Download [here](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP3))
3. Clone this github repository
4. In the terminal, navigate to the folder manual_tomo_annotate and run the command `chmod +x env_setup.sh`. This will make the setup script executable.
5. Run `./env_setup.sh` to build the conda environment and folder structure for annotating. This script will automatically name the conda environment `annotate`, but if you already have an enviornment named this run `./env_setup.sh -n <conda_env_name>` to create the enviornment with a different name.

#### Use
1. Activate the conda environment using `conda activate annotate` or `conda activate <conda_env_name>` if you named it something else.
2. Run `annotate.sh -d <dataset_id> -r <run_id>` to download a tomogram and segment.
3. Save the segmentation image as described below in the File Convention section.

#### Uploading to Supercomputer
Check back soon.
## File Conventions for Segmentation Data
Please do your best to follow the below conventions so all the data can stay organized. They're not set in stone, but we do need to make sure we know where all the data is and that everyone can find it easily.

#### File Structure for Annotation Data
Note: the `env_setup.sh` and `annotate.sh` scripts should auto-build these directories. They **will not** end up in the GitHub repo, as tomograms are too big to store there. So, don't worry that these files do not show up on the repository, as we will primarily be storing files on the supercomputer.


**Note:** DO NOT move the segmentation_data directory or its subdirectories from where they are created. Doing so will make the other scripts non-functional, as they will not be able to find the folders.
```
.
├── segmentation_data
│   ├── raw_tomograms # directory for raw images
│   │   ├── dataset_1
│   │   │   ├── tomo_1.mha
│   │   │   └── tomo_2.mha
│   ├── annotations # directory for segmentation files
│   │   ├── dataset_1
│   │   │   ├── annotation_1.mrc
│   │   │   └── annotation_2.mrc
│   │   └──
│   └──
└──
```
#### File Names
Raw images are automatically downloaded, converted, and renamed to `run_<runID>.mha`. They are saved in the directory `dataset_<datasetID>`. All IDs correspond to the CZI database IDs.

Annotations should be saved following the pattern `<annotation_type>_<runID>`. For example, a membrane segmentation from dataset 10084, run 6100 would be saved as `segmentation_data/annotations/dataset_10084/membrane_6100.mha`.

| Annotation Type | File name convention |
|-----------------|----------------------|
| Membrane        |`membrane_<runID>`|
