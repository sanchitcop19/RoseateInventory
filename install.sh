/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
brew install python
which python
which python3
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
which pip3
which pip
pip install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
which python
which python3
which pip3
pip install -r requirements.txt
