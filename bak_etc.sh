cp /etc ./root/etc -r
_IP=$(hostname) || true
cp /etc ./root/$_IP/etc -r
#tar -zcvf $_IP.tar.gz /etc
git add *
git commit -m "regular backup"
git push origin master