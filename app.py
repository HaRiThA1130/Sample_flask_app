from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for users
users = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/contact')
def contact():  
    return "Contact page is under construction."

@app.route('/shop')
def shop():
    return "Shop page is under construction."

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        # Simple authentication check
        for user in users:
            if user['username'] == uname and user['password'] == pwd:
                return redirect(url_for('home'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        users.append({'username': uname, 'password': pwd})
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
