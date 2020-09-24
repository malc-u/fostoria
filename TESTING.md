# Fostoria Testing

This is TESTING.md file created as an extension to the [README.md](https://github.com/malc-u/fostoria/blob/master/README.md)

- [Fostoria Testing](#fostoria-testing)
  - [Manual testing](#manual-testing)
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
  - [Automated testing](#automated-testing)

## Manual testing

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

## Automated testing
