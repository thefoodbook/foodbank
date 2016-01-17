set -e
python /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/virtualenv.py venv/
source ./venv/bin/activate
pip freeze | grep -v -f requirements.txt - | grep -v '^#' | xargs pip uninstall -y
pip install -r requirements.txt
source ./bin/localenv.sh
python $@

