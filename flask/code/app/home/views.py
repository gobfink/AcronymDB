# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required
from ..models import Acronym

from . import home

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
  
    acronyms = Acronym.query.all()
    return render_template('home/acronyms/acronyms.html',
                           acronyms=acronyms, title="Acronyms") 

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.userIsAdmin == 0:
       abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
