all:$(PROJ_ROOT)/data/multivariate_cnn/training_data

	@python $(PROJ_ROOT)/src/main/model/multivariate_cnn/multivariate_cnn.py \
		$(PROJ_ROOT)/pipeline_config/multivariate_cnn/hyperparam.ini \
		$(PROJ_ROOT)/data/multivariate_cnn/training_data \
		$(PROJ_ROOT)/model/multivariate_cnn \
		$(PROJ_ROOT)/report/multivariate_cnn

$(PROJ_ROOT)/data/multivariate_cnn/training_data: \
	$(PROJ_ROOT)/src/main/data/training_data.py \
	$(PROJ_ROOT)/pipeline_config/multivariate_cnn/training_data.ini \
	$(PROJ_ROOT)/data/multivariate_cnn/aggregate_data

	@python $(PROJ_ROOT)/src/main/data/training_data.py \
		$(PROJ_ROOT)/pipeline_config/multivariate_cnn/training_data.ini \
		$(PROJ_ROOT)/data/multivariate_cnn/aggregate_data \
		$(PROJ_ROOT)/data/multivariate_cnn

$(PROJ_ROOT)/data/multivariate_cnn/aggregate_data: \
	$(PROJ_ROOT)/src/main/data/aggregate_data.py \
	$(PROJ_ROOT)/pipeline_config/multivariate_cnn/aggregate_data.ini \
	$(PROJ_ROOT)/data/multivariate_cnn/raw_data

	@python $(PROJ_ROOT)/src/main/data/aggregate_data.py \
		$(PROJ_ROOT)/pipeline_config/multivariate_cnn/aggregate_data.ini \
		$(PROJ_ROOT)/data/multivariate_cnn/raw_data \
		$(PROJ_ROOT)/data/multivariate_cnn

$(PROJ_ROOT)/data/multivariate_cnn/raw_data: \
	$(PROJ_ROOT)/src/main/data/raw_data.py \
	$(PROJ_ROOT)/pipeline_config/multivariate_cnn/raw_data.ini

	@python $(PROJ_ROOT)/src/main/data/raw_data.py \
		$(PROJ_ROOT)/pipeline_config/multivariate_cnn/raw_data.ini \
		$(PROJ_ROOT)/data/multivariate_cnn

clean:
	@echo do multivariate_cnn cleaning...................
	@rm -r $(PROJ_ROOT)/data/multivariate_cnn \
		$(PROJ_ROOT)/model/multivariate_cnn \
		$(PROJ_ROOT)/report/multivariate_cnn