Thu May  2 16:02:52 MST 2024
----------------------------

The theory is is a stock has wild variability, and variability is
independent across stocks, you can reduce overall variability by
holding a large-ish pool of such stocks.  Let's simulate that.

Getting Started
===============

### one-off crap to create an env in git
#? python3 -m venv --prompt "pyenv> " env
#? git init
#? echo 'env' > .gitignore	# the env folder we just created is not in git

### clean start, new machine
git clone repo
pip install -r requirements.txt	# install all needed pkgs

### typical usage pattern
source env/bin/activate	# to start using the environment
pip install <pkg>	# done while inside env
pip freeze > requirements.txt	# top level, above env!
deactivate		# to stop  using the environment

