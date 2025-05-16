from cryoet_data_portal import Client, Run, Tomogram
"""
This script downloads a tomogram file from the cryoET data portal and saves it to a specified directory.

Usage:
    python auto_tomo_download.py <datasetid> <runid>

Arguments:
    datasetid: The ID of the dataset to download.
    runid: The ID of the run to download.

Environment Variables:
    HOME: The home directory of the user, used to construct the dataset and annotation directories.

Directories:
    segmentation_data/raw_tomograms/dataset_<datasetid>: Directory where the downloaded tomogram will be saved.
    segmentation_data/annotations/dataset_<datasetid>: Directory where annotations related to the dataset will be saved.

Steps:
1. Create dataset and annotation directories if they do not exist.
2. Change the current working directory to the dataset directory.
3. Find the specified run using the provided dataset ID and run ID.
4. Retrieve the tomogram associated with the run.
5. Download the tomogram file in MRC format.
6. Rename the downloaded file to 'run_<runid>.mrc'.
"""
import sys
import os

client = Client()

# IDs for run to download
datasetid = sys.argv[1]
runid = sys.argv[2]

# set dataset directory
home = os.environ['HOME']
dataset_dir = os.path.join(home,'segmentation_data/raw_tomograms','dataset_'+datasetid)
annotation_dir = os.path.join(home,'segmentation_data/annotations','dataset_'+datasetid)
# create dataset and annotation directories if they don't exist and move into dataset dir
os.makedirs(dataset_dir, exist_ok=True)
os.makedirs(annotation_dir, exist_ok=True)
os.chdir(dataset_dir)
# get correct run and download it
run = Run.find(client, query_filters=[Run.id == runid, Run.dataset.id == datasetid])[0]
tomoid = run.tomogram_voxel_spacings[0].tomograms[0].id
tomogram = Tomogram.get_by_id(client, tomoid)
tomogram.download_mrcfile()

# rename file
new_file_name = 'run_'+runid+'.mrc'
os.rename(tomogram.name+'.mrc',new_file_name)