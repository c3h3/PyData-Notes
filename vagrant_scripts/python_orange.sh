# echo Install Genome Desktop
# apt-get install -y xorg gnome-core
# a bug in /etc/init.d/gdm line 78
# if [[ ! -f /etc/init.d/gdm.orig ]]; then
#     cp /etc/init.d/gdm /etc/init.d/gdm.orig
#     sed '78d' /etc/init.d/gdm > /etc/init.d/gdm
# fi
# echo You must restart vagrant by \'vagrant reload --provision\`
# echo To make sure GUI is properly installed and configured.

apt-get install -y mercurial python-qwt3d-qt4 python-qt4
hg clone https://bitbucket.org/biolab/orange /tmp/orange
cd /tmp/orange
python setup.py build
python setup.py install
