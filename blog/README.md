This app was build using Flask
    Explin why i build it using flask


process so far
1. configure empty flask shell
2. connect SQL alchemy with SQLITE database
3. implement rudimentary authentication using werkzeug
4. working on getting forms to working
5. app getting unwieldy, trying to restructure into seperate files
6. added read me
7. got WTF Forms to work and authentication working, going to upload to github for first time
8. adding bootstrap
9. going to add nav bar
10. adding validations for login
11. add flash


Databse info -
 User named Robin, password = password
 have to create table running
 >>> from yourapplication import db
>>> db.create_all()
to get the user
>>> from blog import models
>>> from blog.models import User

User.query.get(1)
User.query.get(1).check_password('password')
User.query.filter_by(username='Robin').first().check_password('password')

Things to do-
apply unique filter to username
change title of website on tab
figure out actual name of website
add verify user exists before allow access to create post
maybe add profile for authors

 <span class="help-block">A longer block of help text that breaks onto a new line and may extend beyond one line.</span>