.PHONY: all clean

all: V60.pdf

1PD_spektrum.pdf: aufgabe4.py
	python3 aufgabe4.py

1PD_spektrum_ch1_ch2.pdf: aufgabe4.2.py
	python3 aufgabe4.2.py

2PD_spektrum_fit.pdf: aufgabe5.py
	python3 aufgabe5.py

V60.pdf: V60.tex bilder/lasermodus.jpg bilder/rb-Linie.jpg bilder/F0017TEK.jpg bilder/F0018TEK.jpg bilder/F0019TEK.jpg 1PD_spektrum.pdf 1PD_spektrum_ch1_ch2.pdf 2PD_spektrum_fit.pdf
	lualatex V60.tex
	lualatex V60.tex

clean:
	rm -f *.aux *.log *.out *.toc *.xml *.bcf *.blg *.bbl *.run.xml *.fls *.fdb_latexmk