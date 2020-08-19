#!/bin/bash
book=quant/
#cd scripts && python convert.py
#cd ..
pandoc -s syllabus.docx -t markdown -o ./quant/syllabus.md
jupyter-book toc ./$book
jupyter-book build $book
