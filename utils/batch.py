import os, sys, subprocess

def main(folder):

    os.chdir(folder)

    for fname in os.listdir(os.getcwd()):
        print 'Working on file: ' + str(fname)
        subprocess.call(['python', '../pdf_rip.py', fname])
        print 'Extraction complete'

if __name__ == "__main__":
    main(sys.argv[1])

