import napari as nap
import mrcfile as mrc
import starfile as sf
import pandas as pd
import sys

tomogram = sys.argv[1]

with mrc.open(tomogram, permissive=True) as f:
    tomo = f.data

view = nap.Viewer()
view.add_image(tomo, name='tomo', scale=(1, 1, 1), colormap='viridis')

# if adding model points
if len(sys.argv) == 3:
    mp = sys.argv[2]
    df = sf.read(mp).iloc[:,:3]
    cols = df.columns.tolist()
    cols[0], cols[-1] = cols[-1], cols[0]
    df = df[cols]
    mod = df.to_numpy()
    view.add_points(mod, size=10, name='model')

nap.run()