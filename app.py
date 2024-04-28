from flask import (
    Flask, request, render_template, 
    redirect, url_for, jsonify)

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/details')
def detail():
    portfolio = request.args.get('portfolio_give', '')
    return render_template('details.html', portfolio=portfolio)
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)