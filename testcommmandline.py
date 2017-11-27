#!/usr/bin/env python
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ID', help='ID of device for upgrade')
    args = parser.parse_args()
    CpxID = args.ID;
    print("Upgrading " + CpxID )
main()
