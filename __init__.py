from flask import Flask
from flask_uploads import UploadSet, configure_uploads, DEFAULTS, send_from_directory
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='dev')

app.config['UPLOADED_FILES_DEST'] = 'uploads'
os.makedirs('uploads', exist_ok=True)
files = UploadSet('files', DEFAULTS + ('pdf',))
configure_uploads(app, files)

@app.route('/uploads/<filename>')
def uploads(filename):
    print('hello')
    return send_from_directory(app.config['UPLOADED_FILES_DEST'], filename)

from . import db
db.init_app(app)

from . import home
app.register_blueprint(home.bp)

from . import auth
app.register_blueprint(auth.bp)

from . import forum
app.register_blueprint(forum.bp)

app.add_url_rule('/', endpoint='home.index')

def store_file(file):
    return files.save(file)
