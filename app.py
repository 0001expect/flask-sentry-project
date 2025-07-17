from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://2933fb41e043424a185fbdac0597c7c5@o4509681672454145.ingest.us.sentry.io/4509681901633537",  # Replace with your actual DSN from Sentry
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    debug=True
)

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flask + Sentry"

@app.route('/error')
def trigger_err():
    division_by_zero = 1 / 0
    return str(division_by_zero)

if __name__ == '__main__':
    app.run(debug=True)
