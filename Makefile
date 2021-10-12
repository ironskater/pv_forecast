.PHONY: env clean test

CONDA_ENV_YML := environment.yml
ENV_NAME := $(shell cat $(CONDA_ENV_YML) | grep name: | cut -d":" -f 2 | tr -d ' ')
PROJ_ROOT := $(shell git rev-parse --show-toplevel)
PYTHONPATH := $(PROJ_ROOT)/src/main

env:
ifeq ($(shell conda env list| grep -w $(ENV_NAME)),)
	@echo Start install virtual env: $(ENV_NAME)
	@conda env create -f $(CONDA_ENV_YML) -n $(ENV_NAME)
	@conda env config vars set PYTHONPATH=$(PYTHONPATH) -n $(ENV_NAME)
else
	@read -p "Virtual env[$(ENV_NAME)] is existed. Do you want to update it? [y/n]:" yesno && \
	if [ "y" = $$yesno ]; then \
		conda env update -f $(CONDA_ENV_YML) -n $(ENV_NAME); \
	else \
		echo "Nothing to be updated"; \
	fi
endif
	# @if [ ! -f "dev.env" ]; then echo PYTHONPATH=$(PYTHONPATH) > dev.env;fi
	@echo PYTHONPATH=$(PYTHONPATH) > dev.env;

merge_data:
	@echo merge stage...

clean_data:
	@echo clean stage...

aggregate_data:
	@echo aggregate stage...

train_data:
	@echo train stage...

multivariate_cnn:
	@echo start training...

test:
	@pytest --verbosity=2 --rootdir=$(PROJ_ROOT)/src/test

clean:
	@echo clean...