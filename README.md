# PTO Tracker

The server component of `pto-tracker`. See the client code here: https://github.com/scarow/pto-tracker-client

### Dependencies

* node.js
* postgresql

### Run locally

We've setup a vagrant repo to help get this running locally. We are assuming you have [vagrant](https://www.vagrantup.com/) installed and set up.

* Clone the repo: `git clone https://github.com/scarow/pto-tracker.git`
* `cd pto-tracker`
* `npm install`

In the same parent directory: 

* Clone the vagrant repo: `git clone https://github.com/h0ke/vagrant-nodejs-dev.git`
* `vagrant up`
* `vagrant ssh`
* `cd /srv/pto-tracker`
* `./node_modules/.bin/db-migrate up 20160107032133-create_tables`
* `npm start`
* point your browser to `192.168.50.3:3000`