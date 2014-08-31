#!/bin/bash
sudo apt-get install python-pip
sudo pip install oauth2
cd gitrepo/datasci_course_materials/

#sqlite3
sudo apt-get install sqlite3

#r
#http://cran.r-project.org/bin/linux/ubuntu/README
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
sudo vi /etc/apt/sources.list
et ajout deb http://cran.univ-paris1.fr/bin/linux/ubuntu precise/

sudo apt-get update
sudo apt-get install r-base

#issue with RccpEigen compilation - hangs on oor right after fastLm.cpp 
#halt and retry

$ R
q()

#modifier la config pour mettre 2G (sinon RccpEigen ne compile pas)

Thanks to X forwarding we can forward the output of graphical programs using X11 to our host machine.

Note: if you're on OSX, you need to install XQuartz first.
config.ssh.forward_x11 = true
