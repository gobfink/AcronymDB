# app/home/views.py
import datetime
from wtforms import BooleanField 
from flask import abort, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required
from ..models import Acronym, Tag, AcroTag
from .. import db

from . forms import AcronymsForm, AcronymSearchForm, AddTagForm

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
       sorter = request.args.get('sort')
       if (sorter == 'definition'):
           acronyms = Acronym.query.order_by(Acronym.definition).all()
       elif (sorter == 'acronym'):
           acronyms = Acronym.query.order_by(Acronym.acronym).all()
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

    """
    Create dynamic objects on the form
      - Query the tag database
      - Turn into actual string values
      - DIsplay in the form
    """
    tags=[]
    tag_query=Tag.query.all();
    for tag in tag_query:
      setattr(AcronymsForm, tag.tag, BooleanField(tag.tag))

    form = AcronymsForm()

    #if request.method == 'GET':
    #    cmd = request.args.get('cmd')
    #    tagid = request.args.get('tagid')
    #    if (cmd == 'deltag'):
    #       acrotag = AcroTag.query.get_or_404(tagid)
    #       tagName = Tag.query.get_or_404(acrotag.tagID).tag
    #       db.session.delete(acrotag)
    #       db.session.commit()
    #       flash('Removing Tag \''+tagName+'\' from acronym \'' + acrotag.acronym.acronym + '\'')
    #    if (cmd == 'addtag'):
           # add code here to handle the add tag, show a pop up window to get the tag, capture the one selected and add
           # the new tag to the AcroTag table.
        #   flash('Adding Tag')

    if form.submit.data:
       if form.validate_on_submit():
            acronym = Acronym(acronym=form.acronym.data, 
                          definition=form.definition.data,
                          author_id=current_user.id,
                          dateCreate=datetime.datetime.now())
            db.session.add(acronym)
            db.session.commit()
            flash('You have successfully added a new Acronym \'' + form.acronym.data + '\'')
            return redirect(url_for('home.acronyms'))
       else:
            flash('Fill in required fields!')
    if form.cancel.data:
        flash('You have cancelled the add of a new Acronym')
        return redirect(url_for('home.acronyms'))

    # load acronym template
    return render_template('home/acronyms/acronym.html', action="Add",
                           add_acronym=add_acronym, form=form,
                           title="Add Acronym")

@home.route('/acronyms/addtag/<int:acroid>', methods=['GET', 'POST'])
@login_required
def add_tag(acroid):
    """
    Add a tag to an acronym
    """
    acronym = Acronym.query.get_or_404(acroid)
    form = AddTagForm(obj=acronym)
    if request.method=='POST':
        if form.submit.data:
           # add code to add to acrotag table
           acrotag = AcroTag(acroID=acroid, 
                          tagID=form.select.data)
           db.session.add(acrotag)
           db.session.commit()
           tag = Tag.query.get_or_404(form.select.data)
           tagname = tag.tag
           flash('You have successfully associated Tag \'' + tagname + '\' to acronym \'' + acronym.acronym + '\'')
        else:
           flash('You have cancelled the association a Tag')

        return redirect(url_for('home.edit_acronym',id=acroid))

    # get the tags that I don't already have for this acronym
    #mychoices = [(1,'Test 1'),(4, 'Test 4')] 
    mychoices = Tag.query.all()
    assoc=[]
    myselect = []
    
    for acrotag in acronym.acrotags:
      assoc.append(int(acrotag.tagID))
    #flash('assoc:'+str(assoc))
    for choice in mychoices:
        if int(choice.id) not in (assoc):
          myselect.append((choice.id, choice.tag))
    form.select.choices=myselect
    # load acronym template
    return render_template('home/acronyms/addtag.html', 
                           form=form,
                           title="Add Tag")

@home.route('/acronyms/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_acronym(id):
    """
    Edit a acronym
    """
    add_acronym = False

    acronym = Acronym.query.get_or_404(id)
    form = AcronymsForm(obj=acronym)
    if request.method == 'GET':
        cmd = request.args.get('cmd')
        acrotagid = request.args.get('acrotagid')
        if (cmd == 'deltag'):
           acrotag = AcroTag.query.get_or_404(acrotagid)
           tagName = Tag.query.get_or_404(acrotag.tagID).tag
           db.session.delete(acrotag)
           db.session.commit()
           flash('Removing Tag \''+tagName+'\' from acronym \'' + acrotag.acronym.acronym + '\'')
        if (cmd == 'addtag'):
           return redirect(url_for('home.add_tag',acroid=id))
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
