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
12. add registation form, add comments form, add posts form
13. add show page for posts, add show page for users


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

add verify user exists before allow access to create post
maybe add profile for authors
make all the links
fix the post creation form(adjust content size and fix 'name to say title')
add link from username to show page
decide whether i want post names to be unique or to
could add wrappers
make webpages inaccessible

 <span class="help-block">A longer block of help text that breaks onto a new line and may extend beyond one line.</span>