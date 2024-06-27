In our final lab, we are taking the idea of lab 1, a page with different users and their access levels and authorized access to different pages. We changed from lab 1 with instead storing the users into a sql database, while also adding their access level AND a value for their failed attempts of logging in. To start, run the werk.py program to start up the webpage. When you first open the web page, you are given two options: a button to login and a button to sign up. If you click the login button you will then be redirected to a login page. Entering a username that does not exist in the database will prompt a message saying that the username is invalid. If the username is valid, then you will have three attempts to get corresponding correct password. The first two times you enter the wrong password, you will be alerted that the wrong password has been entered. If you enter the wrong password 3 times, your account will be locked out and you will have to contact support to unlock your account, but if you do get the password right within 3 attempts, your failed attempts will be reduced back to zero. Once you do log into your account, you will then be brought to a page that gives you buttons that lead to webpages that you are authorized to visit, the other pages will not be an option to click. Once you are in one of the authorized pages, you will have a welcome message, and a button to go back to the main home page. For the sign up option, once you click the sign up button you will brought to a webpage that first prompts you for a username. If the username is already in our database, you will be prompted to re-enter a username. Once you enter a username that is available, you will be then be redirected to another webpage to create a password. You will have 2 options, you can either click the generate strong password button that will generate a strong password for you and add you to the database, if you select this option, after clicking the generate password button you will be shown your password on a different page, which you will obviously need to copy and then hit the home button. Or you can create your own password, if the password does not meet the requirements, then you will prompted to enter it again. Once you reach the requirments, your account again will then be added to the database and you will automatically be sent to the home page. After your account is successfully created, you are then redirected to the home page where you can login or sign up another account. Each new user only has level 1 access, and each custom password needs one lower and higher uppercase character, 1 number, 1 special character and be atleast 8-25 characters long. 
The UI for this program is basic, as I am not the best at CSS and know little to no JS (so it is not present). Each password is salted, encoded and the saved into the database in that style, so the password can not be found easily. No script was used, so I did not see any point of using any SRI and our database is parameterized to avoid the risk of injection attacks. 

I also looked up how to hide sensitive data from the URL and used this GeeksForGeeks article on the flask's session method: https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/#

One more note: There are several usernames and password combos already in the database, I wanted to keep them in there to show the functionality of there not being able to re-use usernames.
