from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///128chan.db'
db = SQLAlchemy(app)

class ChanPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Board = db.Column(db.String(3), nullable=False)
    image_file = db.Column(db.String(30), unique=True, nullable=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Anonymous')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)

class Chanreply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer, nullable=False)
    Board = db.Column(db.String(3), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Anonymous')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return str(self.id)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pol', methods=['GET', 'POST'])
def pol():
            all_posts = ChanPost.query.order_by(ChanPost.date_posted).all()
            all_replies = Chanreply.query.order_by(Chanreply.date_posted).all()
            if request.method == 'POST':
                post_title = request.form['title']
                post_content = request.form['content']
                post_author = request.form['author']
                post_id = request.form['chan_val']
                Board_id = request.form['Board_id']
                print(post_id)
                new_post = Chanreply(Board=Board_id, postid=post_id, title=post_title, content=post_content, author=post_author)
                db.session.add(new_post)
                db.session.commit()
                return redirect('/pol')
            else:
                    return render_template('pol.html', chan=all_posts, chanreply=all_replies)
                    print(chan.file_name)


@app.route('/tec', methods=['GET', 'POST'])
def tec():
            all_posts = ChanPost.query.order_by(ChanPost.date_posted).all()
            all_replies = Chanreply.query.order_by(Chanreply.date_posted).all()
            if request.method == 'POST':
                post_title = request.form['title']
                post_content = request.form['content']
                post_author = request.form['author']
                post_id = request.form['chan_val']
                Board_id = request.form['Board_id']
                print(post_id)
                new_post = Chanreply(Board=Board_id, postid=post_id, title=post_title, content=post_content, author=post_author)
                db.session.add(new_post)
                db.session.commit()
                return redirect('/tec')
            else:
                    return render_template('tec.html', chan=all_posts, chanreply=all_replies)
                    print(chan.file_name)

@app.route('/ran', methods=['GET', 'POST'])
def ran():
            all_posts = ChanPost.query.order_by(ChanPost.date_posted).all()
            all_replies = Chanreply.query.order_by(Chanreply.date_posted).all()
            if request.method == 'POST':
                post_title = request.form['title']
                post_content = request.form['content']
                post_author = request.form['author']
                post_id = request.form['chan_val']
                Board_id = request.form['Board_id']
                print(post_id)
                new_post = Chanreply(Board=Board_id, postid=post_id, title=post_title, content=post_content, author=post_author)
                db.session.add(new_post)
                db.session.commit()
                return redirect('/ran')
            else:
                    return render_template('ran.html', chan=all_posts, chanreply=all_replies)
                    print(chan.file_name)

@app.route('/mkr', methods=['GET', 'POST'])
def mkr():
            all_posts = ChanPost.query.order_by(ChanPost.date_posted).all()
            all_replies = Chanreply.query.order_by(Chanreply.date_posted).all()
            if request.method == 'POST':
                post_title = request.form['title']
                post_content = request.form['content']
                post_author = request.form['author']
                post_id = request.form['chan_val']
                Board_id = request.form['Board_id']
                print(post_id)
                new_post = Chanreply(Board=Board_id, postid=post_id, title=post_title, content=post_content, author=post_author)
                db.session.add(new_post)
                db.session.commit()
                return redirect('/mkr')
            else:
                    return render_template('mkr.html', chan=all_posts, chanreply=all_replies)
                    print(chan.file_name)










app.config["IMAGE_UPLOADS"] = (r"C:\Users\Admin\Desktop\128chan\static\img\uploads")
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG"]


def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False




@app.route('/upload', methods=['GET', 'POST'])
def Upload_image():
    if request.method == "POST":


        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("needs a name")
                return redirect(request.url)
            if not allowed_image(image.filename):
                print("extension not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            post_filename = filename
            post_board = request.form['Board']
            post_title = request.form['title']
            post_content = request.form['content']
            post_author = request.form['author']
            new_post = ChanPost(image_file=post_filename, Board=post_board, title=post_title, content=post_content, author=post_author)
            db.session.add(new_post)
            db.session.commit()
            print("saved")
            return redirect('/pol')
    else:
        return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
