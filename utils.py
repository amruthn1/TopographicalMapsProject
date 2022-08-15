import os
import sys

from parseCSV import clean_dir
from segmentPNG import cleanse_dir
from generateCoords import cleanMetadata, cleanDir


def init():
    # Clean .gitkeep files before proceeding
    print("Cleaning .gitkeep files if they exist")
    if os.path.exists('./temp/img/.gitkeep'):
        os.remove('./temp/img/.gitkeep')
    if os.path.exists('./temp/pdf/.gitkeep'):
        os.remove('./temp/pdf/.gitkeep')
    if os.path.exists('./sliced/.gitkeep'):
        os.remove('./sliced/.gitkeep')
    if os.path.exists('./segmentedoutputs/.gitkeep'):
        os.remove('./segmentedoutputs/.gitkeep')
    if os.path.exists('./metadata/.gitkeep'):
        os.remove('./metadata/.gitkeep')
    if os.path.exists('./blurred/.gitkeep'):
        os.remove('./blurred/.gitkeep')


def deploy():
    # Add .gitkeep files before deploying
    print("Adding .gitkeep files if they don't exist")
    if not os.path.exists('./temp/img/.gitkeep'):
        open('./temp/img/.gitkeep', 'w')
    if not os.path.exists('./temp/pdf/.gitkeep'):
        open('./temp/pdf/.gitkeep', 'w')
    if not os.path.exists('./sliced/.gitkeep'):
        open('./sliced/.gitkeep', 'w')
    if not os.path.exists('./segmentedoutputs/.gitkeep'):
        open('./segmentedoutputs/.gitkeep', 'w')
    if not os.path.exists('./metadata/.gitkeep'):
        open('./metadata/.gitkeep', 'w')
    if not os.path.exists('./blurred/.gitkeep'):
        open('./blurred/.gitkeep', 'w')


def clean():
    # Clean out all project directories
    clean_dir()
    cleanse_dir()
    cleanDir()
    cleanMetadata()


if __name__ == "__main__":
    if 'deploy' in str(sys.argv):
        deploy()
    elif 'init' in str(sys.argv):
        init()
    elif 'clean' in str(sys.argv):
        clean()
    else:
        raise Exception("Invalid argument")
