import subprocess, sys, os

filename = sys.argv[1]
volume_location = str(os.getcwd()) + ':/tmp/'
print('Volume location: ', volume_location)

if __name__ == "__main__":

    shell_args = ['docker', 'run', '-dt',
                '-v', volume_location,
                'pdf_parser', filename]

    main_process = subprocess.Popen(shell_args, stdout=subprocess.PIPE)