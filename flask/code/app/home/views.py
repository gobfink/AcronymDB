# app/home/views.py
import datetime
from flask import abort, render_template, redirect, flash, url_for
from flask_login import current_user, login_required
from ..models import Acronym, Tag
from .. import db

from . forms import AcronymsForm

from . import home

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if current_user.userIsAdmin != 1:
        abort(403)

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """

    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
 
    return render_template('home/dashboard.html',title="Dashboard")

@home.route('/acronyms')
@login_required
def acronyms():
    """
    List all acronyms
    """
    tags = Tag.query.all() 
    acronyms = Acronym.query.all()
    return render_template('home/acronyms/acronyms.html',
                           acronyms=acronyms,tags=tags,title="Acronyms") 

@home.route('/acronyms/add', methods=['GET', 'POST'])
@login_required
def add_acronym():
    """
    Add a acronym to the database
    """

    add_acronym = True

    form = AcronymsForm()

    if form.validate_on_submit():
        acronym = Acronym(acronym=form.acronym.data, 
                          definition=form.definition.data,
                          authID=current_user.id,
                          dateCreate=datetime.datetime.now())
        db.session.add(acronym)
        db.session.commit()
        flash('You have successfully added a new Acronym ' + form.acronym.data + ' !')
        return redirect(url_for('home.acronyms'))

    # load acronym template
    return render_template('home/acronyms/acronym.html', action="Add",
                           add_acronym=add_acronym, form=form,
                           title="Add Acronym")

@home.route('/acronyms/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_acronym(id):
    """
    Edit a acronym
    """
    add_acronym = False

    acronym = Acronym.query.get_or_404(id)
    form = AcronymsForm(obj=acronym)
    if form.validate_on_submit():
        acronym.acronym = form.acronym.data
        acronym.definition = form.definition.data
        db.session.commit()
        flash('You have successfully edited the acronym.')

        # redirect to the acronym page
        return redirect(url_for('home.acronyms'))

    form.acronym.data = acronym.acronym
    return render_template('home/acronyms/acronym.html', action="Edit",
                           add_acronym=add_acronym, form=form,
                           acronym=acronym, title="Edit Tag")


@home.route('/acronyms/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_acronym(id):
    """
    Delete a acronym from the database
    """
    check_admin()

    acronym = Acronym.query.get_or_404(id)
    db.session.delete(acronym)
    db.session.commit()
    flash('You have successfully deleted the acronym.')

    # redirect to the acronyms page
    return redirect(url_for('home.acronyms'))

    return render_template(title="Delete Acronym")

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.userIsAdmin == 0:
       abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
