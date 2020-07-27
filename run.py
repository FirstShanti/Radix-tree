import os
from flask import Flask, render_template
from api import main
from config import * 


app = Flask(__name__)
app.config.from_object(Configuration)


app.register_blueprint(main, url_prefix='/')

@app.route('/')
def index():
	# if node.children:
	# 	with open('db.pickle', 'wb') as f:
	# 		pickle.dump(node, f)
	return render_template('index.html')

@app.errorhandler(404)
def error_404(page):
	return render_template('error404.html')
# db = SQLAlchemy(app)

# # migrate data to sql
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand) 
if __name__ == '__main__':
    app.run(host='0.0.0.0')