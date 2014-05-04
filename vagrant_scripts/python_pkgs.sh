# MongoDB
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' \
    > /etc/apt/sources.list.d/mongodb.list


apt-get update
# apt-get install -y libatlas-base-dev gfortran

apt-get install -y python-numpy python-scipy \
    python-lxml python-numexpr python-openpyxl \
    python-pandas python-matplotlib python-sklearn \
    ipython ipython-notebook ipython-doc ipython-notebook-common \
    python-nltk python-opencv \
    mongodb-org python-pymongo python-pymongo-ext

# TODO: jieba gensim
