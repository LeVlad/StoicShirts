# StoicShirts
A Django created e-commerce site for selling shirts with stoic quotations on them.

# Table of Contents #

1. Design and Market research
2. User Stories
3. Functionality
4. Technologies Used
5. Tests
6. Errors and Fixes
7. Deployment
8. Credits



# 1. Design and Market Research #


During the research for the business model or idea I found that the keywords "stoic" and "quotes" were very sought after and had high organic values especially in the United States.
![Keyword Search](https://user-images.githubusercontent.com/88729876/187352948-2fc48b72-edda-4383-b25f-0c8d6ddde93c.jpg)

The site is made up of 7 page options displayed on a horizontal navbar:
 - Home
 - Products can be sorted by price, rating, category and philosopher or all can be selected
 - Categories can be sorted by every category available or all can be selected
 - Philosophers can be sorted by 5 philosophers
 - Contact Us
 - Subscribe
 - My Account has a dropdown of two options "Register" or "Login"

![Main Page](https://user-images.githubusercontent.com/88729876/187325911-5eec3c5a-1a11-4da4-9b0a-52d43832f6db.jpg)


The initial design of StoicShirts was meant to be slightly different as I wanted to have the navbar spread out  in the 4 corners of the page and in the middle would site the shirt logo.


# 2. User Stories #

User
- As a user I can login so that I can view my account
- As a user I can select products so that I can purchase them
- As a user I can search so that I can browse products
- As a user I can receive an e-mail so that I can confirm my account has been created
- As a user I can rate and leave a review
- As a user I can download an invoice so that I can prove the purchase/ keep for my records
- As a user I can recover password so that I can retrieve access to my account
- As a user I can rate and leave a review
- As a user I can browse so that I can view all the products

Admin
- As an admin I can login so that I can update products, approve reviews, check details of orders
- As an admin I can login so that I can check and update the account details

![User Stories 1](https://user-images.githubusercontent.com/88729876/187320609-b1de0d92-6cb9-44f8-bbbe-8e6a83b02bbc.jpg)

# 3. Functionality #

On StoicShirts any user can:

- access the main pages
- browse the shirts
- add to a check-out bag
- delete from the check-out
- make purchase
- create an account
- view orders
- subscribe tot the newsletter
- browse reviews
- leave a review

# 4. Technologies Used #

## Languages ##
HTML
CSS
Javascript
Python

## Frameworks ##
Django
Bootstrap

## Libraries ##
Jquery
Stripe Payments

## Tools ##
AWS
Heroku
Git
Postgres

# 5. Tests # 

No automated test carried out apart from lighthouse report. The rest have been to check whether we have functionality in finding products, uploading them as an admin, deleting them and leaving reviews as users.

Lighthouse
![lighthouse report 1](https://user-images.githubusercontent.com/88729876/187338471-b0c96dda-e5bc-49eb-8bd6-1dda2c7ef462.png)

A newer report was unavailable as the queries have exceeded the limit.

# CSS VALIDATOR WCS #
![CSS Validator](https://user-images.githubusercontent.com/88729876/187345959-a0da1462-1700-4a19-b498-94592c3bc291.jpg)

# 6. Ongoing Errors and Fixes # 

Problem  --> Error Message --> Solution

1. Add to bag error   -->  Missing "k" in pk= definition -->  Added missing letter     
2. Crispy Field error --> as_crispy_field got passed an invalid or inexistent field" -->  Added missing letter 
3. Deleting product error get_object_or_404 --> Function used instead of parameter ("request") --> Replaced function with "Product" parameter
4. No image media in settings.py --> No module named "django.template.context.processor" -->  Added missing "s" for processors.
5. Contact Us page not working  --> Contact.html template does not exist" --> added better view description and url linking
6. Subscribe page not working  --> Template does not exist -->  Added correct urls in contact/ urls.py
7. Toast Error  --> TemplateSyntaxError  --> Corrected template typo
 
1.![add to bag toast issue](https://user-images.githubusercontent.com/88729876/187349166-6b37069e-f7ae-489f-b7d7-45172f8957c1.jpg)

2.![Crispy Error Checkout](https://user-images.githubusercontent.com/88729876/187349134-4be3f25e-49ad-433a-8a11-6ef83c5a9470.jpg)

3.![deleting error 1 2](https://user-images.githubusercontent.com/88729876/187349234-02c9ebe4-a3d0-444b-bf48-d9aad6d419bb.jpg)

4.![no image media settings py missing s](https://user-images.githubusercontent.com/88729876/187350865-af1bff04-f6b1-4e87-9fa5-38f778e23334.jpg)


5.![Dev Contact Us](https://user-images.githubusercontent.com/88729876/187350816-352ffa7d-c5a6-4df1-a93e-b27fd55e3f8f.jpg)


6.![Subscribe 2](https://user-images.githubusercontent.com/88729876/187350850-f2619390-ad71-4155-bd89-7f15f53cdf81.jpg)

7.![Toasts Error](https://user-images.githubusercontent.com/88729876/187350990-08d35a1e-13ee-4f8b-9aef-730d00071cbb.jpg)

Several issues have been discovered with the reviews and quotes pages but since they do not hinder the overall functionality of the site the issues will be adressed at  later stage.



# 7. Deployment #

This project was produced in GitPod and is deployed on Heroku. This is how to make a copy of this project and deploy it accordingly. The images are hosted on AWS, so you will need to sign up for a AWS account in order to get an API key. I opted to use a gmail account, the settings for which are in the settings.py file. The payment system used is Stripe, which you will need to set up an account for in order to collect the PUBLIC_KEY, PRIVATE_KEY and WebHook keys.

To set it up locally
1 - download the repository using the link at the top of the page, alternatively you can clone it using the following command:

git clone [https://github.com/LeVlad/](https://github.com/LeVlad/StoicShirts)

2 - Set up a virtual environment:

py -m venv venv
3 - Activate the virtual environment:

venv\Scripts\activate
Create a project by entering the command:
django-admin startproject YOURPROJECTNAMEHERE

Create a new app by entering the comand:
py manage.py startapp YOURAPPNAMEHERE

You are now ready to install the packages required to run this program. You can do this by installing the requirements in the requirements.txt file:

pip install -r requirements.txt
Next we need to add the following to the list of installed apps in settings.py:

-'cloudinary_storage',
-'crispy_forms',
-'allauth',
-'allauth.account',
-'allauth.socialaccount',
-'django.contrib.staticfiles',
-'django_countries',
-'home',
-'bag',
-'checkout',
-'profiles',
-'contact',
-'**yourappname**'

You will need to create an env.py file which will contain the following:

os.environ["DATABASE_URL"] = "your postgresql url which you will find in heroku (see below)"
os.environ["SECRET_KEY"] = "your secret key which will added to heroku"
os.environ["CLOUDINARY_URL"] = "your cloudinary api"

# Setting up email server #
In order to send emails (such as user confirmation) you will need to configure an email. I have used gmail and followed the guidelines as stated here:
https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/39dfbd4ba6ac42168b5df88d69c32f02/?child=first


# Setting up on Heroku: # 
1 - Set up a (or log into an existing) Heroku account.

2 - Select add new app and give it a unique name

3 - Select 'Resources' and search for/install the Heroku Postgres add-on.

4 - Select 'Settings' and click 'Reveal Convig Vars'

5 - You will find the DATABASE URL already added, copy this to the env.py file mentioned previously.

6 - You will need the following convig vars:

CLOUDINARY_URL = your API url from cloudinary
SECRET_KEY = your secret key must match the secret key in your `env.py` file
EMAIL_HOST_USER = your chosen email account's address
EMAIL_HOST_PASS = your chosen emaiil account's password or dedicated access key
STRIPE_PUBLIC_KEY = which you will find from your stripe dashboard
STRIPE_SECRET_KEY = which you will find from your stripe dashboard
STRIPE_WH_SECRET = which you will find from your stripe dashboard

# Migrate and Run in Gitpod #

Finally, all that remains is to makemigration by entering the following command:

python3 manage.py makemigrations
Then migrate using the following:

python3 manage.py migrate
And run the app locally:

python3 manage.py runserver


# 8.Credits #

# References #

1. https://docs.djangoproject.com/en/4.1/d
2. https://stackoverflow.com/
3. [https://github.com/ckz8780](https://github.com/ckz8780/boutique_ado_v1)
4. https://getbootstrap.com/
5. https://www.w3schools.com/

## Content ##

Background image logo ![BG-Shirt](https://user-images.githubusercontent.com/88729876/187344817-ccd33ec4-e79f-42f3-ba9a-9971db3eae75.png)

Fonts Used - Google Fonts

Lato - https://fonts.google.com/specimen/Lato
Roboto - https://fonts.google.com/specimen/Roboto

### Quotes ###
1. https://wisdomquotes.com/stoic-quotes/  - quotes
2. https://www.brainyquote.com/authors/immanuel-kant-quotes  - Kant
3. https://yourstory.com/2017/03/29-quotes-by-plato/amp - Plato 
4. https://www.brainyquote.com/authors/arthur-schopenhauer-quotes  - Schopenhauer
5. https://quotes.thefamouspeople.com/plato-257.php - Plato
6. https://www.goodreads.com/author/quotes/17212.Marcus_Aurelius

### Media ###
The shirt templates have been downloaded from https://www.vecteezy.com/


# Acknowledgements #
1. My mentor, Richard Wells, without who I wouldn't have had a fighting chance. He has helped, supported and incouraged me all along the way. I truly wish every mentor/teacher were more like him.



