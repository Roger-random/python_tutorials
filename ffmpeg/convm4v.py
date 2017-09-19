#! /usr/local/bin/python3
"""Script that searches for AVI/MPG/MPEG/WMV files in the given source
directory and invokes FFMPEG to convert each file to a M4V file in the
given destination directory"""

import argparse
import os.path
import subprocess

# Argument parsing

parser = argparse.ArgumentParser()

parser.add_argument("sourcedir", help="Source directory of video files to be converted.")
parser.add_argument("destdir", help="Destination directory of converted *.m4v files")

args = parser.parse_args()

sourcedir = os.path.abspath(args.sourcedir)
if not os.path.isdir(sourcedir):
    raise ValueError(sourcedir + " is not a directory")

destdir = os.path.abspath(args.destdir)
if not os.path.isdir(destdir):
    raise ValueError(destdir + " is not a directory")

print("Looking for video files in", sourcedir)
print("Sending converted m4v to", destdir)

sourcedirfiles = os.listdir(sourcedir)

convert_success = list()
convert_skipped = list()
convert_failed = list()

for file in sourcedirfiles:
    # Check out the "from"
    fullsrc = os.path.join(sourcedir, file)
    if not os.path.isfile(fullsrc):
        print(fullsrc, "is not a file, skipping")
        convert_skipped.append(fullsrc)
        continue
    if not fullsrc.lower().endswith(('avi','mpg','mpeg','wmv')):
        print(fullsrc, "is not a recognized video file, skipping")
        convert_skipped.append(fullsrc)
        continue

    # "from" checks out, look over "to"
    dest = os.path.splitext(file)[0]+'.m4v'
    fulldest = os.path.join(destdir, dest)
    if os.path.exists(fulldest):
        print(fulldest, "already exists, skipping")
        convert_skipped.append(fullsrc)
        continue

    # Both "from" and "to" checks out, try to convert...
    runresult = subprocess.run(["ffmpeg", "-i", fullsrc, fulldest], check=True)
    if runresult.returncode==0:
        convert_success.append(fulldest)
    else:
        convert_failed.append(runresult)

if len(convert_success) > 0:
    print(len(convert_success),"converted")
    for cs in convert_success:
        print("    ",cs)

if len(convert_skipped) > 0:
    print(len(convert_skipped),"skipped")
    for cs in convert_skipped:
        print("    ",cs)

if len(convert_failed) > 0:
    print(len(convert_failed),"failed")
    for cf in convert_failed:
        print("    Error code:",cf.returncode," when executing ",cf.args)
