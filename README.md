# The Newsbox, a blog designed to share stories and up/down vote 
(Developer: Paul Thomas O'Riordan)

![Screenshot of terminal](/)

[View live site](https://.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Scope](#scope)
    4. [Design](#design)
    5. [Wireframes](#wireframes)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals 

- To create a web application which will allow users to share blog posts and news articles similar to reddit and other users will be able to up and down vote posts according to how important/newsworthy they think they are. Users will also be able to comment on posts and engage in a discussion. 

### User Goals
- To be able sign up and create an online profile to share blog posts/news articles.
- To be able to upvote and down vote posts according to importance.
- To be able to comment on a post, engage in a discussion and like other poeples comments.

### Site Owner Goals
- Create a django application that functions in a similar manner to that which can be found on reddit
- Create a django application which users will be able to follow intuitively.
- Create a django application which is fit for purpose and does not have any bugs.
- Create a django application which will have full CRUD functionality. 

## User Experience
### Target Audience
- People who follow the news.
- People who are interested in blogs.
- People who are interested in online forums.

### User Stories

#### First-time User 
1. As a first time user, I want to know what is expected of me on the home page.
2. As a first time user, I want to be able to sign up to the web site easily and create a profile. 
3. As a first time user, I want to be able to read posts but not be able to comment or post. 
4. As a first time user, I want to receive an email after registering. 
5. As a first time user, I want to be able to log out of the web site easily. 

#### Site Owner
5. As the site-owner, I want to be able to review all posts, categories, users, upvotes, downvotes, likes etc.
6. As the site-owner, I want to be able to edit/update/delete a post. 
7. As the site-owner, I want to be able to receive queries from users via a form. 
8. As the site-owner, I want all areas of the site to function correctly and have no bugs. 

### Scope
In this first version all posts will be classified by the aggregate score of upvotes - downvotes. Ideally in future this would reset after a given amount of time to allow for newer posts to be shown in the feed on a daily basis. Also in future versions sign on using social profiles would be implemented as well as password recovery. The user model would also be altered. 

## Technical Design

### Flow Chart

Below you can see the ERD, created with [lucidchart](/)

![Screenshot of log on flowchart]()

### Data models

For this project I have used the following features:
- list comprehension making a list from an iteration, a more succinct way to create a list from a for loop. 
- Dictionaries e.g. in the username/password checking. 


## Technologies Used

### Languages

- [Python 3](https://www.python.org/)

### Frameworks and Tools

1. [Heroku](https://heroku.com/) - Heroku was used to deploy the project and to provide a virtual terminal to for examiners. 
2. [GitHub](https://github.com/) - GitHub was used as a remote repository to store project code. 
3. [Gitpod](https://gitpod.com/) - Gitpod was used as the main IDE for this project.
4. [lucidchart.com](https://www.lucidchart.com/pages/) - was used to draw flowchart and the ERD.


#### Libraries

### 3rd Party Libraries
1. [](https://) - JUSTIFICATION:  For the purposes of the project spec, I wanted to access and manipulate from googlesheets and to interact with the google API so I have chosen to use the gspread library for these functions.

2. [](https://) - JUSTIFICATION:  For the purposes of the project spec, I wanted to be able to give the user visual feedback similar to the official game which gives color clues to help the users identify which letters they have in the correct position and which letters they have in the word but not in the correct position. 

## Features

### 

![Screenshot of ](/)

**This screen covers the following user stories:**

1. As a first time user, .


### 

![Screenshot of ](/)

**This screen covers the following user stories:**

3. As a first time user, 

#### Feedback relating to letters

![Screenshot of ](/)

**This screen covers the following user stories:**

4. As a first time user, 

#### 

![Screenshot of ](/)

**This screen covers the following user stories:**

6. As the site-owner,

## Validation

### Python Validation
The Python code of each module was validated using [PEP8 Validation Service](http://pep8online.com/).  All modules returned a pass with 0 errors and 0 warnings.

![Screenshot of pep8](/)

### Testing user stories

All user stories were extensively tested and the clear and simple interface, constant feedback as well as gaining insight from different people, including my mentor, testing it without any prior knowledge of the game, all helped in the deployment of this project. 


1. As a first time user, 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|        |           |  |  |

![Screenshot of ](/)

2. As a first time user, 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|        |             |  |  |

![Screenshot of ](/)

3. As a first time user,

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|       |            |  |  |

![Screenshot ](/)

4. As a first time user,  

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|       |             |  |  |

![Screenshot of ](/)

5. As the site-owner, 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|        |           | |  |

![Screenshot of ](/)

6. As the site-owner, 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|      |            |  |  |

![Screenshot of ](/)

7. As the site-owner,

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|        |             |  |  |

![Screenshot of](/)

8. As the site-owner,

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|       |           |  |  |

![Screenshot ](/)



## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| Calling  |   Changed    |


## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are making a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/rashdogg74/).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/rashdogg74/).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

### Code

- **Code Institute** - for git template IDE and heroku deployment instructions.
- **Heroku** - for deployment [Heroku](https://heroku.com/) 
- **Bootstrap** - for styling [Bootstrap](https://getbootstrap.com/)
- **Code Institute** - for a walkthrough project which allowed me to reuse certain lines of code. 
- With the exception of the above, all code was written raw and occasional references to W3C schools, stackoverflow, youtube, slack. No code has been borrowed from other sources.

### Acknowledgments: 

- To my partner Ashley for helping me through a difficult time leading up to this project.