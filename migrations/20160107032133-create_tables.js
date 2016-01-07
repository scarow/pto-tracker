var dbm = global.dbm || require('db-migrate');
var type = dbm.dataType;

exports.up = function (db, callback) {
  db.createTable('teams', {
    id: { type: 'int', primaryKey: true, autoIncrement: true },
    manager_id: 'int',
    name: 'string'
  }, createUsers);

  function createUsers(err) {
    if (err) { callback(err); return; }
    db.createTable('users', {
      id: { type: 'int', primaryKey: true, autoIncrement: true },
      name: 'string',
      email: 'string',
      password: 'string',
      role: 'string',
      start_date: 'date',
      end_date: 'date',
      pto_hours: 'int',
      per_year: 'int',
      active: 'boolean'
    }, createRequests);
  }

  function createRequests(err) {
    if (err) { callback(err); return; }
    db.createTable('requests', {
      id: { type: 'int', primaryKey: true, autoIncrement: true },
      type: 'string',
      user_id: 'int',
      start_date: 'date',
      end_date: 'date',
      hours: 'int',
      status: 'int'
    }, createRequestStatus);
  }

  function createRequestStatus(err) {
    if (err) { callback(err); return; }
    db.createTable('request_status', {
      id: { type: 'int', primaryKey: true, autoIncrement: true },
      state: 'string',
      note: 'text',
      date: 'date'
    }, createSettings);
  }

  function createSettings(err) {
    if (err) { callback(err); return; }
    db.createTable('settings', {
      yearly_rollover: 'boolean',
      sick_is_pto: 'boolean'
    }, callback);
  }
};



exports.down = function(db, callback) {
  callback();
};
