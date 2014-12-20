Garoa Push
==========

The bridge between the [Garoa Status][garoa-status] API and your smartphone: the easiest way to know when the [Garoa Hacker Club][garoa] is opened or closed - powered by [Pushbullet][pushbullet].

## The development environment

You have to create a test application using [Pushbullet's dashboard][pushbullet-createapp], then add its credentials to your `.env` file.

    # Create an .env file from the template
    cp .env.template .env
    # Edit it as needed
    vim .env

    # Inside a virtualenv
    pip install -r requirements.txt
    python manage.py migrate

    # Launch the three services on different terminals
    python manage.py runserver
    python manage.py rqworker default
    rqscheduler

    # Add the notification task to the scheduler
    python manage.py schedule-task

[garoa]: https://garoa.net.br/
[garoa-status]: http://status.garoa.net.br/
[pushbullet]: https://www.pushbullet.com/
[pushbullet-createapp]: https://www.pushbullet.com/create-client
