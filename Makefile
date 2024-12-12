all: help

.PHONY: help clean swagger_json


help:
	@echo "help - show this help"
	@echo "clean - remove artifacts"
	@echo "doc - genegate api specification"

clean:
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +

generate:
	@if [ -z "${SWAGGER_JSON_PATH}" ]; then\
		echo "SWAGGER_JSON_PATH environment variable is not set";\
	else\
		java -jar /usr/share/java/swagger-codegen-cli-2.4.28.jar generate -i ${SWAGGER_JSON_PATH} -l python -c codegen-config.json -o tmp &&\
		rm -rf tasksdjclient && cp -R tmp/tasksdjclient . &&\
		mkdir -p docs/generated_docs && rm -rf docs/generated_docs/docs && cp -R tmp/docs docs/generated_docs && cp -f tmp/README.md docs/generated_docs &&\
		mkdir -p test && cp -R -n tmp/test/* test &&\
        rm -rf tmp;\
	fi
