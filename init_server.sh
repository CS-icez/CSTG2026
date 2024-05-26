export FLASK_APP="/home/icez/college/CSTG2026"
export FLASK_ENV="development"
cp -r $FLASK_APP/resources $FLASK_APP/../uploads
rm -f $FLASK_APP/uploads
ln -s $FLASK_APP/../uploads $FLASK_APP/uploads
python3 -m flask init-db
