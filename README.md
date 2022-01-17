# Ensemble Full-Stack Project
Author: Brad Edwards
Email: j.bradley.edwards@gmail.com
Github: 
License: MIT

First of all, thank you for the opportunity to do this project for Ensemble Systems. And thank you
even more for taking the taking to review it.

## Back End - Python, django

The back end was implemented in Python using django to take advantage of its excellent CRUD support, 
speed of implementation, and ease of implementing REST APIs. I also chose it because I have done 
a few personal and school projects in Python. I considered ASP.NET, my other go to, and Ruby on Rails,
but I find ASP.NET takes time and I would be learning Ruby from the ground up. So they made less sense
given my time constraints.

The implementation meets the project requirements, but needs further work. Given a range of time 
constraints, I focused on demonstrating I was aware of certain requirements, technologies, or 
practices, even if they were not fully implemented. If I were to spend more time on this project I 
would focus on the following:

1. Unit testing is not sufficient. I have demonstrated how testing works in the application, however 
coverage is insufficient in the back end.

2. Input validation and security. The database engine does a good job of sanitizing inputs to avoid 
SQL injection attacks. However there is insufficient up front validation, cleaning, and interpretation. 
For instance, if a user puts in a long date string such as 2000-01-01 the application should slice out 
the date and carry on rather than returning an error.

3. Security. CORS headers are in place and currently limit access to the client application on a specific 
port. However, request rate limiting, JWT token based or other authentication for CRUD API access, and 
moving the django admin url to a long randomized string are all low-hanging security fruit.

4. Pre-commit, Flake8, Black. Linters and static code analysis would help validate code prior to commits 
to improve code quality, readability, and avoid certain errors.

For the sake of file size and saving the poor folks at OMDB API excessive requests, I skimmed a few results 
from them to seed the test database. The backend/management/commands/getmovies.py file runs through all 
three-letter permutations of the alphabet and queries OMDB API for up to 5 movie titles that match. A 
production ETL pipeline would need a lot more work for robustness and completeness. However, removing the 
rate limit in getmovies.py would result in the script eventually scraping the entire database. So it is a
good start. For a production application, I would probably implement a Strategy pattern to abstract out 
parsing for a particular source since we might want to ingest data from sources in addition to OMDB API.

Of note: OMDB API now requires Patreon subscriptions to get access to poster data.

## Front End - JavaScript, Vue.js, Axios

The front end was implemented in Vue.js as it was one of the available options in the requirements. I have
done some personal project work in Vue.js before and there are a lot of examples online for working with 
Vue.js and django, so it was a natural fit.

Front end work is literally never done. There are always more refinements and tweaks that could be added.
 That said, some are particularly important to note:

 1. Unit testing. Balancing other take home project assessments, I did not have time to do this project the 
 way I do my own and school projects; test first. The front end has no unit test coverage, and that would 
 obviously not be acceptable for a professional project.

 2. Input validation. Handling much of the user input validation on the front end speeds up time to response 
 for the user and limits hits on the servers for the project client. Most of the input validation can and 
 should be in the Vue components that expose inputs to the user.

## Other Improvements

1. Integration testing. This would be important to ensure the front and back ends work together smoothly. 
It is easy enough to write tests one thinks are accurate to the other system that turn out not to 
be in practice. And easy enough for something to break after later updates. Perhaps this could be part of a 
CI/CD pipeline.

2. Mobile client. This project could benefit from also having a mobile application. Responsive styling only 
goes so far and there might be all kinds of personalization or added features that would make sense for mobile
users. In any event, I have used Xamarin for an iOS application as a school project and I am confident I could
get up to speed for native, React Native, or Flutter development.

# Thanks Again

Once again, I appreciate you taking the time to review this project. I hope to speak with you and your team soon.

All the best,
Brad
