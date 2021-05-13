a='''
#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    std::cout<<"hellwo";

    
    return 0;
}

import shlex,subprocess

def run(cmd: str):
    cmd = shlex.split(cmd)
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
'''
