# app/home/views.py
import datetime
from flask import abort, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required
from ..models import Acronym, Tag, AcroTag
from .. import db

from . forms import AcronymsForm, AcronymSearchForm

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

@home.route('/acronyms', methods=['GET','POST'])
@login_required
def acronyms():
    """
    List all acronyms
    """
    totalcount = Acronym.query.count()

    search = AcronymSearchForm(request.form)
    if request.method == 'POST':
       searchVal = request.form["search"]
       choice = request.form["select"]
       searchStr = "%{}%".format(searchVal)
       if choice == 'acronym':
          acronyms = Acronym.query.filter(Acronym.acronym.like(searchStr))
       elif choice == 'definition':
          acronyms = Acronym.query.filter(Acronym.definition.like(searchStr))
       else:
          #Need to find all tag ids that match the search term,
          tags = Tag.query.filter(Tag.tag.like(searchStr))
          taglist = []
          for tag in tags:
              taglist.append(tag.id) 
          # then find all acroIDs in acrotag
          acrotags = AcroTag.query.filter(AcroTag.tagID.in_(taglist))
          acrolist = []
          for acrotag in acrotags:
              acrolist.append(acrotag.acroID)
          # then find all acronyms that have acroid in the acroID list
          acronyms = Acronym.query.filter(Acronym.id.in_(acrolist))
       subcount = acronyms.count()
       acronyms = acronyms.order_by(Acronym.acronym)
    else:
       acronyms = Acronym.query.order_by(Acronym.acronym).all()
       subcount = len(acronyms) 
    tags = Tag.query.all() 
    return render_template('home/acronyms/acronyms.html',
                           acronyms=acronyms,
                           tags=tags,
                           totalcount=totalcount,
                           subcount=subcount,
                           title='Acronyms',
                           form=search) 

@home.route('/acronyms/add', methods=['GET', 'POST'])
@login_required
def add_acronym():
    """
    Add a acronym to the database
    """

    add_acronym = True

    form = AcronymsForm()

    if form.validate_on_submit():
        if form.submit.data:
            acronym = Acronym(acronym=form.acronym.data, 
                          definition=form.definition.data,
                          author_id=current_user.id,
                          dateCreate=datetime.datetime.now())
            db.session.add(acronym)
            db.session.commit()
            flash('You have successfully added a new Acronym \'' + form.acronym.data + '\'')
        else: 
            flash('You have cancelled the add of a new Acronym')
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
        if form.submit.data:
           acronym.acronym = form.acronym.data
           acronym.definition = form.definition.data
           db.session.commit()
           flash('You have successfully edited the acronym \'' + acronym.acronym + '\'')
        else:
           flash('You have Cancelled the edit of acronym \'' + acronym.acronym + '\'')

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
