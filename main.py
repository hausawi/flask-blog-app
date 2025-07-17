from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from posts import Data


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cac7e326c021997ff92f1c829f57943d'


posts = [
    {
        '_id': '01',
        'author': 'Haider',
        'title':'    بعض الجوانب الثقافية والتقليدية لشعوب الهوسا، التي تعكس ثراء وتنوع ثقافتهم في الفنون والترفيه.',
        'category':'Economy',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createAt':'12/7/2025',
        'img':'/static/hausa2.png'
    },
    {
        '_id': '02',
        'author': 'Haider',
        'title':'التطور الديني للشعب، بما في ذلك الأديان التقليدية والتحولات الدينية',
        'category':'Economy',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createAt':'12/7/2025',
        'img':'/static/hausa3.jpg'
    },

    {
        '_id': '03',
        'author': 'Haider',
        'title':'الاقتصاد والتجارة والنشاط الاقتصادي للشعب، بما في ذلك الزراعة، والتجارة، والصناعة.',
        'category':'Economy',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'createAt':'12/7/2025',
        'img':'/static/hausa4.jpg'
    },
    {
        '_id': '04',
        'author': 'Haider',
        'title':'الأصول والتاريخ المبكر و الأساطير والروايات الشفوية',
        'category':'Economy',
        'content':'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for "lorem ipsum" will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
        'date':'12/7/2025',
        'img':'/static/hausa1.jpg'
    },
    
]

@app.route("/")
def home():
    return render_template('home.html', posts=Data, title='Home')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/alert")
def alert():
    return render_template('alert.html')

if __name__ == '__main__':
    app.run(debug=True)