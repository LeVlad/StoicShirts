# StoicShirts22

A Django created e-commerce site for selling shirts with stoic quotations on them.

# Table of Contents #

1. Design  
1.1. Bussiness Model  
1.2. Market Research
1.3. Facebook Marketing  
2. User Stories
3. Functionality
4. Technologies Used
5. Tests  
5.1. Lighthouse  
5.2  CSS Validator  
5.3. HTML Validator  
6. Errors and Fixes  
6.1 Issues  
7. Deployment  
8. Credits  



# 1. Design #

The site is made up of 7 page options displayed on a horizontal navbar:  
 - Home  
 
 ![image](https://user-images.githubusercontent.com/88729876/192626316-9f69db30-0201-406f-a5e3-7b81e053f852.png)

 - Products can be sorted by price, rating, category and philosopher or all can be selected  
 
 ![image](https://user-images.githubusercontent.com/88729876/192626404-7386cf43-a741-434d-9d08-f9f0b80eb0f5.png)

 - Categories can be sorted by every category available or all can be selected  
 
 ![image](https://user-images.githubusercontent.com/88729876/192626544-6856c3f4-7bd7-445f-b21c-8c0dfa275724.png)

 - Philosophers can be sorted by 5 philosophers  
 
 ![image](https://user-images.githubusercontent.com/88729876/192626680-8492b7f1-22e3-496d-8097-543fca3da758.png)

 - Contact Us  
 
 ![image](https://user-images.githubusercontent.com/88729876/192626728-bdd41497-02e4-4e02-a335-23cc9159ae9b.png)

 - Subscribe  
 
 ![image](https://user-images.githubusercontent.com/88729876/192627056-140de4d9-f3dd-47d5-92a4-0c9448611efb.png)

 - My Account has a dropdown of two options "Register" or "Login" and once logged in the user can navigate to the profile page 
 
 ![image](https://user-images.githubusercontent.com/88729876/192627274-2634acfa-01e5-4c13-a0e0-0fcce016a7c3.png)


The initial design of StoicShirts was meant to be slightly different as I wanted to have the navbar spread out  in the 4 corners of the page and in the middle would sit the shirt logo.

## 1.1. Business Model ##

The selected business model for StoicShirts22 is a B2C model in which direct contact can be made by the customer through the website and purchase the offered products.

The delivery framework used to satisfy customer requests is the drop-shipping type where the customers order the products that we upload from our manufacturers but the stocking, delivering and standards upkeep will rely on third parties which is why the customer service department will be set-up so as any order can be tracked, if delivered damaged, will be replaced and rewards offered to multiple purchasess (i.e. massive price drop and extra products added as bonus to free delivery)


## 1.2  Market Research ##

During the research for the business model or idea I found that the keywords "stoic" and "quotes" were very sought after and had high organic values especially in the United States.  

![Keyword Search](https://user-images.githubusercontent.com/88729876/187352948-2fc48b72-edda-4383-b25f-0c8d6ddde93c.jpg)  

After researching some related keywords have found that the most trending combination relating to philosophers and shirt were a mix of “seneca “, “plato “, "quotes" and "shirts".  

![seneca worldwide trends 2](https://user-images.githubusercontent.com/88729876/192107676-8e272ad7-5c5f-4ecc-baf9-6bc58846cf16.jpg)  

![stoic google trends](https://user-images.githubusercontent.com/88729876/192107699-da41d5bf-d57e-4783-a22f-1450cbd51165.jpg)  

![shirts google trends 2](https://user-images.githubusercontent.com/88729876/192107682-685380ad-e4e0-4b7b-8b14-1562c0fa4aeb.jpg)  

Compared to the rest of the keywords,“seneca” had a massive increase combined with other keyword searches and ”plato” as well saw a great increase over the last 5 years. Seeing this upward trend I decided once finished I would use google’s keyword planner to see what would be the site’s potential. 

Using Google’s Forecast option we can see that an average of £600+ could be made only using advertisements strategically placed on the site.  
![image](https://user-images.githubusercontent.com/88729876/192110241-ae66320c-4a07-4647-92b8-6809111e965d.png)

## 1.3. Facebook Marketing ##

![StoicShirts22 Facebook Mock-up](https://user-images.githubusercontent.com/88729876/192624908-82fb6c37-063e-457b-a09c-8d4fc6cba1f5.png)


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

---

# 5. Tests # 

I have not undertaken any automated testing and I chose to manually test the site functionality and layout.

Idea 💡: After creating all the templates I wanted to ensure their linkeage and functionality

Test 📝: To test this, I went through each and made sure they were loading correctly.

Result 👷: All templates loaded as expected in development.

Verdict ✅: This test has passed.

---

Idea 💡: Once the functionality of the sign up and login were done I wanted to test and see if they work correctly.

Test 📝: To test this, I went through using a different device, created an account and managed to access the rest of the pages.

Result 👷: Everything worked as expected.

Verdict ✅: This test passed and the design is more appealing than the standard allauth template.

---

Idea 💡: A good UX experience is given by interactions with the pages on a website, that's why messages have been implemented in the site.

Test 📝: Testing has been done by confirming every action that should send a message, is doing so.

Result 👷: Users are receiving success messages for loggin in and out and error messages for incorrect forms.

Verdict ✅: This test passed and no further corrections are required.

---

Idea 💡: Correct functionality of the contact form and subscribe

Test 📝: To test this I have filled in the forms and confirmation is received in the console while in Gitpod but also via e-mail while in production.

Result 👷: Users are receiving success messages for successfully using the contact form and the subscribe option.

Verdict ✅: This test passed and no further corrections are required.

---

## 5.1. Lighthouse ##

## Initial report ##  
![lighthouse report 1](https://user-images.githubusercontent.com/88729876/187338471-b0c96dda-e5bc-49eb-8bd6-1dda2c7ef462.png)

## Follow up report ##  
![image](https://user-images.githubusercontent.com/88729876/192377526-c3415f3d-1797-4b04-85b7-1756df08820f.png)




## 5.2. CSS VALIDATOR WCS ##  

![CSS Validator](https://user-images.githubusercontent.com/88729876/187345959-a0da1462-1700-4a19-b498-94592c3bc291.jpg)

## 5.3. HTML VALIDATOR WCS ## 

![image](https://user-images.githubusercontent.com/88729876/192369549-f8a9a62b-060e-4d9a-b3eb-983d33112a73.png)

# 6. Issues & Fixes # 

## 6.1. Issues ##

Issue 🐛: Add to bag error.  
Cause🔧: Missing "k" in pk= definition.  
Resolution✅: Added missing letter resolved the issue.  

1.![add to bag toast issue](https://user-images.githubusercontent.com/88729876/187349166-6b37069e-f7ae-489f-b7d7-45172f8957c1.jpg)

---

Issue 🐛:  Crispy Field error  
Cause🔧: as_crispy_field got passed an invalid or inexistent field.  
Resolution✅: Added missing letter.  
2.![Crispy Error Checkout](https://user-images.githubusercontent.com/88729876/187349134-4be3f25e-49ad-433a-8a11-6ef83c5a9470.jpg)

---

Issue 🐛: Deleting product error get_object_or_404.  
Cause🔧: Function used instead of parameter ("request").  
Resolution✅: Replaced function with "Product" parameter.  

3.![deleting error 1 2](https://user-images.githubusercontent.com/88729876/187349234-02c9ebe4-a3d0-444b-bf48-d9aad6d419bb.jpg)
  
---
  

Issue 🐛:   No image media in settings.py.  
Cause🔧: No module named "django.template.context.processor".  
Resolution✅: Added missing "s" for "processors".  

4.![no image media settings py missing s](https://user-images.githubusercontent.com/88729876/187350865-af1bff04-f6b1-4e87-9fa5-38f778e23334.jpg)

---
  
Issue 🐛:Contact Us page not working.  
Cause🔧: "Contact.html template does not exist".  
Resolution✅: added better view description and url linking.  


5.![Dev Contact Us](https://user-images.githubusercontent.com/88729876/187350816-352ffa7d-c5a6-4df1-a93e-b27fd55e3f8f.jpg)

  
---
  

Issue 🐛: Subscribe page not working.  
Cause🔧: Template does not exist.  
Resolution✅: Added correct urls in contact/ urls.py.  

6.![Subscribe 2](https://user-images.githubusercontent.com/88729876/187350850-f2619390-ad71-4155-bd89-7f15f53cdf81.jpg)
  
---
  

Issue 🐛: Toast Error.  
Cause🔧: TemplateSyntaxError.  
Resolution✅: Corrected template name typo.  

7.![Toasts Error](https://user-images.githubusercontent.com/88729876/187350990-08d35a1e-13ee-4f8b-9aef-730d00071cbb.jpg)


---

Issue 🐛:  Contact Form/ Sign Up page display 500 error page although filled in successfully.  
Cause🔧: USER_ACCOUNT_PASSWORD variable typo in Heroku Config Vars.  
Resolution✅: Added correct variable name and everything working fine.  

8. ![image](https://user-images.githubusercontent.com/88729876/192164888-d3105146-bc89-426d-8046-11c2acaca0bb.png)
  

---


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
2. My family for putting up with me during the long annoying nights



