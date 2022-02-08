# Overview

This program interfaces with a Google Firebase Firestore to interact with stored information. The user will be able to add, delete, modify, and query for data.

I wanted to simply practice connecting with a cloud database and interacting with it through a program. I chose to use a Minecraft server I've been playing on for a while for information context. It is by no means accurate and I intend for it to stay that way, for privacy of course. 

The user will be able to view which players are in the database (server) and see small pieces of information related to each player. The user will also be able to add new players or delete old ones. On the chance that information is entered incorrectly or becomes outdated there is an option to modify existing user information.

[Firebase Tutorial/Demo Video](https://youtu.be/t5K6fRkKXx4)

# Cloud Database

I used Google Firebase as my cloud database platform.

I ended up using the Firestore Database instead of the Realtime Database. The Firestore Database is a NoSQL, document-oriented database.

As far as how the data in this data base is stored, it is only using one collection with 4 fields per document.

The collection is the Users. Each document and it's fields correspond with each distinct user.

# Development Environment

* Python 3.8.12
* firebase_admin Library
* Firebase Firestore Database
* Git/GitHub
* VS Code

# Useful Websites

* [Google Firebase Webpage](https://firebase.google.com)
* [Official Firebase Set Up Tutorial](https://firebase.google.com/docs/firestore/quickstart)
* [Firebase Admin Library Documentation](https://firebase.google.com/docs/reference/admin/python/firebase_admin)

# Future Work

* Add a Collection to provide information that corresponds to the separate regions found within the Minecraft server.
* I wanted to make use of the PyInquirer Library to make the UI/UX more intuitive.
* Modify outputs to make options easier to understand and use.
