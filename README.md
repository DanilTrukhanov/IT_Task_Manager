# Disclaimer
Please note that this project may contain bugs and is not yet fully completed. It is a work in progress :)

# Deploy
- You can test this project by going to https://trukhanovit-task-manager.onrender.com
- You can use following credentials:
  - Login: `admin.trukhanov`
  - Password: `Danil$2002$boss.`


# IT_Task_Manager
IT company task manager where you can create tasks with deadline, mark them as complete.
- Tasks are ordered by status(`in progress`, `done`), by priority(from `Urgent` to `Low`) and by deadline.
- You can create new tasks, update the existing tasks, delete them.
- Tasks also have types, which is set while creation. You can create new task types.
- Tasks have to be assigned to workers.
- New workers can be created by only authenticated users.
- Each worker have a position that is set while creation worker. You can also create new positions.



- Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata django_fixtures.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.trukhanov`
  - Password: `Danil$2002$boss.`
