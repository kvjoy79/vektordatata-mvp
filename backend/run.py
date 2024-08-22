from app import app
from app.routes.auth import auth_bp
from app.routes.scrapes import scrape_bp
from app.db.mongodb import connect_to_db

app.config.from_object('config')


app.register_blueprint(scrape_bp, url_prefix='/v1/api')
app.register_blueprint(auth_bp, url_prefix='/v1/api/auth')

if __name__ == '__main__':
    connect_to_db()
    app.run(debug=True)

