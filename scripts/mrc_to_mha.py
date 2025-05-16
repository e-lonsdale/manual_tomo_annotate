import mrcfile
import SimpleITK as sitk
import os
import sys

def convert_mrc_to_mha(mrc_file_path, output_dir):
    # Load the .mrc file
    with mrcfile.open(mrc_file_path, mode='r') as mrc:
        data = mrc.data

    # Create a MetaImage
    img = sitk.GetImageFromArray(data)

    # Save the image
    output_file_name = os.path.splitext(os.path.basename(mrc_file_path))[0] + '.mha'
    output_file_path = os.path.join(output_dir, output_file_name)
    sitk.WriteImage(img, output_file_path)
    print(f"Converted {mrc_file_path} to {output_file_path}")

def main():
    # get vars from command line
    mrc_file = sys.argv[1]
    dataset_id =  sys.argv[2]
    home = os.environ['HOME']

    output_dir = f'{home}/segmentation_data/raw_tomograms/dataset_{dataset_id}'
    # Convert the .mrc file to .mha and save it in the temporary directory
    convert_mrc_to_mha(mrc_file, output_dir)

if __name__ == "__main__":
    main()