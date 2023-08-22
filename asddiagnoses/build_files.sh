echo " BUILD START"
source bin/activate
python3.10 -m pip3 install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear
echo " BUILD END"
