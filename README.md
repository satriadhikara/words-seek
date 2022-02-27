# **Words Seek**

Hi! My name is Satriadhikara Panji Yudhistira

I'm from Jakarta, Indonesia

And this is my final project for CS50

## **About the project**

---

A simple game web application game for CS50 final project

Video demo: [words seek demo](https://youtu.be/8wXEmdhGL7M)
(sorry for my bad english)

## **Build With**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Sqlite](https://www.sqlite.org/index.html)
- [Bootsrap](https://getbootstrap.com/)

## **Requirement**

You need to install this requirement

- flask

```
$ pip install Flask
```

- sqlite

```
$ sudo apt install sqlite3
```

## **Getting Started**

---

### **How to play**

You will get a key that is 2 characters
And then you must answer it with word that contains the key that you get within 5 seconds

**Example**

You got a key that is **ED**, then you can answer it with ti**ED** / w**ED**nesday / **ED**ucation

- Note: If you answer with word that contains the key but not side by side r**E**a**D** then its FALSE

### **Contains**

This project contains:

#### **README.md**

this is what you saw right now

#### **requirement.txt**

this text file contains the requirements of the web application

#### **app.py**

This file contains the backends of the web application

- Libraries

  - string
    > This library is for generating string
  - random
    > This library is for randomizing the string to 2 characters that will be the key
  - sqlite3
    > This library is for access or connect to the database (I renamed it to just "sql" for simplicty in code)
  - flask
    > This library is for creating the routes, rendering the templates, and for requesting name from templates file

- Global Variables

  `home = True`

  > a boolian variable for showing the home nav icon

- Functions
  `get_key()`

  > This function returns randomized key that contains word from dictionary database

- Routes

  - `/`

    > this route is for rendering the homepage (index.html)

  - `/help`

    > this route is for rendering the help page (help.html)

  - `/play`

    > this route is for rendering the play page (play.html) and has two methods

    - POST

      > this methods request answer and key from play.html and connect to database for checking if the answer is a word that contains the key and if the checking is right then returns render success.html and return render failure.html if its flase

    - GET

      > this method is calling get_key function to generate the key returns render play.html for user to play the game

  - `/success`

    > this route returns render success.html for succeeding the user because the answer is right

  - `/failed`

    > this route returns render failed.html because the answer is wrong

#### **EDMTDictionary.db**

This database from [@eddydn](https://github.com/eddydn/DictionaryDatabase) its contains words from dictionary

#### **/static folder**

This folder contains the static file

- styles.css
  > this file is the stylesheet of the web application

#### **/templates folder**

This folder contains the templates that will be rendered in app.py

- index.html

  > This file contains the home page of the web app

- play.html

  > This file contains the page that user plays the game, there is a timer with progress bar, and a key (2 alphabet) that must be contains in the answer, theres an input field that user can type the answer, and lastly theres an input button

- help.html

  > This file contains the guide that tell user how to play the game

- result.html

  > This file contins the result of the game, output "succeeded" if right and "failed" if wrong

## **Contact**

---

satriadhikara - [@satriadhikara](https://twitter.com/satriadhikara) - [satriadhikara@gmail.com](mailto:satriadhikara@gmail.com)

Project link: [words-seek](https://github.com/satriadhikara/words-seek.git)
