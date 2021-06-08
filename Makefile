ProdL.pdf:
	pandoc -V fontfamily=times \
		-V geometry=margin=1in \
		-V colorlinks \
		-f markdown -t pdf \
		ProdL.md > ProdL.pdf

clean:
	-$(RM) ProdL.pdf
