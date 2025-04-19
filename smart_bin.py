import os
from time import sleep
import argparse

def bin(path:str, time:int)->list:
    files = os.listdir(path)
    removed = []
    real_files = [os.path.join(path, file) for file in files if os.path.isfile(os.path.join(path, file))]
    for file in real_files:
        if os.path.getctime(file):
            os.remove(file)
        removed.append(file+"removed by lifetime")

    directories = [os.path.join(path, file) for file in files if os.path.isdir(os.path.join(path, file))]
    for directorie in directories:
        bin(directorie)
        try:
            os.rmdir(directorie)
            removed.append(file + "removed by emptiness")
        except:
            pass
    return removed

parser = argparse.ArgumentParser()
parser.add_argument('--trash_folder_path',type=str)
parser.add_argument('--age_thr',type=int)
args = parser.parse_args()
current_path = os.getcwd()
path = args.trash_folder_path
time = args.age_thr
file = open("bin_logs.txt","w")

while(True):
    sleep(1)
    logs = bin(path,time)
    for log in logs:
        file.write(log+"\n")

