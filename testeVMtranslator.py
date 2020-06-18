#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rafael Corsi @ insper.edu.br
# Dez/2017
# Disciplina Elementos de Sistemas
from os.path import join, dirname
import sys, subprocess

from pathlib import Path
sys.path.insert(0, str(Path.home()) + '/Z01-Tools/scripts/')
from config import *
from assembler import assemblerAll, clearbin
from simulateCPU import simulateFromTestDir
from testeAssembly import compareRam, compareFromTestDir, clearTestDir
from vmtranslator import vmtranslator, vmtranslatorFromTestDir

sys.path.insert(0, './vmTranslator/')
from genJAR import genJAR
from compileVM import compileVM

def testeVM(jarAssembler, jarVM, testDir, vmDir, nasmDir, hackDir, gui, verbose):

    clearbin(nasmDir)
    clearbin(hackDir)

    print("------------------------------")
    print("- Translating src files       ")
    print("- to I-VMTranslator/bin/nasm/ ")
    print("------------------------------")
    compileVM(False, jarVM, vmDir, nasmDir)

    # montador
    print("-------------------------")
    print("- Assembling files .... " )
    print("-------------------------")
    assemblerFromTestDir(jarAssembler, testDir, nasmDir, hackDir)

    # simulando
    print("-------------------------")
    print("- Simulating .... ")
    print("-------------------------")
    simulateFromTestDir(testDir, hackDir, gui, verbose)

    # testAssembling files
    print("-------------------------")
    print("- Testando .... ")
    print("-------------------------")
    compareFromTestDir(testDir)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--testDir", help="lista de arquivos a serem testados")
    ap.add_argument("-v", "--verbose", help="log simulacao", action='store_true')
    ap.add_argument("-g", "--gui", help="carrega model sim", action='store_true')
    args = vars(ap.parse_args())

    pwd = os.path.dirname(os.path.abspath(__file__))
    testDir = pwd+"/tests/testsVMTranslator/"
    vmDir = pwd+"/tests/testsVMTranslator/src/"
    nasm = pwd+"/bin/nasm/"
    hack = pwd+"/bin/hack/"

    genJAR()

    jar = pwd+'/vmTranslator/Z01-VMTranslator.jar'
    print(jar)
    testeVM(ASSEMBLER_JAR, jar , vmDir=vmDir, testDir=testDir, nasmDir=nasm, hackDir=hack, gui=False, verbose=False)
