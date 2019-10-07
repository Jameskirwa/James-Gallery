# Photo-Gallery

## Description

This a website that allows a user to see photos in different categories.

## Created by James Kirwa 6/10/2019

## BDD

| Behaviour         | Input            | Output                     |
| ----------------- | ---------------- | -------------------------- |
| serch by category | category         | images under that category |
| serch by location | location         | images under that category |
| Copy Image link   | click bitton     | link copied                |

## Setup and installations

## Prerequisites

1. [Python3.6](https://www.python.org/downloads/)

2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Django

## Clone the Repo and rename it to suit your needs

## Initialize git and add the remote repository

bash
git init

## Create and activate the virtual environment

bash
python3.6 -m virtualenv virtual

bash
source virtual/bin/activate

## Setting up environment variables

Create a `.env` file and paste paste the following filling where appropriate:

DEBUG=True #set to false in production
DB_NAME='gallery'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1

## Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

## Run chmod a+x start.py

   bash
   chmod a+x start.py

## Run the app

   bash
  ./start.sh

## Access the application through localhost:5000

Open [localhost:5000](http://127.0.0.1:5000/)

## Contributing

Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs

Create an issue mentioning the bug you have found

## Known bugs

- N/A

## Support and contact details

Contact [James Kirwa](jameskirwa34@gmail.com) for further help/support

## License

[MIT](https://github.com/Jameskirwa/MyGallery/blob/master/license)
