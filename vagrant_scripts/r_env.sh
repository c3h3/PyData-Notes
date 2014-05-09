apt-get install -y r-recommended
apt-get install -y gdebi-core libapparmor1
wget http://download2.rstudio.org/rstudio-server-0.98.501-amd64.deb
gdebi -n rstudio-server-0.98.501-amd64.deb
