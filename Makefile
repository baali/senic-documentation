# convenience makefile to set up the project documentation
# note, that this assumes a checkout of `senic-hub` and `senic-os` on the 
# same folder level as this repository

bin = ../senic-hub/venv/bin

htdocs: $(bin)/sphinx-build *.rst conf.py
	$(bin)/sphinx-build . $@

$(bin)/sphinx-build: senic-hub/index.rst senic-os/README.rst
	$(MAKE) -C ../senic-hub/

senic-hub/index.rst:
	ln -s ../senic-hub/docs senic-hub

senic-os/README.rst:
	ln -s ../senic-os senic-os

clean:
	git clean -fXd

.PHONY: clean htdocs
