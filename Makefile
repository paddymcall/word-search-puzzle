all: main.pdf main_no_solutions.pdf

main_no_solutions.tex: main.tex ./game_boards/current.table
	sed 's|\\input{./game_boards/current.solution}||g' main.tex > main_no_solutions.tex

main_no_solutions.pdf: ./game_boards/current.table
	latexmk main_no_solutions.tex

main.pdf: ./game_boards/current.table main.tex
	latexmk main.tex

./game_boards/current.table: words.txt variables.py main.py functions.py
	guix shell --container \
	coreutils python python-numpy python-unidecode -- \
	python3 main.py

clean:
	rm -f main.pdf main_no_solutions.pdf

clean-all: clean
	rm -f game_boards/current.*
