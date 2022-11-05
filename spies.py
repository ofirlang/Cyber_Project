#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Log-puzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like: 10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg 
HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6" """


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    image_urls = []
    with open(filename, 'r') as place_code:
        for line in place_code:
            get = line.index('GET')
            jpg_in_line = re.findall("jpg", line)
            if jpg_in_line:
                jpg = line.index('jpg')
                url = "https://"  # + hostname + line[get + 4:jpg + 3]
            if url not in image_urls:
                image_urls.append(url)
        image_urls.sort()
    return image_urls


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    img_number = 0
    for url in img_urls:
        with urllib.request.urlopen(url) as response:
            image = response.read()
            file_name = dest_dir + "\\img" + str(img_number)
            with open(file_name, 'wb') as img:
                img.write(image)
        img_number += 1
    with open(dest_dir + "\\index.html", 'a+') as index:
        index.write('<!DOCTYPE html>\n'
                    '<html lang="en">\n'
                    '<head>\n'
                    '<meta charset="UTF-8">\n'
                    '<meta http-equiv="X-UA-Compatible" content="IE=edge">\n'
                    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                    '<title>Document</title>'
                    '</head>\n'
                    '<body>\n')
        for entry in os.listdir(dest_dir):
            if "img" in entry:
                path = dest_dir + "\\" + entry
                index.write(f'<img src="{path}" alt="Image not found">\n')
        index.write('</body>\n'
                    '</html>')


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
