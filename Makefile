manuscript = answinter
references = answinter
latexopt   = -halt-on-error -file-line-error

all: all-via-pdf r2s

all-via-pdf: $(manuscript).tex $(references).bib
	pdflatex $(latexopt) $(manuscript)
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $(manuscript)
	pdflatex $(latexopt) $(manuscript)

all-via-dvi:
	latex $(latexopt) $(manuscript)
	bibtex $(manuscript).aux
	latex $(latexopt) $(manuscript)
	latex $(latexopt) $(manuscript)
	dvipdf $(manuscript)

clean:
	rm -f *.pdf *.dvi *.toc *.aux *.out *.log *.bbl *.blg *.log *.spl *~ *.spl *.zip

realclean: clean
	rm -rf $(manuscript).dvi
	rm -f $(manuscript).pdf

%.ps :%.eps
	convert $< $@

%.png :%.eps
	convert $< $@

zip:
	zip paper.zip *.tex *.eps *.bib

r2s:
	dot -Tpdf -l r2s.ps r2s.dot -o r2s.pdf

.PHONY: all clean
