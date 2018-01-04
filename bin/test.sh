#!/usr/bin/env bash
# vim: filetype=sh:

cd "$(dirname $0)"; cd ..

OUTPUT_DIR=${OUTPUT_DIR:-_testing_output}
MODULE_NAME=dockerutils

if [ -d .venv ]; then
	source .venv/bin/activate
elif [ -e activate ]; then
	source ./activate
fi

mkdir -p $OUTPUT_DIR

export GIT_HASH=`git log --pretty=format:'%h' -n 1`
echo "GIT_HASH: $GIT_HASH" > $OUTPUT_DIR/pytest_output.txt

if [[ $1 != 'nolint' ]] && [[ $1 != 'emacs' ]]; then
	pylint $MODULE_NAME --rcfile=.pylintrc -d C,R | tee $OUTPUT_DIR/pylint_output.txt
fi

#pytest --color=yes tests | tee _testing_output/pytest_output.txt
pytest --color=yes --cov-config coverage.cfg --cov=$MODULE_NAME --cov-fail-under=80 --cov-report term-missing tests | tee _testing_output/pytest_output.txt
exit ${PIPESTATUS[0]}
