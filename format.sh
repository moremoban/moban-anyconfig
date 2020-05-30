isort -y $(find moban_anyconfig -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
black -l 79 moban_anyconfig
black -l 79 tests
