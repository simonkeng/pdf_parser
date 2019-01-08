'''
    Generate an image for every molecule in SDF

    Usage:
    python generate_images.py structure.sdf

    Contributor: Simon Keng

'''


import sys, os, subprocess
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from IPython.display import Image


def generate_images(input_sdf):
    
    # read in SDF
    sdf = Chem.SDMolSupplier(input_sdf)

    # create dir to store images
    subprocess.call(['mkdir', 'images'])
    os.chdir('images')

    for struct in sdf:

        outfile = struct.GetProp('Lot Supplier ID') + '.png'

        # write out png images, 600 x 600, for each structure 
        rdkit.Chem.Draw.MolToFile(struct, outfile, size=(600, 600))

if __name__ == "__main__":

    generate_images(sys.argv[1])




