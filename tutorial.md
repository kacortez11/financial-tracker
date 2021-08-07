# Financial Tracker

python manage.py commands 

migrate 
- syncs settings with our project

startapp <component_name>
- creates folder for component specific stuff (test, models, views, etc)

createsuperuser
- allows to create a super user that has access to admin 
- admin/admin

makemigrations <specific component name>
- creates migration file of your app 
whenever we make changes to models.py 
  makemigrations
  migrate
  
shell
- all django project stuff will work inside shell
Product.objects.all() - select all products table
Product.objects.create(title='', description='')
  
runserver 8000
- start server at port 8000

**Notes**:
* add to admin.py so it will show at admin site:
* admin.site.register(Product)
* to start over, can delete all migrations +dbsqlite during dev/learning
* blank=False on models means required
* on foreign keys' related names, dont include the _id