"""The app module, containing the app factory function."""
from flask import Flask
from run4it.app.extensions import jwt, db, migrate
from run4it.api.user.model import User


def create_app(config_object, app_name):
    app = Flask(app_name)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)

    register_extensions(app)
    register_shell_context(app)

    return app

def register_extensions(app):
    """Register Flask extensions"""
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

def register_shell_context(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': User
        }

    app.shell_context_processor(shell_context)