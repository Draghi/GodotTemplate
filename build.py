#!/usr/bin/env python3

from glob import glob;
import sys;
import subprocess;
import os;
import multiprocessing;

threadCount = max(multiprocessing.cpu_count()-2, 2);
target   = sys.argv[1] if len(sys.argv) >= 2 else "debug";
platform = sys.argv[2] if len(sys.argv) >= 3 else "x11";
builddir = os.path.abspath("build/");

os.chdir("ide/");
subprocess.call([
    "scons",
    "-j"+str(threadCount),
    "platform="+str(platform), 
    "target="+str(target), 
    "custom_modules=" + os.path.abspath("../src/"),
    "LINKFLAGS=\"-O0 -r -flinker-output=rel\"",
]);
