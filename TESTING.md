# Fostoria Testing

This is TESTING.md file created as an extension to the [README.md](https://github.com/malc-u/fostoria/blob/master/README.md)

- [Fostoria Testing](#fostoria-testing)
  - [Automated testing](#automated-testing)
    - [HTML validation](#html-validation)
    - [CSS validation](#css-validation)
    - [JavaScript validation](#javascript-validation)
    - [Python validation](#python-validation)
      - [Python testing](#python-testing)
      - [Travis CI](#travis-ci)
  - [User stories testing](#user-stories-testing)
    - [As a new user I want to be able create an account](#as-a-new-user-i-want-to-be-able-create-an-account)
    - [As a new user I want to visit gallery of available to purchase photos](#as-a-new-user-i-want-to-visit-gallery-of-available-to-purchase-photos)
    - [As a new user I want to find out what print sizes are available to purchase](#as-a-new-user-i-want-to-find-out-what-print-sizes-are-available-to-purchase)
    - [As a returning/registered user I want to be able to login into my account](#as-a-returningregistered-user-i-want-to-be-able-to-login-into-my-account)
    - [As a returning/registered user I want to be able to see my profile](#as-a-returningregistered-user-i-want-to-be-able-to-see-my-profile)
    - [As a returning/registered user I want to be able to see my previous purchases](#as-a-returningregistered-user-i-want-to-be-able-to-see-my-previous-purchases)
    - [As a returning/registered user I want to have possibility of changing my profile details](#as-a-returningregistered-user-i-want-to-have-possibility-of-changing-my-profile-details)
    - [As a purchasing user I want to add chosen product to my cart/basket](#as-a-purchasing-user-i-want-to-add-chosen-product-to-my-cartbasket)
    - [As a purchasing user I want to view products currently added to my cart/basket](#as-a-purchasing-user-i-want-to-view-products-currently-added-to-my-cartbasket)
    - [As a purchasing user I want to have possibility of changing quantity of products in the cart/basket](#as-a-purchasing-user-i-want-to-have-possibility-of-changing-quantity-of-products-in-the-cartbasket)
    - [As a purchasing user I want to remove items from my cart/basket when i changed my mind](#as-a-purchasing-user-i-want-to-remove-items-from-my-cartbasket-when-i-changed-my-mind)
    - [As a purchasing user I want to see total value of my cart/basket](#as-a-purchasing-user-i-want-to-see-total-value-of-my-cartbasket)
    - [As a purchasing user I want to be able to enter address I want my purchase dispatched to](#as-a-purchasing-user-i-want-to-be-able-to-enter-address-i-want-my-purchase-dispatched-to)
    - [As a purchasing user I want to be able to pay for my purchase](#as-a-purchasing-user-i-want-to-be-able-to-pay-for-my-purchase)
    - [As a browsing/visiting user I want simple, not too complicated page to use](#as-a-browsingvisiting-user-i-want-simple-not-too-complicated-page-to-use)
    - [As a browsing/visiting user I want to use my page on my phone or tablet as well as my desktop](#as-a-browsingvisiting-user-i-want-to-use-my-page-on-my-phone-or-tablet-as-well-as-my-desktop)
    - [As a browsing/visiting user I want to be able to see all products in 1 gallery](#as-a-browsingvisiting-user-i-want-to-be-able-to-see-all-products-in-1-gallery)
    - [As a browsing/visiting user I want to have possibility of searching gallery](#as-a-browsingvisiting-user-i-want-to-have-possibility-of-searching-gallery)
    - [As a browsing/visiting user I want to click on the picture in the gallery and be presented with info about it](#as-a-browsingvisiting-user-i-want-to-click-on-the-picture-in-the-gallery-and-be-presented-with-info-about-it)
    - [As a browsing/visiting user I want to see photos grouped into categories](#as-a-browsingvisiting-user-i-want-to-see-photos-grouped-into-categories)
    - [As a browsing/visiting user I want to find frequently asked questions](#as-a-browsingvisiting-user-i-want-to-find-frequently-asked-questions)
    - [As a browsing/visiting user I want easy way of contacting page owner - via contact form](#as-a-browsingvisiting-user-i-want-easy-way-of-contacting-page-owner---via-contact-form)
  - [Manual testing](#manual-testing)
    - [Responsiveness](#responsiveness)
      - [Bugs - responsiveness](#bugs---responsiveness)
    - [Interaction](#interaction)
      - [Bugs - interaction](#bugs---interaction)
    - [Logic](#logic)
      - [Bugs - logic](#bugs---logic)

## Automated testing

### HTML validation

This was done using [W3C Markup Validation Service](https://validator.w3.org/) on both html files in hte development stage as well as on deployed project using live links.

**Bugs in HTML:**

There is 1 error found " Element ul not allowed as child of element small in this context" for the view https://fostoria.herokuapp.com/accounts/register/ . This cannot be addressed as it is an error within the crispy form code and it is automatically rendered by django-crispy-forms.

### CSS validation

CSS was prefixed with [Autoprefixer CSS online](https://autoprefixer.github.io/) with included last 3 versions of browsers.
CSS was validated using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) with no errors found.

### JavaScript validation

JavaScript was validated using installed in Visiual Studio Code [JSHint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint) extension.

### Python validation

Python was validated using installed in Visual Studio Code [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension as well as [pylint](https://pypi.org/project/pylint/) linter and [pylint-django](https://marketplace.visualstudio.com/items?itemName=ms-python.python) plugin.

#### Python testing

To run existing Python tests follow below steps:
1. Activate your virtual environment using terminal command:


    ```console
    Windows: <name of your virtual environment>\Scripts\activate
    Linux: source <name of your virtual environment>\Scripts\activate
    ```
2. Run tests by using terminal command:

    ```console
    Windows: python manage.py test
    Linux: py manage.py test
    ```

3. Test can be also run for a specific app using following terminal command:
   
    ```console
    Windows: python manage.py test app_name_here
    Linux: py manage.py test app_name_here
    ```

4. Test results will be summarised in the terminal.

#### Travis CI

[Travis CI](https://travis-ci.org/) was used to test the project. 

## User stories testing

### As a new user I want to be able create an account
  
Anyone visiting this page can create an account. They can do this by clicking in "register" link under user icon or while trying to process the payment during checkout.

### As a new user I want to visit gallery of available to purchase photos

Link to gallery is located in a main navbar. They can also be found hidden under few buttons located thought this page. These are:-
- "Order prints" button on the bottom of home/index page
- "Keep browsing" button in an empty basket
- "Keep browsing" button on the bottom of photo details page
- "Order some more" button under table with previous orders in a user profile view
- "Check out our offer" button in a user profile view when there haven't been any orders placed yet
  
### As a new user I want to find out what print sizes are available to purchase

Information about sizes available to order can be found in FAQ section on the about page and in photo details view.

### As a returning/registered user I want to be able to login into my account

Every previously registered customer has got possibility of login into their own account. This can be done by accessing login page through link placed under user icon on the top of the page in the navbar section.

### As a returning/registered user I want to be able to see my profile

Every previously registered customer can access their profile view by login into their account. User profile allows the user to see their previous purchases as well as amend some on their login credentials (username and linked ot the account e-mail).

### As a returning/registered user I want to be able to see my previous purchases

All previous purchases for registered user can be accessed via login in page and profile view.

### As a returning/registered user I want to have possibility of changing my profile details

Every previously registered user has got possibility of amending some of their user credentials - username and email.

### As a purchasing user I want to add chosen product to my cart/basket

While browsing the gallery every user (registered or not) has got possibility of adding chosen photo to cart. They can do that by choosing favourite picture, clicking it therefore accessing photo details page. There they have possibility of choosing the size of the print they wish to add to cart as well as quantity.

### As a purchasing user I want to view products currently added to my cart/basket

Products currently added to the cart can be viewed by simply clicking the cart icon on the top of the page. This view will display all photo prints added to the cart, their name, size, price as well as total price of the cart/basket. 
This view can be also accessed by clicking "Go to cart" button in photo detail view.

### As a purchasing user I want to have possibility of changing quantity of products in the cart/basket

Cart/basket view gives possibility of amending/updating the quantity of added to the cart items. This is simply done by amending the number of chosen photo and pressing "Update" button.

### As a purchasing user I want to remove items from my cart/basket when i changed my mind

Cart/basket view gives possibility of removing added to the cart items. This is simply done by pressing "Remove" button.

### As a purchasing user I want to see total value of my cart/basket

Total value of the items added to the basket is displayed within cart view as well as underneath the cart icon - on the top of the page, in the navbar section.

### As a purchasing user I want to be able to enter address I want my purchase dispatched to

Every time website user decides to proceed with the purchase there are 2 steps to a checkout process - first of them is to enter customer's shipping address thus allowing user to specify the address the purchase is dispatched to.

### As a purchasing user I want to be able to pay for my purchase

Checkout process consist of 2 steps, second step being processing the card payment for the order. 

### As a browsing/visiting user I want simple, not too complicated page to use

Layout of the page is consistent with the market standards. All information is placed where it is expected to.
Navigation is simple, not too advanced, there are not complicated routes to get to the information needed.

### As a browsing/visiting user I want to use my page on my phone or tablet as well as my desktop

This page was created utilising Bootstrap framework therefore it works on all devices from small phones to large desktop screens.

### As a browsing/visiting user I want to be able to see all products in 1 gallery

This page contains main gallery showcasing all pictures available for purchase, there are also 3  additional galleries that present parts of main gallery depending on the classification made by the developer.

### As a browsing/visiting user I want to have possibility of searching gallery

There is a search bar provided within the navbar that allows user to search photo titles and name of the places where the picture was taken. Search bar contains examples of search words as a hint for a user.

### As a browsing/visiting user I want to click on the picture in the gallery and be presented with info about it

Each photo clicked in the gallery links to the photo detail page that displays more information about it.
There is also a possibility to order a print of chosen picture from the detailed view.

### As a browsing/visiting user I want to see photos grouped into categories

The developer decided to group photos into 3 categories depending on the subject of the photo.
These are:
- Lakes & Seas
- Forests
- Fields & Mountains
  
Alternatively every browsing user can search the gallery via search bar (e.g. using name of the place that pictures were snapped in (these can be seen in pictures details)).

### As a browsing/visiting user I want to find frequently asked questions

There is a FAQ section of the About page that can be easily accessed from any part of this website via top navbar links. It will provide answers to frequently asked questions such as: "What is the actual size of A3 print?" etc.

### As a browsing/visiting user I want easy way of contacting page owner - via contact form

The contact form can be accessed via link in the main navigation bar. It allows user to send an email message to the store owner. It is easy, hassle free process of submitting a form consisting of 3 fields - user's contact e-mail address, message subject and message text. It gives the website owner all information needed to be able to respond.

## Manual testing

### Responsiveness

- **Plan**: this page was planned to be responsive, working on all devices - mobile phones, tablets and desktops. Following this it was planned for Bootstrap library to be used for a page design.
- **Implementation**: page was **tested in Chrome Developer Tools** throughout the process of putting it together to make sure it was responsive to all devices. "Responsive" slider was used to make sure content is shown correctly on desktop, tablet and mobile, that they look as desired by the developer. Bootstrap classes as well as media rules were used to adjust responsiveness. **Tested the pages on devices available in Chrome**, these were:
  
  - 240 x 360 Jio Phone 2
  - 280 x 653 Galaxy Fold
  - 320 x 568 iPhone 5/SE 
  - 360 x 640 Blackberry Z30 & Galaxy Note
  - 375 x 667 iPhone 6/7/8
  - 375 x 812 iPhone X
  - 411 x 731 Pixel 2
  - 414 x 736 iPhone 6/7/8 Plus
  - 540 x 720 Surface Pro
  - 600 x 960 Nexus 7
  - 600 x 1024 Blackberry PlayBook
  - 768 x 1024 iPad
  - 800 x 1280 Nexus 10
  - 1024 x 1366 iPad Pro
  
- **Result**: page is responsive and can be used on all planned devices. There are no elements on this page that are not responding as planned.
- **Conclusion**: all tests that were run on responsiveness were passed therefore page is fully responsive.

#### Bugs - responsiveness

Throughout the development process I came across these bugs:

- **Footer**
  - **Bug**: footer information was not displaying as intended
  - **Fix**: added media in CSS to adjust the size and text-alignment
  - **Result**: this bug was removed and footer info is displayed as intended on all screens

- **Qty in basket contents**
  - **Bug**: quantity input field and label were not centered on small screens
  - **Fix**: added media in CSS to adjust the alignment
  - **Result**: this bug was removed and footer info is displayed as intended on all screens

### Interaction

- **Plan**: there are elements that are planned to be interactive on this page e.g. buttons throughout the page, navbar, photos in the gallery, forms (login, register, contact, update dteails in the user profile)etc.
- **Implementation**: interaction was carried out on many devices and on several browsers, including Chrome, Firefox and Opera. Following elements were tested by making sure they act in the way they were intended, that they lead to the page or action as planned.
  - Navbar toggle button
  - Navbar links
  - Logo/project name
  - User button
  - Cart button
  - `Read  more` button on index page
  - `Order prints` button on index page
  - Accordion on about page
  - Gallery - each picture
  - Gallery - pagination buttons
  - Contact form + `Send` button
  - Search bar
  - User button
  - Login form + `Submit` button
  - Register form + `Sign up` button
  - Update form + `Update` button
  - `Check out our offer` button within profile (no previous orders)
  - `Order some more` button within profile (orders previously placed)
  - Cart button
  - Size selector within product details display
  - Quantity selectro within product details display
  - `Add to cart` button within product details display
  - `Keep browsing` button with product details display
  - `Go to cart` button within product details display
  - `Keep browsing` button - empty basket display
  - Quantity selector - cart display
  - `Update` button - cart display
  - `Remove` button - cart display
  - `Checkout` button - cart display
  - Delivery details form + `Confirm` button within checkout
  - Payment details form + `Submit payment` button within checkout
  - Sweetify messages
  - Footer icons
- **Result**: all tested elements are interactive as planned . There are no elements on this page that are not responding as planned
- **Conclusion**: all tests that were run on interactivity were passed therefore page is interactive

#### Bugs - interaction

Throughout the development process I came across two bugs related to page interaction:

- **Removed from cart message**
  - **Bug**: sweetify message was disappearing without confirmation button clicked
  - **Fix**: relised that `Remove` button is placed within update form therefore JavaScript function that operates this (removal using update form) will not wait for a button click
  - **Result**: this bug was removed and after removing item from the cart there is a message "Removed!" displayed that dissapears on its own.

### Logic

- **Plan**:
  - the page was planned to have 2 tier access for unregistered and registered users,
  - search bar is intended to allow users to search for photo title or name of the place where photo was taken
  - it was planned to allow only registered users to proceed with the purchase,
  - this page is intended to allow all user to use contact form but all fields of the form must be filled in before submission,
  - products/photos were intended to be displayed as a gallery as well as based on main subject of a photo
  - all products added to the cart can be revised - quantity added can be changed or item can be removed from the cart
  - cart should be displaying total price of items within the cart at all times (if any items added, if none there is no total dispalyed)
  - user profile displays all previously placed orders by registered user
  - user profile view allow user to change username or e-mail associated with the profile
  - user has possibility od setting delivery address during checkout
  - user has possibility to pay with card
- **Implementation**:
  - attempted to access pages intended for registered users by pasting direct access address to the address bar in the browser eg. fostoria.herokuapp.com/accounts/profile (not successful - redirected to login page as a result)
  - attempted to search for random keywords that do not exist in product names and places (not successful -message "no photos matching your search cirteria" displayed accordingly)
  - attempted to proceed to checkout without user being registered/logged in (not successful - redirected to login page)
  - attempted to submit the contact form without filling in all fields (not successful - warning messages displayed informing fields must be filled in)
  - attempted to display gallery not included in the navbar by amending address directly in the browser - e.g. fostoria.herokuapp.com/photos/trees/ (not successful - 404 page displayed)
  - checked if quantity of added to the cart products is actually amended when button `Update` pressed (successful)
  - checked if product is removed from the cart when `Remove` button pressed (succcessful)
  - attemped the brake the logic of cart total price by changing the quantity and number of products in the basked by adding, updating and removing several items (not successful - total price displayed correctly at all times)
  - attempted to log in with old username after it was udated using user profile udate form (not successful - username was changed therefore login is possibile with updated/ new username)
  - placed dummy order to check it displays in uder profile (successful)
  - attempted checkout without setting delivery address (not successful)
  - attempted to place the order wihotu giving card details (not successful)
- **Result**: all tested elements are working properly. There are no elements that present problems with logic
- **Conclusion**: all tests that were run on logic were passed

#### Bugs - logic

Throughout the development process I came across these bugs:

- **Assigining correct price and size**
  - **Bug**: adding item to the cart was not assigning correct price for chosen size
  - **Fix**: added conditional in cart.contexts.py 
      ```python
      if size == 'A3':
          price = 60
        elif size == 'A2':
          price = 75
        elif size == 'A1':
          price = 90
        elif size == 'A0':
          price = 115
        else:
          price = 140
      ```
  - **Result**: this bug was removed and all prices as well as total price for the order is now assigned correctly
