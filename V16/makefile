.PHONY: all clean

all: V16.pdf

V16.pdf: V16.tex bilder/Thermschema.png bilder/Aufbau_foto.jpg bilder/Abmessungen.png bilder/Drehschieberpumpe.png bilder/Scrollpumpe.png
	lualatex V16.tex
	lualatex V16.tex
clean:
	rm -f *.aux *.log *.out *.pdf *.toc *.xml *.bcf *.blg *.bbl *.run.xml *.fls *.fdb_latexmk