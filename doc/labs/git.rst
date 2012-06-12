Lab: Making Your First Commit
=============================

This repository has been used for a number of classes at Rochester Institute of Technology, and is designed to be an easily extensible primer on using git.

This lab assumes you already have a working git environment, as well as a Github account.

Getting the Source
------------------
The source for this documentation is currently found on `Github <http://github.com/FOSSRIT/posse>`_.  Every time a change is `pushed` to this repository, those changes are automatically propagated here.  But we don't have to worry about that just yet.  For now, we want our own copy of the documentation so we can make changes to it.

From the Github page of the project, look for a button labeled `fork` in the upper right of the screen.  If you are logged in, this will create a fork of the project in your own account, where you can make and share changes without worrying about breaking the upstream's code.

.. note:: A *fork* refers to a repository which has been been copied from another repository and has possibly diverged from the original project.  The two branches can be visualized to split, or come to a fork at this point.

Now that you have a fork you can commit changes to, we want to check out a local copy, so that we can actually get to making those changes.  To do this on a UNIX clone (Mac OSX, Linux, etc.), open a terminal and run::

 $ git clone git@github.com:<username>/posse.git

Alternatively, you could use the Github GUI on Windows or OSX to get a copy of the repository.

Now that you have a copy of the source for this documentation, we are going to edit one of the files inside.  Using your favorite text editor, open up the file ``data/students.yaml``

The ``data/students.yaml`` file is a structured data file that keeps track of
all the students in the class and metadata about them.  Using this file and the
bindings in ``lib/posse/model/students.py`` we can build scripts that count
how many lines of code each student modifies each week, or how many
words/blogpost, or whatever we like.

What we are going to do is add our information to the file.  There should already be a few entries in the file, so just copy one of those and add your details.  You don't want to remove any of the ones currently there, but rather add yours.

Once you have done this, save the files, commit your changes, and push, either with a `git commit -a; git push` or through the Github GUI program.

Congratulations!  You've made a change to an open source project, and shared it with the world.  Now we need to notify the project we forked from that we have changes we'd like them to incorporate.  Back on the Github page of your fork of the project, there should be a `Pull Request` button just to the left of where the fork button was that you used to make this fork of the repoitory.  Pressing this button sends you to a screen giving you a chance to summarize the changes you've made and essentially justify why you feel this should be included.  Submitting this opens a pull request to the upstream project, allowing others to discuss the proposed changes.  As this is a trivial change, it is unlikely that much discussion will take place in this case.

Setting up your environment
---------------------------

Before you can do anything with this (build the documentation or run any of the
scripts) you'll need to setup and activate a python `virtualenv
<http://pypi.python.org/pypi/virtualenv>`_.  Run the following at the command
prompt...

On Linux/Mac OS X
+++++++++++++++++

If you don't have virtualenv installed yet, try::

 $ sudo easy_install virtualenv virtualenvwrapper

If you're using a distro like Fedora or Ubuntu, you should try this instead::

 $ sudo yum install python-virtualenv

Once you have virtualenv installed, you should be able to run::

 $ virtualenv --no-site-packages -p python2 sphinxenv
 $ source sphinxenv/bin/activate
 $ git clone git@github.com:YOUR_USERNAME/posse.git
 $ cd posse
 $ python setup.py develop

On Windows
++++++++++

At the windows command prompt::

 $ virtualenv --no-site-packages -p python2 sphinxenv
 $ sphinxenv/Scripts/activate.bat

In msysGit or git-bash::

 $ git clone git@github.com:YOUR_USERNAME/posse.git

Back in the windows command prompt::

 $ cd posse
 $ python setup.py develop


Building the "Documentation"
----------------------------

The "documentation" for the course (the syllabus, all the homework assignments,
notes on the lectures) are all kept in the ``doc/`` directory of this
repository.  The files all end with the extension ``.rst`` which is the file
extension for the `reStructuredText <http://sphinx.pocoo.org/rest.html>`_ markup
language.  They are all furthermore tied together the the `sphinx` framework for
building integrated docs.

You might notice that the syllabus, et. al. is hosted on
http://readthedocs.org/.  The `upstream github repository
<http://github.com/ralphbean/posse>`_ has a hook installed
that automatically triggers a ``git pull`` at http://readthedocs.org from
http://github.com.  Thus, every time we change the docs here, they are
automatically re-built into HTML for us and posted online.  Awesome!

This however means that we should be careful before we push anything to github,
or it will 'go live'.  To be careful, you should rebuild the documentation
locally (on your machine) to check that whatever modifications you made to the
``.rst`` files actually renders into the HTML that you want.

In order to do that, first make sure you have your virtualenv activated.

Being certain of that, in the root directory, simply run::

 $ sphinx-build -b html doc html-output

The html documentation will be generated in ``html-output/``.  Check
``html-output/html/index.html`` to see if it exists.

.. note:: If your machine complains that 'sphinx-build' is a command that could
   not be found, try running "$ python setup.py develop" in the root of the
   posse repository first.  That ``setup.py`` file contains
   information about all *other* open source projects that are *required* for
   this project, and will automatically install them from
   http://pypi.python.org/

Validating the ``data/students.yaml`` file
------------------------------------------


In order to ensure that you don't introduce any unparseable errors into the
file, there is a script in ``lib/posse/model/validate.py`` that reads in the
file and checks each entry.  You should run it after every time you edit
``data/students.yaml``.

In order to run the ``validate.py`` script, make sure you have your
virtualenv activated.

In the root of the cloned source directory, run::

  $ python lib/posse/model/validate.py

The data format (`YAML <http://www.yaml.org/>`_) can be a little prickly though.
It is `whitespace-sensitive`, meaning that how many spaces you put before an
entry on each line has an impact on how the data is interpreted.  It also means
that tabs and spaces are distinctly different in their meaning.  It also means
that editing such a file is easy to mess up.
