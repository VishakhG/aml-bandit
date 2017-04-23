all:
	pdflatex bandit_review.tex
	bibtex bandit_review
	pdflatex bandit_review.tex
	open bandit_review.pdf
sup:
	pdflatex appendix.tex
	bibtex appendix
	pdflatex appendix.tex
	open appendix.pdf
clean:
	rm *.aux *.brf *.pdf *.log *.bbl *.blg *.dvi *.ps *.out *.fdb_latexmk *.synctex.gz
