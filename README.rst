=============
nblox-contact
=============

----------
Deployment
----------

.. code:: bash

  $ npm install
  $ serverless deploy -v


Tailing the logs:

.. code:: bash

  $ serverless logs -f nxcontact -t


-----------
Development
-----------

.. code:: bash

  $ virtualenv -p python2.7 .virtualenv
  $ source .virtualenv/bin/activate
  $ pip install -U pip
  $ pip install -r requirements-dev.txt


Running the dev server:

.. code:: bash

  $ ./bin/dev-server.sh


Another way of running the dev server:

.. code:: bash

  $ export FLASK_APP=nxcontact
  $ flask run


Testing and things:

.. code:: bash

  $ py.test
  $ tox

