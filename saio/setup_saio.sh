# /bin/bash
# Copyright (c) 2010-2012 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#install indepency
sudo apt-get install -y --force-yes python-software-properties
# If you want install swift use deb package,enable it
#sudo add-apt-repository ppa:swift-core/release
sudo apt-get update

sudo apt-get install -y --force-yes curl gcc git-core memcached python-configobj \
	python-coverage python-dev python-nose python-setuptools \
	python-simplejson python-xattr sqlite3 xfsprogs python-webob \
	python-eventlet python-greenlet python-pastedeploy python-netifaces \
	memcached



#Add swift user
sudo useradd -d /home/swift -s /bin/bash -U swift 
sudo password swift
#setup xfs for disk
sudo  apt-get -y --force-yes install vsftpd 

sudo dd if=/dev/zero of=/srv/swift-disk bs=1024 count=0 seek=1000000
sudo mkfs.xfs -f -i size=1024 /srv/swift-disk
echo "/srv/swift-disk /mnt/sdb1 xfs loop,noatime,nodiratime,nobarrier,logbufs=8 0 0" |sudo tee -a /etc/fstab

sudo mkdir -p /mnt/sdb1
sudo mount /mnt/sdb1
sudo mkdir -p /mnt/sdb1/1 /mnt/sdb1/2 /mnt/sdb1/3 /mnt/sdb1/4 /mnt/sdb1/test
sudo chown -R swift:swift /mnt/sdb1/

if ! [ -d /srv ]
then 
    sudo mkdir /srv 
fi

for x in 1 2 3 4 
do
  sudo  ln -s /mnt/sdb1/$x /srv/$X
done

sudo mkdir -p /etc/swift/object-server /etc/swift/container-server /etc/swift/account-server

for x in 1 2 3 4 
do
  if [ ! -d "/srv/$x/node/sdb$x" ];then
    sudo mkdir -p /srv/$x/node/sdb$x
  fi
done

sudo mkdir -p /var/run/swift
sudo  chown -R swift:swift /etc/swift /srv/1/ /srv/2/ /srv/3/ /srv/4/ /var/run/swift

echo -e "mkdir /var/run/swift \\n chown swift:swift /var/run/swift" |sudo tee -a /etc/rc.local  

if [ -e /home/swift/.bashrc ]
then 
   echo -e "export SWIFT_TEST_CONFIG_FILE=/etc/swift/test.conf  \\n export PATH=${PATH}:~/bin" |sudo tee -a /home/swift/.bashrc 
   sudo source ~/.bashrc
fi


#configure swift and related conf
if ! [ -d /etc/swift ]
then
    sudo mkdir /etc/swift
fi
sudo chown swift:swift /etc/swift

# copy conf files 
sudo cp -R conf/* /etc/swift/
sudo cp rsyncd.conf /etc
sudo service rsync restart

#some system need easy_install and pip
sudo apt-get --force-yes -y install python-setuptools
sudo easy_install pip

#Install swift
#git clone https://github.com/openstack/swift.git
sudo chmod -R 755 swift 
cd /home/sandy/swift/swift ; 
sudo pip install -r requirements.txt
sudo python setup.py develop; 
cd -

#Install swiftclient
#git clone https://github.com/openstack/python-swiftclient.git
sudo chmod -R 755 python-swiftclient 
cd python-swiftclient; 
sudo pip install -r requirements.txt
sudo python setup.py install;
cd ..

#make ring and start server
cd bin;
sudo sh remakerings
sudo swift-init main start

echo "Hi, SAIO is Finished......."



