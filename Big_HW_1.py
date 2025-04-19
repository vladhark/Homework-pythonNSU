import os
#import re
import argparse

def walk(path:str, ignore:list):
    files = os.listdir(path)
    real_files = [os.path.join(path,file) for file in files if os.path.isfile(os.path.join(path,file))]
    directories = [file for file in files if os.path.isdir(os.path.join(path,file))]
    out = []
    for file in real_files:
        #print(file)
        print(ignore)
        for to_ignore in ignore:
            #print("-"+to_ignore)
            if to_ignore[0]=="*":
                if file[::-1].find(to_ignore[::-1][:-1])==0:
                    out.append(file+' ignored by expression '+to_ignore)
            else:
                if file==os.path.join(path,to_ignore):
                    out.append(file + ' ignored by expression ' + to_ignore)
    #print(path,real_files,directories)
    for sub_path in directories:
        new_path = os.path.join(path,sub_path)
        if os.path.isdir(new_path):
            out += walk(new_path,ignore)
    return out

def out_to_normal_view(path:str,out:list):
    for i in range(len(out)):
        out[i] = out[i][len(path):]
    return out

def out(out:list):
    for statement in out:
        print(statement)

def out_file(path_to_write:str,out:list):
    file = open(path_to_write,"w")
    for statement in out:
        file.write(statement+"\n")
    file.close()

def gitignore_in(path:str)->list:
    file = open(os.path.join(path,".gitignore"))
    return file.readlines()
parser = argparse.ArgumentParser()
parser.add_argument('--route',type=str)
path = parser.parse_args().route
current_path = os.getcwd()
#path = ""
path_to_ignore = os.path.join(current_path,path)
ignore = gitignore_in(path_to_ignore)
path_to_write = os.path.join(path_to_ignore,"ignored.txt")
print(ignore)
out_file(path_to_write, out_to_normal_view(path_to_ignore,walk(path_to_ignore,ignore)))
#out(out_to_normal_view(path_to_ignore,walk(path_to_ignore,ignore)))