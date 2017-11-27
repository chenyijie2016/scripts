curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-3.4.10.tgz
tar -zxvf mongodb-linux-x86_64-ubuntu1604-3.4.10.tgz
mv  mongodb-linux-x86_64-ubuntu1604-3.4.10/ /usr/local/mongodb
echo 'export PATH=/usr/local/mongodb/bin:$PATH' >> ~/.bashrc
mkdir -p /data/db
# test
mongod