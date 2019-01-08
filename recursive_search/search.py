import subprocess, os

cids = [
    'MRT-B0659-P1',
    'MRT-B0659-P2',
    'MRT-B0662-P1',
    'MRT-B0662-P2',
    'MRT-B0666-B-P1',
    'MRT-B0666-B-P2',
    'MRT-C0526',
    'MRT-D0373-2',
    'MRT-D0376-1',
    'MRT-D0369-P2',
    'MRT-D0381',
    'MRT-E0204',
    'MRT-E0207',
    'MRT-B0682-P4'
        ]


def run_shell_script(item_list):
    
    for i in item_list:

        with open('catalog.txt', 'a') as f:
            
            print(f'Searching for {i}')

            script_path = os.path.dirname(__file__) + '/search.sh'
            
            subprocess.call([script_path, i], stdout=f)


if __name__ == "__main__":

    run_shell_script(cids)
        
