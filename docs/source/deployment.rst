.. index:: deployment


**********
Deployment
**********


.. index::
    double: deployment; Openshift deployment

Auto-deployment on Openshift 3
==============================

In order to enable auto-deployment for the project, you need to have a `OpenShift Online` account.

If you don't have one yet, you can create one on the following `link <https://console.preview.openshift.com/console/>`_.

OpenShift web console
---------------------

.. index::
    double: deployment; Openshift console


Once on the OpenShift console, follow the next steps to setup a new project:
    - Choose **Python** language on the catalog and select **Python 3.5** model.
    - Fill **name**, **Git URL** fields and proceed with the creation.



After creating the project, you will need to take note of the following info for the deploy: **GitHub Webhook URL**
and **GitHub secret**.

For the **GitHub Webhook URL**, go to builds and open the one on the list. Then go to configuration tab, and the
GitHub Webhook URL field will be on the right.

The **GitHub secret** can be found on the build config file. To open it, click over **action** dropdown placed on the
top right corner of the console, and select **Edit YAML**.

Inside the build config editor, search the fragment that points to the repository and make sure that **ref** param points
to the branch that will be auto deployed.

.. code-block:: bash

  source:
    type: Git
    git:
      uri: 'https://github.com/Soundphy/soundphy'
      ref: master

Next, search for the *spec / triggers* fragment where the **GitHub secret** is placed, and grab the token.

.. code-block:: bash

  spec:
    triggers:
    - type: Generic
      generic:
        secret: 00000000000
    - type: GitHub
      github:
        secret: 00000000000

GitHub webhook configuration
----------------------------

.. index::
    double: deployment; GitHub webhook


Now it's time to setup the webhook that triggers the autodeployment. With the project opened on GitHub, go to
webhook screen via *settings / webhook / Add webhook*. In there:

 - Fill the Payload URL field with the **GitHub Webhook URL** taken from Openshift console.
 - Choose **application/json** as content type.
 - Fill the secret field with the **GitHub secret** token.

Depending on your needs you could adjust more or less the events that triggers the webhook, in this case *push* event
is enough.

Once you create the webhook, it will be deployed by the first time automatically, so be sure that was successfully
delivered before closing the tab.
