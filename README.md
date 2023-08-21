# MAgPIE Movies
#### Video Demo:  [YouTube Demo](https://youtu.be/aWiMzbAd4l0)
#### Description: Hello Wolrd from kenya.:kenya: For my CS50 Web-development final project, I made a responsive movie review website that gets live data from [IMDB](https://www.imdb.com) using [PyMovieDb](https://github.com/itsmehemant7/PyMovieDb) API and displays it in a pleasing format. There is a secured login system in place.

### Distinctiveness and Complexity:
This  project is purely distinct from any other project previously submitted in `CS50W` and `CS50X` including `social network` from project 4 `e-commerce` from project 2.
MAgPIE movies makes use of the user authentication provided by Django and one more model, `Watchlist` to give its users the bestg experience. 
Searching for movies and saving/deleting a movie from the watchlist is done entirely through javascript fetch.
The Web applistion is responsive to differnt screen sizes and the contents are perfectly framed for the best user experince.

### Languages used:
  - Pyhthon
  - python -> Django
  - JavaScript
  - jQuery
  - HTML/CSS

### Resources:
  - [PyMovieDb](https://github.com/itsmehemant7/PyMovieDb) is a python wrapper to represent the [IMDB](https://www.imdb.com) API. It helps you to get files i.e.   Movies/TV-Series information from IMDB by scraping.
  - [Boxicons](https://boxicons.com/)
  - [Bootstrap](https://getbootstrap.com/)
  - [jQuery](https://jquery.com)
  - [jQuery DataTables](https://datatables.net/)

### Instalation packages
    * Python3
    * pip install PyMovieDb
    * pip install requests-html

## Files
  ### - index.html
  Displays Featured movie, top 50 popular movies and TV-series and also upcoming movies.
  ### - layout.html
  basic page layout with the navbar and the search results section.
  ### - list.html
  If the user is logged in, it will display all the movies in their watchlist.
  ### - movie.html
  Page for viewing a movie's information from its id.
  ### - person.html
  Page for viewing a person's information from their id.
  ### - register.html
  Page for creating new user.
  ### - scripts.js
  Used for some functions like adding a movie to watchlist or searching without refreshing the page.
  ### - styles.css
  Used for styling the website.

## Notes:
 Default Admin-> name: `admin` password: `1234` email: `admin@admin.com`.
 
#### Running the website:
 
  - :arrow_right: Make sure you have the required packages listed installed.
  - Direct to the folder containing manage.py
  - in your terminal, run `python3 manage.py runserver`
         

#### Conclusion:
This was an exciting project to work on. I have learned a lot in this course to help me  in programming and would wish to continue with other CS50 courses in future.


**My name Hugh Herschell and this was CS50’s Web Programming with Python and JavaScript**
