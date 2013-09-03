cp /etc ./root/etc -r
_HOSTNAME=$(hostname) || true
#cp /etc ./root/$_IP/etc -r
#tar -zcvf $_HOSTNAME.tar.gz /etc
git add *
git commit -m " : regular backup"
git push origin master
