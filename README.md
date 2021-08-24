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

   * Destionations :- All the destination created by user will be saved safely in database! 

     ![screenshot](static/wireframes/database-2.png)


   * User Data :- user name & password will be securely save in user collection ( by using Werkzeug Security password hash).
   
      [Back to Highlights ](#highlights)

# Features

  ## Existing Features

  
  Every page of the website features a consistently responsive and intuitive layout and navigational system:

  
### General features

  * full page overlay navigation which will open once click on menu icon from left to right and to close click on cross icon.

  *  All the webpages are fullt responsive on all devices.

  *  Footer will seen on all the pages on left side next destination logo, and rest it contains nav links and social links as well.
 
  *  full page overlay nav fully responsive on all devices.

  *  All the image cards and text are fully responsive.

  *  User or Visitor can contact author  via contact form! which is available for every one both first time visitors or to existing User.

  *  Search functionality which will help to find destination by destination name and country name.

### Home page 

  * Home page contains some beautiful images  and color combination will attract user.

  * Two buttons on home page ! on top lef button will lead visitors to registration page so visitor can create account and other button will lead to connecting 
    page of the next holiday destination where able to see some more best destinations and with external links of holiday webpage.

### register account 

  *  Here Visitors are able to create their account by follow the account create instructiion which is provided under the each input.

  *  Once user register! page will redirect to profile page and will show welcome message.

### Destination Page 

  * Destination page where all the added destiantion will appear so all exisitng user can see them and can search by destination name.

  * User can independently walk around and read other users destionation.

### Add destination page 

  * Once user has registered on Next destination club so they are able to add own destination by fill up the add destination form step by step.

  * Once user succesfully added destination , will get flash message on top and will redirect to destination page.

  * User need to fill the add destination form completely with proper information ! cant skip any input empty.

### Profile page 

  * Here is place where user  can independently play around ! I mean user can edit and delete their profile as their wish ,not just profile 
    user is able to delete , edit , create new destination as well. 

  * Every time when user want do delete process! will get one warning message before delete , which will make user to change their mind and 
    go back with out remove.

### Login page and logout page 

  * Once user login  in their account it will redirect to profile page where user can add their destination and delete ,edit,or update user 
    information.
  
  *  Once User logout it will redirect user to login page and will get flash message!  for security purpose message will appear on top 
     (user has succesfully log out).

## Features left  which I want to implement in future:-

  * First implement will be allow  user  to upload profile image.

  * Second implement will be create 2 extra input in add destination form ! first one will be hotel links so user will have idea what cost it will be 
    around and second  will be links for sight touring of destination.

  * Email notification functionality for users to be alerted when a new destination is added.

  * Add pagination to the next holiday destination, destinations would be displayed on a new page and pagination would be displayed.
   
    [Back to Highlights ](#highlights)

# Technology used in a Project

  ## Frameworks, Libraries & Programs

   * HTML5 
      
      * Markup language used for structuring and presenting content on the internet.
  
   * CSS 

      * Cascading Style Sheets tO style the whole structure of project.

   * Java Script
     
      * Java script used for full screen overlay navigation menu and contact form validation.

   * Python 

      * Python is an interpreted high-level general-purpose programming language. Used to write the logic that operates the site.

   * Emailjs 
    
      * EmailJS is a allows for the sending of emails directly from JavaScript without the need for any backend code. Here is link emailjs

   * Bootstrap 5 & Media Query
    
      * To make it responsive on all the devices such as Desktop , Ipad and Mobile.

   * Flask 
    
       * framework used to create and populate the templates.

   * Jinja 

       * Jinja templating language used to simplify and display backend data in html.

   * PyMongo 

       * flask_pymongo used for interacting with MongoDB database from Python.

   * Google Font
    
      * To make structure beautiful.

   * Github
     
     * Used to store the projects code after being pushed from Git.

   * Git 

     * used for version control to commit to Git and push to Heroku.

   * Gitpod 

     * Used as code editor to create my project.

   *  Font Awesome

      * Used to display icons as well as the social media icons in the footer.

   * Favicon

     * Used to generate the websites favicon logo of various sizes for different devices.

  *  Balsamiq 

     * I used a balsamiq to create a wireframe

  *  Heroku

     * Cloud platform used to deploy application.

  *  W3C Validator HTML & W3C Validator CSS

     * Both used to test all the code for the project to check for valid HTML and CSS.

  * JSHint
     
     * It used to test and validate all Javascript written for this project.

    [Back to Highlights ](#highlights)

# Deployment 
  
 ## Version control

 The project was deployed on GitHub Pages. I used Gitpod as a work space where I commited all changes to git version control system. 
 I used push command in Gitpod to save changes into GitHub.

## Github

  ### To run localy

   * Log in to GitHub and click on repository to download ([Milestone Project 3](https://github.com/jas-sin82/next-destination-club-milestone-3)).
   
   * Select `Code` and click Download the ZIP file.
   
   * After download you can extract the file and use in your local environment.
   
   * Second option is you can [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
     or [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repository ([Milestone Project 3](https://github.com/jas-sin82/next-destination-club-milestone-3)) into your github account.

## Heroku

  This project is live and automatically deployed to Heroku. The following steps outline the necessary steps to set-up and deploy a project that uses Python alongside MongoDB.
  
  * Before deploying your project create a requirements.txt file by running the following command in the CLI

         pip3 freeze --local > requirements.txt

   * Create a Procfile file by running the following command in the CLI

         echo web: python app.py > Procfile 

   * Once theses files have been correctly created commit and push these to your GitHub repository.

   * Create an account/log in to your Heroku account.

   * select "New App"

     ![screenshot](static/wireframes/heroku.png)


   * write your project name (make sure it must be unique ) and select your region, and then click "Create app.


     ![screenshot](static/wireframes/heroku-2.png)

   * You will directly to the deploy screen for your project.To connect directly to your GitHub repository select the deployment
     method ( Git Hub conncect to Git Hub)
     

      ![screenshot](static/wireframes/heroku-3.png)

   * After you connected to your repository, click on "Settings" tab on your app dashboard, and click on "Reveal Config Vars"  
     add your configuration variables to Heroku.

   * Then back to the deploy tab and select "Enable Automatic Deploys" and from Manual deploy choose your master branch, and click "Deploy Branch

      ![screenshot](static/wireframes/heroku-4.png)

  *  Success message will appear your app is successfully deployed, to live view click on View.

  


     

    

     





     
     
       



