from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('run')

manager = Manager(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Welcome baies</h1>"

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context, use_ipython=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
