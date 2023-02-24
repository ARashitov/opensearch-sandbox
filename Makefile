env_configure: env_install_jupyter_extensions env_install_precommit_hooks
	echo "Environment is configured"

env_install_precommit_hooks:
	pre-commit install && pre-commit install --hook-type commit-msg

env_install_jupyter_extensions:
	jupyter contrib nbextension install --sys-prefix \
	&& jupyter nbextension install --user https://rawgithub.com/minrk/ipython_extensions/master/nbextensions/toc.js \
	&& jupyter nbextension enable --py widgetsnbextension \
	&& jupyter nbextension enable codefolding/main \
	&& jupyter nbextension enable spellchecker/main \
	&& jupyter nbextension enable toggle_all_line_numbers/main \
	&& jupyter nbextension enable hinterland/hinterland \
	&& jt -t grade3

run_jupyter:
	jupyter-notebook --ip 0.0.0.0 --no-browser

run_precommit:
	pre-commit run --all-files

kafka_run:
	docker-compose -f docker-compose.yaml up -d

kafka_stop:
	docker-compose -f docker-compose.yaml down

run_producer:
	python3 'src/producer.py'

run_classical_consumer:
	python3 'src/consumer.py'

run_batch_consumer:
	python3 'src/consumer_batch.py'
