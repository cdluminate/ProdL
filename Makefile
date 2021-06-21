ProdL.pdf: clean
	pandoc \
		-V classoption=b5paper,10pt \
		--toc -V toccolor=magenta \
		-V fontfamily=times \
		-V geometry=margin=1in \
		-V colorlinks \
		-f markdown -t pdf \
		ProdL.md > ProdL.pdf

clean:
	-$(RM) ProdL.pdf
