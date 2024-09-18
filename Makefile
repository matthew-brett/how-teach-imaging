default: slides

all: slides handout

SOURCE=how_teach_imaging
LINK_COLOR=blue

# Need gpp for conditional stuff
# `brew install gpp` on macOS

# HTML options, without \ as quoting character (otherwise it will disable LaTeX
# macros).
GPP=gpp -U "<\#" ">" "\B" "|" ">" "<" ">" "\#" ""

DO_PANDOC=pandoc --citeproc --variable urlcolor=$(LINK_COLOR) -o

slides: $(SOURCE).md
	$(GPP) $(SOURCE).md | $(DO_PANDOC) \
		$(SOURCE)_slides.pdf \
		-t beamer

handout: $(SOURCE).md
	$(GPP) -DHANDOUT=1 $(SOURCE).md | $(DO_PANDOC) \
		$(SOURCE)_handout.pdf

clean:
	rm *.pdf
