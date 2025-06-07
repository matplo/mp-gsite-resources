#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# find all the html files in the current directory and subdirectories
# add the subdirectory to the base http path
# print the list

import os
import sys
import glob
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate HTTP paths for HTML files.')
    parser.add_argument('-b', '--base_http_path', default='https://matplo.github.io/mp-gsite-resources/', help='Base HTTP path to prepend to HTML file paths')
    args = parser.parse_args()
    base_http_path = args.base_http_path
    html_files = sorted(glob.glob('**/*.html', recursive=True))

    dirs = []
    for f in html_files:
        d = os.path.dirname(f)
        if d not in dirs:
            dirs.append(d)
      
    unique_dirs = set(dirs)
    done_subdirs = []
    first_dir = True
    for html_file in html_files:
        subdir = os.path.dirname(html_file)
        if subdir:
            http_path = os.path.join(base_http_path, subdir)
        else:
            http_path = base_http_path
        html_link = os.path.join(http_path, os.path.basename(html_file))
        html_dir_path = os.path.dirname(html_link)
        if html_dir_path not in done_subdirs:
          if first_dir:
              print(f"- Base HTTP path: {base_http_path}")
              first_dir = False
          done_subdirs.append(html_dir_path)
          print(f"\n- Directory: {html_dir_path}")
        print('   ', html_link)
    
if __name__ == "__main__":
    main()