# pip3 uninstall -y django_billing &&

# Packing new version
cd package/django_billing/ &&
python3 setup.py sdist &&

#Install new version
pip3 install --user dist/django_billing-0.0.1.tar.gz &&
cd ../../
