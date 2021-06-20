ProdL.pdf: clean
	pandoc \
		-V classoption=b5paper,10pt \
		-V fontfamily=times \
		-V geometry=margin=1in \
		-V colorlinks \
		-f markdown -t pdf \
		ProdL.md > ProdL.pdf

clean:
	-$(RM) ProdL.pdf
