default: writeup.pdf

%.html : %.Rmd
	Rscript -e 'library(rmarkdown); render("$<")'

%.pdf : %.Rmd
	Rscript -e 'library(rmarkdown); render("$<", output_format="pdf_document")'

gmake clean: cleancache
	rm -rf *.html

cleancache:
	rm -rf *_cache

