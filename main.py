import os, shutil, filecmp
import random, string
from colorama import Fore, Style
import glob

random.seed(1)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def create_random_file(parent_dir):
    filename = get_random_string(8) + '.txt'
    full_path = os.path.join(parent_dir, filename)
    f = open(full_path, "w")
    f.write(get_random_string(128))
    f.close()

class ZipadorTest():
    def __init__(self, test_number, root_dir):
        self.test_number = test_number
        self.parent_dir = os.path.join(root_dir, "zipador_test{}".format(self.test_number))
        self.lab_number = random.randint(1, 9)
        self.relatorio_filename = "relatorio.pdf"
        self.diretorio_dirname = "KT-213_Lab{}".format(self.lab_number)

    def setup(self):
        # Create a new parent directory for isolating the test
        os.mkdir(self.parent_dir)
        # Create files
        # relatorio
        relatorio_path = os.path.join(self.parent_dir, self.relatorio_filename)
        relatorio_file = open(relatorio_path, "w")
        relatorio_file.write("Hello World!")
        relatorio_file.close()

        # diretorio
        diretorio_path = os.path.join(self.parent_dir, self.diretorio_dirname)
        os.mkdir(diretorio_path)

        # Create files within <diretorio>
        for _ in range(5):
            create_random_file(diretorio_path)
        
        # Copy zipador.sh into parent dir
        try:
            shutil.copy('./zipador.sh', self.parent_dir)
        except FileNotFoundError:
            print(Fore.RED + "File \'zipador.sh\' not found!")
            return

    def cleanup(self):
        try:
            shutil.rmtree(self.parent_dir)
        except FileNotFoundError:
            printcolored(Fore.BLUE, "The previous test dir was not found. Moving on...")

    def run(self):
        os.chdir(self.parent_dir)
        
        command = "./zipador.sh {} {}".format(self.relatorio_filename, self.diretorio_dirname)
        print("-- Script output --")
        os.system(command)
        print("-- End of script --")
        correct_filename = "ze_zinho_lab{}.zip".format(self.lab_number)
        # Test if file was created with proper naming
        if os.path.isfile(correct_filename):
            printcolored(Fore.GREEN, "The file {} was created successfully!".format(correct_filename))
        else:
            printcolored(Fore.RED, "The file {} was not created! There is a problem with this program.".format(correct_filename))
            return -1
        # Decompress file and check if its contents are the same as the source
        decompress_dirname = "decompressed"
        decompress_cmd = "unzip {} -d {}".format(correct_filename, decompress_dirname)
        os.system(decompress_cmd)
        # Compare files
        relatorio_dcmp_path = os.path.join(decompress_dirname, self.relatorio_filename)
        if filecmp.cmp(self.relatorio_filename, relatorio_dcmp_path):
            printcolored(Fore.GREEN, "{} appears correctly in the decompressed archive!".format(self.relatorio_filename))
        else:
            printcolored(Fore.RED, "{} doesn't appear in the decompressed archive!".format(self.relatorio_filename))
            return -1
        # Compare directories
        diretorio_dcmp_path = os.path.join(decompress_dirname, self.diretorio_dirname)
        dircmp = filecmp.dircmp(self.diretorio_dirname, diretorio_dcmp_path)
        if len(dircmp.diff_files) == 0:
            printcolored(Fore.GREEN, "The {} directory appears correctly in the decompressed archive!".format(self.diretorio_dirname))
        else:
            printcolored(Fore.RED, "The {} directory does not appear correctly in the decompressed archive!".format(self.diretorio_dirname))
            return -1
        return 0

def printcolored(foreground, text):
    print(foreground + text)
    print(Style.RESET_ALL, end='')

# Root directory
root_dir = os.getcwd()

failed_tests = []

for i in range(1, 10):
    test = ZipadorTest(i, root_dir)
    test.cleanup()
    test.setup()
    result = test.run()
    if result != 0:
        failed_tests.append(i)

if len(failed_tests) == 0:
    printcolored(Fore.GREEN, "Passed all tests! Yaay :D")
else:
    for i in failed_tests:
        printcolored(Fore.RED, "Error on test #{}".format(i))
