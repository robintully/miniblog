# Miniblog

Miniblog is a microblog platform built with the Python Flask framework. Miniblog emphasizes a lightweight, modular and fast blogging framework. Flask was chosen due to its minimal prerequisites and lightweigt; Miniblog does not carry deadweight.

These pursuits were selcted to ensure that Miniblog could be deployed and adapted to meet a wide variety of needs. Although I am experienced with Rails, building a Rails app would create too much of a monolithic and inflexible app. Although building a Rails blog CMS would be quick and familiar to me, Rails is not the ideal tool for the job. In researching lighter weight and adaptable solutions, Flask appeared to be the best tool for the job. I decided to learn Flask and Python to use them to build a simple CMS platform that is incredibly small in terms of code, but incredibly powerful and modular. In reflecting on the end product, I think this was the right choice and a wonderous learning oppurtunity. 

Miniblog can support multiple users and one administrator. The administrator is always the first user created. Users can create blog posts, and comment on any other blog post. Blogs can be accessed through either the home route, which renders an index of all posted blogs, or by selecting posts from an individual user's show page. Comments are accessed by accessing the show page of an individual post. User's show pages can be found by clicking on a user's names. Security is provided by hashing and salting passwords with Werkzeug, and CSRF protection is enabled through the use of WTForms. Templates are rendered using the Jinja2 engine built into FLask. The database is currently a SQLite databse with the Flask SQLAlchemy ORM.


### Prerequisities

Miniblog possesses the following requirements, these links provide documentation and installation instructions for Miniblog's dependencies.
1. [Python](https://docs.python.org/3/)
2. [Flask](http://flask.pocoo.org/docs/0.11/)
3. [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
4. [Flask-WTF](https://flask-wtf.readthedocs.io/en/v0.9.5/)
5. [Werkzeug](http://werkzeug.pocoo.org/)


## Creation

Miniblog's creation process
1. Cnfigure Flask shell and ensure routes are working
2. Cnnect SQL alchemy with SQLITE database
⋅⋅* This step took a decent amount of time due to the fact that I was learning an entirely new programming language, framework, and ORM at the same time. I am accustomed to SQL-Alchemy, Flask and Python now but it is always interesting how such simple things need to be relearned when switching stacks. Overall, I am immensely pleased to have learned these new technologies.
3. Iplement rudimentary authentication using Werkzeug
⋅⋅* I searched for a while to find a Flask add on that would handle user registration and authentication in the manner I wanted, I didn't find a suitable option so I implemented my own methods; thankfully Werkzeug handled password hasing and salting for me.
4. Implement forms with WTForms
⋅⋅* WTForms was selected due to its ease of use and built in CSRF prevention. It was easy to work with for the most part.
5. Break down app into seperate files to promote flexibility
⋅⋅* Miniblog was becoming too monolithic and hard to follow, it echoing the tendencies of a Rais app that I was trying to avoid. Thankfully this problem was easily solved by breaking up the app into seperate files.
6. Added initial read me to notate what work needs to be done 
7. Integrated WTForms and SQL Alchemy to allow data to be created from forms
8. Added Bootstrap for style
9. Added navigation bar
10. Added validations for login
⋅⋅* Using the built in validation handling of WTForms was easy and properly informs the user of what error is produced in their log in attempt
11. Add flash to display information to users
⋅⋅* Flash messages are an appropriate way to temporarily inform the user of their actions. Theh Flash messages are displayed in the navbar as this seemd like an aesthetically pleasing location.
12. add registation form, add comments form, add posts form
13. add show page for posts, add show page for users
⋅⋅* The minimal displays for Posts and users are intentional, it assists in the aesthetic pursuit of what Miniblog is, a functional and lightweight blogging platforms that eschews frills. Frills could be added by new creators but are not necessary in the stock version.
14. add delete routes and buttons for comments and posts
15. add admnin
⋅⋅* The admin handling is currently determined by providing the first created user with admin functionality. However, this could be easily changed by utilizing the admin boolean attribute of a user and changing the routes and views to examine this attribute. Miniblog originally handled administration by using this attribute and maintains the functionality to do so. Yet it was determined that ease of creating new instances of miniblog would be facilitated if new creators could just deploy the website and then create themselves as a user, giving themself admin status. 
16. added update form and route for posts, post form autofilled with post content
17. restructured website so that session stores user id instead of username and routes are based off of integers rather then strings
⋅⋅* I go back and forth on which way I prefer in handling sesison. Currently miniblog uses id's which assists in clean URLS and redirect that do not have the escaped character problem of strings. However, I admit that it would perhaps be nicer to avoid the problem all together by creating slugs and using sllugs to navigate and redirect users. But slugs would make the user have to either create a slug, or generate a random slug, or have their title converted into a slug, which might negatively impact the UX.
18. refactored and cleaned more of the code, added more explanatory comments
19. load bootstrap from CDN rather then local storage to be lighter

## Deployment

Miniblog can be deployed in numerous ways. Explanatory documentation can be found [here](http://flask.pocoo.org/docs/0.11/deploying/)


## Authors

* **Robin Tully** - [github](https://github.com/robintully)


## License

This project is licensed under the MIT License 

## Acknowledgments

* Thanks to all authors of the utilized frameworks and languages. It was a pleasure working with your products
* Thanks to the Flatiron school for providing an enjoyable location to work in
* Thanks to you for reading this and inspecting this project