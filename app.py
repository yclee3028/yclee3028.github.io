from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    month = datetime.now().month
    season = 'Winter' if month in [12, 1, 2] else 'Spring' if month in [3, 4, 5] else \
             'Summer' if month in [6, 7, 8] else 'Fall'
    return render_template('index.html', season=season)

if __name__ == '__main__':
    app.run(debug=True)