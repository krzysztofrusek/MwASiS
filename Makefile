CONF=nbconf.py


%.pdf: %.md
	pandoc $< -o $@ -t beamer --slide-level 2 --resource-path=out


out/Modele_probabilistyczne.md: wykład/Modele_probabilistyczne.ipynb
	jupyter nbconvert --config nbconf.py  --output-dir=out  $<
	sed -i '' 's/\[svg/\[/g' $@

wyklady: out/Modele_probabilistyczne.pdf

stud:
	mkdir -p stud



stud/%.ipynb: ćwiczenia/%.ipynb stud
	python3 -m nbconvert \
	--to notebook \
	--output $@ \
	--TagRemovePreprocessor.enabled=True \
	--TagRemovePreprocessor.remove_cell_tags='hide' \
	--output-dir=.  $<

# stud/%.tar.gz: stud/%.ipynb data requirements.txt
# 	 tar -cvzf $@ $^

stud/%.tar: stud/%.ipynb
	tar -cvf $@ -C stud $*.ipynb
	# tar -rvhf $@  -C data/$* .

%.tar.gz: %.tar
	gzip $^

cw: stud/Obliczenia_techniczne_Ćwiczenia.tar.gz 

clean:
	rm -rf out stud

.PHONY: gdown laby



all: laby wyklady