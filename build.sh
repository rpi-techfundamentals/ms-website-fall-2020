#!/bin/bash
book=quant/
#cd scripts && python convert.py
#jupyter-book toc ./$book
jupyter-book build $book
