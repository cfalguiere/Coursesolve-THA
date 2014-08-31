#!/bin/bash
mkdir VM
cd VM
git clone https://github.com/uwescience/datasci_course_materials.git
vagrant init precise64
vagrant up 
vagrant ssh 

#TODO commande pour lancer le script d'install et cd /vagrant

#   config.ssh.forward_x11 = true
#   config.vm.provider :virtualbox do |vb|
#     # Don't boot with headless mode
#     #vb.gui = true

     # Use VBoxManage to customize the VM. For example to change memory:
#     vb.customize ["modifyvm", :id, "--memory", "2048"]
#   end
