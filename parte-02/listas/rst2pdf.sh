#!/bin/bash

file_name=lista02

pandoc ${file_name}.rst -o ${file_name}.md
pandoc header.yaml ${file_name}.md -o ${file_name}.pdf --pdf-engine=xelatex
rm ${file_name}.md
