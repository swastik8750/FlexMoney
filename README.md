# FlexMoney
Yoga Classes Assignement for joining as SDE intern

# Problem Statement: 📃
Assume that you are the CTO for the outsourcing firm which has been chosen to build an
admission form for the Yoga Classes which happen every month.
Requirements for the admission form are:

- Only people within the age limit of 18-65 can enroll for the monthly classes and they will
be paying the fees on a month on month basis. I.e. an individual will have to pay the fees
every month and he can pay it any time of the month.
- They can enroll any day but they will have to pay for the entire month. The monthly fee is
500/- Rs INR.
- There are a total of 4 batches a day namely 6-7AM, 7-8AM, 8-9AM and 5-6PM. The
participants can choose any batch in a month and can move to any other batch next
month. I.e. participants can shift from one batch to another in different months but in
same month they need to be in same batch

# Tech Stack 🧑‍💻
- Django is used for backend.
- SQLite used for database.
- Basic HTML and CSS for page designing.
- Pythonanywhere is used to Host it.


# My Approach 🎯💡
 I have created the login system and providing the flexibility to the user for enrolling for the upcoming batches.
 
 
 I have used 3 pages for login, signup, and dashboard where User can see the enrolled batches(The list of upcoming batches user is enrolled) with the flexibilty to enroll in other batch within the dashboard.
 **Login:**
  |-------------------------------------------------------------------------------------------|
<kbd> ![Signin-page](https://user-images.githubusercontent.com/78960121/207646710-7ca985f9-af1e-47b5-ac2b-2bf87d32d4ce.png)</kbd>
 |-------------------------------------------------------------------------------------------|
 **Signup:**
  |-------------------------------------------------------------------------------------------|
 <kbd>![signup-page](https://user-images.githubusercontent.com/78960121/207646758-ef20eb6e-a7e7-41e5-b0ea-22b1243dfa2e.png)</kbd>
 |-------------------------------------------------------------------------------------------|

 **Dashboard with list and new batch enroll: **
  |-------------------------------------------------------------------------------------------|
 <kbd>![dashboard-page](https://user-images.githubusercontent.com/78960121/207646735-de7b6190-7a9f-4479-aa7a-3310bc9ca4c0.png)</kbd>
 |-------------------------------------------------------------------------------------------|
 
 #ER Diagram and Database Scheme:
 
 **ER Diagram:**
  |-------------------------------------------------------------------------------------------|
 <kbd>![ER_FLEX drawio](https://user-images.githubusercontent.com/78960121/207646638-817f77de-158e-4125-a58f-68141566e2c7.png)</kbd>
  |-------------------------------------------------------------------------------------------|

 **Database Diagram:**
  |-------------------------------------------------------------------------------------------|
  <kbd>![Tables drawio](https://user-images.githubusercontent.com/78960121/207649966-f0b93d41-e3d4-4d3c-8ad1-0e74c9f3a669.png)</kbd>
   |-------------------------------------------------------------------------------------------|

  ```User (
  username VARCHAR(255) PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  dob DATE NOT NULL
);
```
```
Batch (
user User FOREIGN KEY,
batchVARCHAR(255) NOT NULL,
month DATE NOT NULL
);
 ```
 #How to run
 
 -Clone the Repo:
 ```
 git clone https://github.com/swastik8750/FlexMoney.git
 ```
 -Jump to the project:
 ```
 cd FlexMoney
 ```
 -Install the Requirements:
 ```
 pip install -r requirements.txt
 ```
 - Run the Server:
 ```
 python manage.py runserver
 ```
 
  
 
 
 
