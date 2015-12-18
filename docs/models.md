##User

```
id
name
email
password
role
start_date
end_date
pto_hours
per_year
active
```

##Team

```
id
manager_id (user_id)
name
```

##Requests

```
id
type
user_id
start_date
end_date
hours
status
```

##Request Status

```
id
state = <requested, approved, rejected>
note
date
```

##Settings

```
yearly_rollover
sick_is_pto
```