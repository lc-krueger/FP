.PHONY: all clean

all: V60.pdf

1PD_spektrum.pdf: aufgabe4.py
	python3 aufgabe4.py

1PD_spektrum_ch1_ch2.pdf: aufgabe4.2.py
	python3 aufgabe4.2.py

2PD_spektrum_fit.pdf: aufgabe5.py
	python3 aufgabe5.py

V60.pdf: V60.tex bilder/aufbau_numm.jpg bilder/band-structure.png bilder/contrib.png bilder/em_ab_stim.png bilder/hl-chip.png bilder/int_vs_git_ext.png bilder/littrow.png bilder/modeshift.png bilder/pn-junction_energy.png bilder/popinv.png bilder/rb_trans.png bilder/strahlung.png bilder/verstaerk_aktmed.png bilder/verstaerk_intcav.png bilder/lasermodus.jpg bilder/rb-Linie.jpg bilder/F0017TEK.jpg bilder/F0018TEK.jpg bilder/F0019TEK.jpg 1PD_spektrum.pdf 1PD_spektrum_ch1_ch2.pdf 2PD_spektrum_fit.pdf
	lualatex V60.tex
	lualatex V60.tex

clean:
	rm -f *.aux *.log *.out *.toc *.xml *.bcf *.blg *.bbl *.run.xml *.fls *.fdb_latexmk