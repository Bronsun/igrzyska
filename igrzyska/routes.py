from flask import render_template, url_for, flash, redirect,request
from igrzyska import app,db
from igrzyska.forms import DudaForm,TrzaskForm
from igrzyska.modules import Duda,Trzask

@app.route("/")
@app.route('/opinie',methods=['GET','POST'])

def opinie():
    return render_template('opinie.html')

@app.route('/trzask',methods=['GET','POST'])
def dodajTrzask():
    form = TrzaskForm()
    message=None
    if form.validate_on_submit():
        trzask = Trzask(answer=form.answer.data)
        db.session.add(trzask)
        db.session.commit()
        message = "Dodano opinię o Rafale Trzaskowskim"
    return render_template('trzask.html',form=form,message=message)

@app.route('/duda', methods=['GET','POST'])
def dodajDuda():
    form = DudaForm()
    message=None
    if form.validate_on_submit():
        duda = Duda(answer=form.answer.data)
        db.session.add(duda)
        db.session.commit()
        message = "Dodano opinię o Andrzeju Dudzie"
    return render_template('duda.html',form=form,message=message)

@app.route('/wynikiduda',methods=['GET','POST'])
def zobaczDuda():
    answers = Duda.query.order_by(Duda.date_posted.desc())
    return render_template('wynikiduda.html',answers=answers)

@app.route('/wynikitrzask',methods=['GET','POST'])
def zobaczTrzask():
    answers = Trzask.query.order_by(Trzask.date_posted.desc())
    return render_template('wynikitrzask.html',answers=answers)