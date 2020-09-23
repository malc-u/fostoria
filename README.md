# FOSTORIA

[![Build Status](https://travis-ci.com/malc-u/fostoria.svg?branch=master)](https://travis-ci.com/malc-u/fostoria)

Landscape photography of Poland with webshop (selling photo prints). Photographs by Tomasz Zowada - based in Upper Silesia (Poland).


## UX

### Target Audience

- People that like work of the artist
- People that got here via artist's social media
- People that like landscape photography
- People that like Upper Silesian landscape
- People that are looking to purchase landscape photo print

### User Stories

1. As a new user:
 - I want to be able create an account
 - I want to visit gallery of photos available to purchase photos
 - I want to find out what print sizes are available to purchase
2. As a returning/registered user:
 - I want to be able to login into my account
 - I want to be able to see my profile
 - I want to be able to see my previous purchases
 - I want to have possibility of changing my profile details
3. As a purchasing user:
 - I want to add chosen product to my cart/basket
 - I want to view products currently added to my cart/basket
 - I want to have possibility of changing quantity of products in the cart/basket
 - I want to remove items from my cart/basket when i changed my mind
 - I want to see total value of my cart/basket
 - I want to be able to enter address I want my purchase dispatched to
 - I want to be able to pay for my purchase
4. As a browsing/visiting user:
 - I want simple, not too complicated page to use
 - I want to use my page on my phone or tablet as well as my desktop
 - I want to be able to see all products in 1 gallery
 - I want to have possibility of searching gallery
 - I want to click on the picture in the gallery and be presented with info about it
 - I want to see photos grouped into categories
 - I want to find frequently asked questions 
 - I want easy way of contacting page owner - via contact form

### Design choices

The color scheme that was chosen is a light theme that would not be overwhelming and will nicely present photos.
There are only couple subtle colors to contemplate main content and distinguish items on the page. However first and foremost the intention was to emphasize the work of the artist and not web design. Page was designed in such way to be light, plain and simple thus showcasing landscapes captured on the photographs.

### Wireframes

Initial wireframes can be seen by clicking the following:
- [Desktop](https://github.com/malc-u/fostoria/tree/master/wireframes/desktop)
- [Tablet](https://github.com/malc-u/fostoria/tree/master/wireframes/tablet)
- [Mobile](https://github.com/malc-u/fostoria/tree/master/wireframes/mobile)

## Features

### Existing Features

#### Elements on every page
- Name of the page - in the far left corner of desktop/bigger tablet device - links to home page
- Top navbar that is reduced to navbar button placed in top left corner on smaller screens - this navbar included search bar that allows users to search through the photos (placeholder displays examples of searches)
- User profile icon (for registered users) or register/login (unregistered users) - Top right corner of bigger screens and in the middle for smaller screens - that is linked to registration/ login/ logout and profile view depending of the login status of page user
- Cart icon - linked to the cart view - far top right corner. It also displays total cart amount once products added to the cart
- Footer containing information about author of the photographs and that the page is for educational purposes only - fixed to the bottom of the page
- Footer with social media links and copyrights - bottom of the page

#### Index/home page
- Carousel consisting of 3 photographs of the artist as hero image.
- Button "Read more" to about page
- Button "Order prints" - directing to the all photos gallery

#### About page
- Information about the author
- Accordion with Frequently Asked Questions

#### Gallery
- Page header 
- 8 photographs displayed in 2 rows x 4 photos on big screens, 4 rows x 2 photos on medium screens and 8 rows x 1 photo on mobiles
- Paginator allowing to go through gallery - with active page coloured:
    - on first page there are 3 buttons "1", "Next" and "Last" 
    - following pages- except last - consisting of 5 buttons - "First", "Previous", Current page "number", "Next" and "Last"
    - last page is similar to first one - showing 3 buttons - "First", "Previous" and Current/last page "number"

#### Photo view/ detailed page
- Photo chosen for detailed view can be seen on the left side of the page (on large screens), and on the top of the page (medium and small screen)
- On the left (on large screens) and directly under photo (on medium and small screens) there are:
    - Photo title as a header
    - Information about where the photo was taken
    - Information about print sizes and print prices available
    - Form field allowing user to choose the size of the picture to add to cart
    - Form fied allowing user to choose the quantity of already chosen size to be added to the aart
    - "Add to cart" button
    - 2 additional buttons - "Keep browsing" and "Go to cart" allowing user to eaither go back to the gallery or to move tot he cart view

#### Contact page
- Page header
- Contact form with "Send" button
- Info on above the form about when to use the form and below the form about when the contact requests will be actioned

#### Login page
- Page header
- Link to registration if not yet registered
- Login form with "Submit" button

#### Register page
- Page header
- Link to login page if already registered
- Registration form with "Sign up" button

#### Profile page
- Page header
- Left side of the page contains pre-filled update form with user username and email and "Update" button
- Right side - info about orders:
    - You haven't ordered yet and "Check out our offer"(linked to gallery) button for users that haven't placed ordered yet
    - Table presenting all previous orders - containing each photo print name, size, quantity and total price as well as date when order was placed. Under the table is "Order some more" button(linked to the gallery)

#### Basket/cart page
- Page header
- Info about empty basket if no items in the cart and button "Keep browsing" linked to the gallery
- Basket contents that include photo added to the cart, its title, print size ordered, price for each print, quantity of the print that can be amended, "Update" and "Remove" buttons allowing user to subsequently update the qty of items in the basket of remove the item from the basket
- Below all items added to the basket there is an info about standard delivery cost and total basket value
- Below the basket content there is also "Checkout" button allowing logged in user to proceed with checkout or in case of not logged in it redirects to login page 

#### Checkout / delivery page
- Page header
- Delivery details form (name, address, contact phone number)
- Button "Confirm" allowing user to confirm delivery details

#### Checkout / payment page
- Page header
- Credit card processing form
- Information about the charge about to be submitted
- "Submit payment" button

### Features for future releases
- Password reset by e-mail
- Possibility of changing print size in cart view (not only quantity)
- Admin view allowing to add products using front-end (not only Django admin panel)

## Information Architecture

### Database Choice

- Database used during development (installed with Django) - sqlite3
- Database used once the project was deployed - PostgreSQL (SQL database provided by Heroku)

### Data Models

#### User

User model is this project is utilizing default User model from ``` django.contrib.auth.models ```

#### Products 

Within ``` products ``` app there are models that contain all details that are related to all items sold on this website

##### Product Group model

|         Name         |   Key in db  |   Validation   | Field type |
|:--------------------:|:------------:|:--------------:|:----------:|
|  Product group name  |     name     | max_length=254 |  CharField |
| Product display name | display_name | max_length=254 |  CharField |

##### Product model

|                    Name                    |   Key in db   |                     Validation                    |        Field type       |
|:------------------------------------------:|:-------------:|:-------------------------------------------------:|:-----------------------:|
|             Product name/title             |     title     |                   max_length=254                  |        CharField        |
|          Place of product's origin         |     place     |                   max_length=254                  |        CharField        |
|               Product's image              | product_image |                    blank=False                    |        ImageField       |
| Product Group this product is assigned to  | product_group | blank=False, null=False, on_delete=models.PROTECT | ForeignKey ProductGroup |

##### Pricing Sizes model

This model is created with Many to Many relationship from Django and displayed as a through model that is combined of 2 separate models with Foreign Keys to this one. 
1. First of these models is **Print Price model**:

|              Name              |  Key in db  |        Validation       |         Field type        |
|:------------------------------:|:-----------:|:-----------------------:|:-------------------------:|
|      Price of the product      | print_price | blank=False, null=False |        IntegerField       |
| Sizes of the product available | print_sizes | through='PricingSizes'  | ManytoManyField PrintSize |

2. Second of these models is **Print Size model**:

|               Name              |   Key in db  |        Validation       |         Field type         |
|:-------------------------------:|:------------:|:-----------------------:|:--------------------------:|
|       Size of the product       |  print_size  |      max_length=120     |          CharField         |
| Prices of the product available | print_prices | through='PricingSizes'  | ManytoManyField PrintPrice |

3. Combined **model Pricing Sizes** is built as follows:

|         Name         |  Key in db  |        Validation        |       Field type      |
|:--------------------:|:-----------:|:------------------------:|:---------------------:|
| Size of the product  |  print_size | on_delete=models.CASCADE |  ForeignKey PrintSize |
| Price of the product | print_price | on_delete=models.CASCADE | ForeignKey PrintPrice |

#### Checkout models

##### Order Shipping Details model

This model holds shipping information for an order user has placed.

|           Name          |      Key in db      |              Validation              |    Field type   |
|:-----------------------:|:-------------------:|:------------------------------------:|:---------------:|
| Customer placing order  |       customer      |       on_delete=models.PROTECT       | ForeignKey User |
|        User name        |      full_name      |      max_length=100, blank=False     |    CharField    |
|  First line of address  |  first_address_line |      max_length=75, blank=False      |    CharField    |
|  Second line of address | second_address_line | max_length=75, blank=True, null=True |    CharField    |
|       Town or city      |     town_or_city    |      max_length=50, blank=False      |    CharField    |
|          County         |        county       | max_length=50, blank=True, null=True |    CharField    |
|         Postcode        |       postcode      |       max_length=10, null=True       |    CharField    |
|         Country         |       country       |      max_length=50, blank=False      |    CharField    |
|       Phone number      |     phone_number    |      max_length=20, blank=False      |    CharField    |

##### Order Line Detail model

This model holds information of an order placed by the user. It relies on Order Shipping Details model as it includes Foreign Key to that model.

|          Name         |    Key in db   |                Validation               |            Field type           |
|:---------------------:|:--------------:|:---------------------------------------:|:-------------------------------:|
|    Shipping details   | order_shipping |   null=False, on_delete=models.CASCADE  | ForeignKey OrderShippingDetails |
|    Product ordered    |     product    |   null=False, on_delete=models.PROTECT  |        ForeignKey Product       |
|    Quantity ordered   |    quantity    |               blank=False               |           IntegerField          |
| Date order was placed |  date_ordered  | blank=True, default=datetime.date.today |            DateField            |
|      Order total      |      total     |               blank=False               |           IntegerField          |
|  Product size ordered |      size      |               max_length=3              |            CharField            |


## Technologies Used

### Languages 

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [Python](https://www.w3schools.com/python/)
- [JavaScript](https://www.w3schools.com/js/)

### Libraries & frameworks

- [JQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- [FontAwesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Django 3](https://docs.djangoproject.com/en/3.1/releases/3.0/)

### Tools
- [Visual Studio Code](https://code.visualstudio.com/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [GitHub](https://github.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [Amazon S3 bucket](https://aws.amazon.com/)
- [imgbb](https://imgbb.com/)
- [Django Cripsy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Sweetify](https://pypi.org/project/sweetify/)
- [Stripe](https://stripe.com/gb)
- [Dj-Database-Url](https://pypi.org/project/dj-database-url/)
- [Psycopq2](https://pypi.org/project/psycopg2-binary/)
- [Heroku](https://heroku.com/)
- [Travis CI](https://travis-ci.org/)
- [Pylint](https://pypi.org/project/pylint/)
- [Pylint-Django](https://pypi.org/project/pylint-django/)
- [Autopep8](https://pypi.org/project/autopep8/)
- [Balsamiq](https://balsamiq.com/)
- [Gunicorn](https://gunicorn.org/)
- [Tables generator](https://www.tablesgenerator.com/)


## Testing

Please see [Testing](https://github.com/malc-u/fostoria/blob/master/TESTING.md) for all my testing

## Deployment

### Running this project locally

Please ensure you have all listed below tools - installed on your local machine:
- IDE (Integrated Development Environment such as [Visual Studio Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/))
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://pypi.org/project/pip/)
- [GIT](https://git-scm.com/)
- [SQLite3](https://www.sqlite.org/download.html)

You will also need to open accounts on listed below:
- [Stripe](https://dashboard.stripe.com/register)
- [Amazon AWS](https://aws.amazon.com/) and [S3 Bucket](https://docs.aws.amazon.com/s3/index.html) set up
- [Gmail](https://www.gmail.com/)

Once all above are set-up please follow below steps:

1. **Save** a zip **copy of [this](https://github.com/malc-u/fostoria)** Github **repository** using "Clone of download" green button or clone repository directly to your IDE using command

```console
git clone https://github.com/malc-u/fostoria
```

2. In the terminal of your IDE **open folder with the repository**
3. **Create virtual environment** using command

```console
Windows: python -m venv <name of your virtual environment>
Linux: py3 -m venv <name of your virtual environment>
```

4. **Activate** your **virtual environment** with command (this must be done everytie your machine is restarted)

```console
Windows: <name of your virtual environment>\Scripts\activate
Linux: source <name of your virtual environment>\Scripts\activate
```

5. If needed upgrade pip locally using command

```console
Windows: python -m pip install --upgrade pip
Linux: sudo -H pip3 install --upgrade pip
```

6. **Install** all Python **modules** this project depends on using command:

```console
Windows: pip install -r requirements.txt
Linux: pip3 install -r requirements.txt
```

7. Set up the following environment variables within your IDE (create a file in the root of the project named "env.py", copy the code block below and populate with your details):

```python
import os
os.environ['SECRET_KEY'] = '<Your Django Secret Key>'
os.environ["STRIPE_PUBLISHABLE"] = '<Your Stripe Publishable Key>'
os.environ["STRIPE_SECRET"] = '<Your Stripe Secret Key>'
os.environ["AWS_ACCESS_KEY_ID"] = '<Your AWS Access Key'
os.environ["AWS_SECRET_ACCESS_KEY"] = '<Your AWS Secret Access Key>'
os.environ["EMAIL_HOST"] = '<Your SMTP Enabled Gmail Address>'
os.environ["HOST_PASS"] = '<Your SMTP Enabled Gmail Password>'
os.environ["DATABASE_URL"] = '<Your PostgreSQL Database URL>'
os.environ["HEROKU"] = 'True'
```

8. **Migrate** admin panel models to create your database template with the terminal command:

```console
Windows: python manage.py migrate
Linux: py manage.py migrate
```

9. **Create your superuser** to access django admin panel and its features:

```console
Windows: python manage.py createsuperuser
Linux: py manage.py createsuperuser
```

10. **Add** your **development IP** to the **ALLOWED_HOSTS** variable list in **settings.py**

11. Run your project locally:

```console
Windows: python manage.py runserver
Linux: py manage.py runserver
```

12. Once the program is running in a browser - **add "/admin" to the existing host address** to access django-login panel(e.g. http://127.0.0.1:8000/admin). **Log in** with your super-user details.

13. **Add** new **ProductGroups** followed by adding new **Product**, sizes in Print Size, prices in Print Price** and in PricingSizes match entered earlier size from Print Size with the price from Print Price models. 

14. After assigning prices to sizes to the database make sure they match contexts.py in Cart app. Sizes assigned by you must also be updated in templates/details.html in Products app where they exists as options in 'add_to_cart' form.

15. Once instances of these items exist in your database and match both contexts.py and form options in templates/details.html your local site will run as expected.

### Deploying to Heroku

In order to deploy this project to Heroku you will need to open accounts on:
- [Heroku](https://www.heroku.com/)
- [GitHub](https://github.com/)

Once this is done please follow below steps:

1. In your environment create ```requirements.txt``` file with terminal command:

```console
Windows: pip freeze > requirments.txt
Linux: pip freeze > requirments.txt
```

2. Create ```Procfile``` using terminal command:

```console
Windows: echo web: python app.py > Procfile
Linux: echo web: py app.py > Procfile
```

3. Create new repository on GitHub for this project, you can follow [this advice](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)

4. ```git add``` and ```git commit``` all changes done so far for this project and ```git push``` to your remote repository on GitHub

5. Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to the closest one to your actual location.

6. Go to "Rescources" tab in app's dashboard and from "Add-ons" search list pick "Heroku Postgres" - this will create your database.

7. Move to "Deploy" tab and pick deployment method as GitHub and link your Heroku app with chosen by you GitHub repository

8. Go to "Settings" tab in your Heroku app's dashboard, scroll down and click "Reveal Confirm Vars". Set them to the following ones:

|          Key          |                Value               |
|:---------------------:|:----------------------------------:|
|      SECRET_KEY       |      <Your Django Secret Key>      |
|   AWS_ACCESS_KEY_ID   |        <Your AWS Access Key>       |
| AWS_SECRET_ACCESS_KEY |    <Your AWS Secret Access Key>    |
|      DATABASE_URL     |   <Your PostgreSQL Database URL>   |
|       EMAIL_HOST      |  <Your SMTP Enabled Gmail Address> |
|       HOST_PASS       | <Your SMTP Enabled Gmail Password> |
|   STRIPE_PUBLISHABLE  |    <Your Stripe Publishable Key>   |
|     STRIPE_SECRET     |      <Your Stripe Secret Key>      |
|         HEROKU        |                <True>              |

9. In your IDE ensure you are now using Heroku Postgress as a default database instead on your local SQLite3 (this can be done by updateing your local env.py file as indicated in section "Running this project locally" no. 7 or commenting out your local database settings in settings.py)

10. Migrate your database to Heroku by using terminal command:

```console
Windows: python manage.py migrate
Linux: py manage.py migrate
```

11. Create super-user for your hosted project using terminal command:

```console
Windows: python manage.py createsuperuser
Linux: py manage.py createsuperuser
```

12. Go back to Heroku app's dashboard - tab "Deploy" - scroll down to "Manual Deploy", pick master branch and click "Deploy Branch"

13. Upon build completion you can view your app hosted on Herok by clicking "Open app" button provided.

14. From the link provided by Heroku add ```/admin``` (e.g. https://yourappname.herokuapp.com/admin) to the end of the url, log in with your super-user account and create instances of ProductGroup and Product within the new database. 

15. Once these are completed your app will work as expected.

## Credits

This project has been created by me, however some content has been :
- The photos used in this site were obtained from T. Zowada's [website](https://fostoria.pl/) and [Instagram](https://www.instagram.com/tomaszzowada_fostoria/)

### Acknowledgements

- [Simen Daehlin](https://github.com/Eventyret) - my Code Institute mentor
