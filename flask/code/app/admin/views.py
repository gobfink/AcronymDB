# app/admin/views.py
from sqlalchemy import func
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .. import db
from ..models import Tag

from . forms import TagsForm


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if current_user.userIsAdmin != 1:
        abort(403)


# Tag Views


@admin.route('/tags', methods=['GET', 'POST'])
@login_required
def list_tags():
    """
    List all tags
    """
    check_admin()

    tags = Tag.query.all()

    return render_template('admin/tags/tags.html',
                           tags=tags, title="Tags")


@admin.route('/tags/add', methods=['GET', 'POST'])
@login_required
def add_tag():
    """
    Add a tag to the database
    """
    check_admin()

    add_tag = True

    form = TagsForm()

    if form.validate_on_submit():
        tag = Tag(tag=form.tag.data)
        #tag = Tag(form.tag.data)
        #tag = new Tag
        #tag.tag = form.tag.data
        #exist_count = db.session.execute(func.count(Tag.id).scalar())
        #if exist_count <= 0 :
            # add tag to the database
        db.session.add(tag)
        db.session.commit()
        flash('You have successfully added a new tag ' + form.tag.data + ' !')
        #else:
            # in case tag name already exists
        #    flash('Error: tag '+ form.tag.data + ' already exists.')

        # redirect to tag page
        return redirect(url_for('admin.list_tags'))

    # load tag template
    return render_template('admin/tags/tag.html', action="Add",
                           add_tag=add_tag, form=form,
                           title="Add Tag")


@admin.route('/tags/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_tag(id):
    """
    Edit a tag
    """
    check_admin()

    add_tag = False

    tag = Tag.query.get_or_404(id)
    form = TagsForm(obj=tag)
    if form.validate_on_submit():
        tag.tag = form.tag.data
        db.session.commit()
        flash('You have successfully edited the tag.')

        # redirect to the tag page
        return redirect(url_for('admin.list_tags'))

    form.tag.data = tag.tag
    return render_template('admin/tags/tag.html', action="Edit",
                           add_tag=add_tag, form=form,
                           tag=tag, title="Edit Tag")


@admin.route('/tags/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_tag(id):
    """
    Delete a tag from the database
    """
    check_admin()

    tag = Tag.query.get_or_404(id)
    db.session.delete(tag)
    db.session.commit()
    flash('You have successfully deleted the tag.')

    # redirect to the tags page
    return redirect(url_for('admin.list_tags'))

    return render_template(title="Delete Tag")
