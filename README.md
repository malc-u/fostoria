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
- [Django](https://www.djangoproject.com/)

### Tools

## Testing

Please see [Testing](https://github.com/malc-u/fostoria/blob/master/TESTING.md) for all my testing

## Deployment


## Credits

This project has been created by me, however some content has been imported:

- The photos used in this site were obtained from T. Zowada's [website](https://fostoria.pl/) and [Instagram](https://www.instagram.com/tomaszzowada_fostoria/)

### Acknowledgements

- [Simen Daehlin](https://github.com/Eventyret) - my Code Institute mentor
