apg-get install -y git

cd /tmp
wget https://github.com/c3h3/PlaYdata/archive/master.zip
unzip master.zip
cd PlaYdata-master/
python setup.py install

cd /tmp
rm master.zip
wget https://github.com/c3h3/PlaYnlp/archive/master.zip
unzip master.zip
cd PlaYnlp-master/
python setup.py install

cd /tmp
rm -rf PlaYdata-master PlaYnlp-master master.zip

su - vagrant
cd ~
git clone https://github.com/c3h3/PlaYnlp-Corpus.git
git clone https://github.com/c3h3/PlaYdata.git
git clone https://github.com/c3h3/PlaYnlp.git
git clone https://github.com/c3h3/PyData-Notes.git
