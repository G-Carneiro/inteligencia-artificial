# inteligencia-artificial
Trabalhos da disciplina INE5430 - Inteligência Artificial (UFSC).

## Markdown to PDF

### Requirements

```
sudo apt install pandoc texlive-xetex
```


### Convert

```shell
pandoc file.md -o file.pdf --pdf-engine=xelatex
```

or

```shell
 pandoc file.md -o file.pdf --pdf-engine=xelatex -V geometry:landscape
```