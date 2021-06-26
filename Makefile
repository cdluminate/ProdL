ProdL.pdf: clean
	pandoc \
		-V classoption=b5paper,10pt \
		--toc -V toccolor=magenta \
		-V fontfamily=times \
		-V geometry=margin=1in \
		-V colorlinks \
		--pdf-engine pdflatex \
		-H assets/header.tex \
		-f markdown -t pdf \
		ProdL.md > ProdL.pdf

ProdL.tex:
	pandoc -f markdown -t latex ProdL.md --toc -r markdown-auto_identifiers --standalone > ProdL.tex

clean:
	-$(RM) ProdL.pdf
