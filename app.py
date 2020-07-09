from flask import Flask, render_template
import os
path = 'static'
files = os.listdir(path)
imagefile = []
for f in files:
    imagefile.append(f)

app = Flask(__name__)
@app.route('/verify/<id>')
def verify(id):
    if (id + '.png' in imagefile):
        return render_template("base.html", content=id)
    else:
        return render_template('errorfound.html')


if __name__ == '__main__':
    app.run(debug=True)
