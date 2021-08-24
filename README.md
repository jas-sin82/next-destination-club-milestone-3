# Next Destination Club Holiday App

## Data Centric Development Milestone 3 project.

### Overview

This project presents a Holidays destiantions call Next destination Club. This is a website/app where User  can find and save their best destinations all around the world, User will able to create a account to see all destination or to save their own Holidays.Once user got login details next step is to update profile with add destination or to look around app to see the existing destination and other features.I have designed this project, fully focus on Database creation, security and CRUD(create, read, update and delete).App has a few diffrent webpages each page has different contents and buttons but as user prospective each webpage will easily and smoothly will navigate user to their destination.


##  Screenshots of project


# Desktop, Ipad & Mobile

![screenshot](static/images/responsive-snapshot.png)

# Highlights


 * [User Experience (UX)](#User-experience-UX)
    
    * [User Desire](#user-desire)
     
    * [User Stories](#user-stories)

    * [Wireframes of website](#wireframes-of-website)

    * [Design](#design)
       
        * [Colors](#colors)

        * [Typography](#typography)

        * [Imagery](#imagery)

        * [Icons](#icons)

    * [Database Model](#database-model) 

    * [Features](#features)

    * [Technology used in a Project](#technology-used-in-a-Project)

    * [Testing](#testing)

        * [ Functionality Test ](#functionality-test)
        
        * [ Compatibility testing ](#Compatibility-testing) 

        * [Code Validation Test](#Code-validation-test)

        * [Error found during site development ](#Error-found-during-site-development)

        * [ Performance Testing ](#performance-testing)

    * [Deployment](#Deployment)

    * [Credits](#credits)

    * [Screenshots of complete project](#screenshorts-of-complete-project)


#  User Experience (UX)

   

## User Desire

   * User is looking for app where user is able to Add, read, update and delete favorite Holiday Destination.

   * User will be easy intractive with the Holiday app beacuse all the webpages/navlinks will easily and smoothly will navigate 
     user to their destination..

   * User is able to  send their response to author of the app via contact form.

   * User is looking for app where user is able to find more stunning holidays destinations around the world.
     Author has provided some external links to user as well which will help them to find next holiday destination.

   [Back to Highlights ](#highlights)

## User Stories

 * As a first Time Visitor!

    * I want to easily understand the main purpose of the site.

    * I want to all the webpages/navlinks will easily and smoothly navigate user to their destination..

    * I want to easily access all the destination .
    
    * Able to Create an Account.

    * I want to know that my personal information is safe and stored securely on a database.

    * I want to have full control of my account, create ,read , update  and  delete my destinations.

    * Able to contact or send feedback to author via contact form.

 * As a returning visitor:

    * Able to easily register and update my profile information.

    * Able to log into my account and access to all features of the site.

    * Able to create, read, update, delete my destinations.
 
    * Able to  reach author if any question via contact form or send feedback to author via contact form.

 * Frequent Visitor:

    *  I want to be able to manage my own holiday destination either by editing or deleting.

    *  I want to able to manage my profile information by update my username or password.


 *   As an Author of the site:

     *  Be able to add new categories(right now author can edit or create new category)!

# Strategy 

  * As a author I have Choose a holiday colors for web design that will help to convert visitors to regular user.
    The home page contain some of the beautiful holiday images which will attract visitors to find out more about 
    website.

  * New user can explore the landing page and even more ! stragically placed read more button which will navigate user to the
    connecting page, where user will find some of the beautiful destinations with external API.

  * The website functinality (website enable the user to) :-

    * Register and Log in to account.

    * Create their favorite destinations & save them in to the database.

    * User can veiw holiday destination created by them , or by other users!
     
    * Edit & Delete a destination created by own.
    
    [Back to Highlights ](#highlights)

# Wireframes of Website  

### I used a balsamiq to create a wireframe. Here is link [balsamiq](https://www.balsamiq.com/)
       
 ![screenshot](static/wireframes/wireframe-1.png) 
  
 ![screenshot](static/wireframes/wireframe-2.png) 

 ![screenshot](static/wireframes/wireframe-3.png)


 [Back to Highlights ](#highlights)

# Design 

  * Colors 

    * Themecolor of the webpage is bit much same as sea blue #1A2980,  #26D0CE, #1A2980 ,which I think is good for user intraction and 
      I have placed two buttons on the home page color of orange text and white background.The main purpose of this background color  
      is to make user intraction above. 
    
    *  Most of the webpage text has written in white and yellow color which create nice combination with background color  #1A2980,  
       #26D0CE, #1A2980 and make webpage more user intractive. The color blue has positive affects on the mind and the body.
       As the color of the spirit.

    *  Blue represents both the sky and the sea, and is associated with open spaces, freedom, intuition, imagination, expansiveness,' inspiration, and sensitivity.
       Blue also represents meanings of depth, trust, loyalty, sincerity, wisdom, confidence, stability, faith, heaven, and intelligence.
      
  * Typography 

    * There will be two fonts used throughout the website. Roboto , Playfair Display SC and Serif specific so that will be used for the fall back font,
      Playfair Display SC font used in  webpage headings and Logo to make more user intractive.

  * Imagery

    * Choices of the images is an important component of this site. I chose clean images that will intract Visitors. Three images at the home page to catch the visitors    
      intrerest and strategically add bootstrap carousel which contains three stunning beach images  which will help to attract visitors to look more in side webpage.

    * Navigation overlay menu bar which cover whole screen ! one of the big user attrative design.

  * Icons 
    
    * All icons used are taken from Font Awesome [Font Awesome.](https://fontawesome.com/). I have used search button icon and icon used in add destination
      form,direction icon used in all image cards, edit ,delete ,create links , umbrella icon used for external links,register button and social media
      link in the footer even icon used in nav links both in overlay bar and footer links.

# Database Model

   * This project uses MongoDB for all database its a document-orientated database program.

   * MongoDB Atlas is used as database backend for storing user and destination details. 
     There are three collections name Categories , destinations and Users.

     ![screenshot](static/wireframes/database.png)


     
     
       



