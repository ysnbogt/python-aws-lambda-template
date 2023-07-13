libraries      := $(shell cat ../requirements.txt | tr '\n' ' ' | tr -s ' ')
python_version ?=

package:
	@cp -r ../src/* . \
	&& python${python_version} -m pip install ${libraries} -t . \
	&& zip -r ../layer.zip .
