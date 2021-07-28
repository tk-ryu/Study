from flask import Flask
from flask_app.models import db, migrate

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)



    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite+pysqlite:///test.db"

    db.init_app(app)
    migrate.init_app(app, db)

    from flask_app.routes import main_route
    app.register_blueprint(main_route.bp)
    
    return app

if __name__ =='__main__':
    app = create_app()
    app.run