#!/usr/bin/python
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outroot', '-o', dest='outroot', required=True)
parser.add_argument('--num_images', '-n', dest='num_images', required=True)
args = parser.parse_args()

for pic_num in range(0, int(args.num_images)):
    print("Taking photo %i" % pic_num)
    os.system("raspistill -w 160 -h 160 -o %s/image-%i.jpg" % (args.outroot, pic_num))
    time.sleep(1)
