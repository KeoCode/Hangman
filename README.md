# Hangman Game

A classic Hangman game written in Python and played on a terminal based window. 

![AmIResponsive](assets/images/amIResponsive.png)

This simple game has the standard rules of hangman, there is  secret word that only reveals the length of the word through underscores to represent a letter. You have 6 guesses to guess a letter or a word before you run out of lives.

The random word is choosen from a google spreadsheet that has over 850 nouns to choose from for multiple game plays before it would repeat any words. 

### User Experience

The purpose of the game is a simple word game for entertainment purposes in a termminal environment using Python. 

The site is designed with user experience in mind: 

- User wants to enjoy playing word game.
- User wants to win the game and get winning message when it is achieved
- User wants to have clear feedback for their action
- Provides clear error messages to help the user input the correct values expected

### Existing Features

- __Introduction section__

  - Once the game runs it starts with Hangman graphic and welcomes the user to the game and asks the user for their name. It will welcome them by username that was entered and advise the user they have 6 chances to guess the right word.  It will then ask them to press the enter key when they are ready to begin the game.

  ![Introduction](/assets/images/introScreen.png)

- __The Game Play section__

This is the main section of the game, where is picks a random word from the spreadsheet of words and display the length of the word with underscores. It will display how many lives are left and any letters or words already guessed. It will also display clear error mesages for any incorrect or duplicate data entered to increase user friendly play.
It the then displays a winner or loser message depending on the outcome.

![Game Play Section](/assets/images/startGame.png)

- __The Replay section__

  - This function asks the user at the end of the game if they would like to.

  ![Replay](/assets/images/winner.png)

  __The Scoreboard__

  - Once finished playing you final score is added to the scoreboard on my google spreadsheet. You win 10 points for every win and lose 10 points for every loss.

![Scores](/assets/images//scoreboard.png)

### Testing 

- Tested the code in the Code Institute Heroku terminal and also the terminal inside of Gitpod.
Checked that symbols, numbers or empty spaces will come up as invalid guesses when guessing the word.

![Error Handling - Repeating letters](/assets/images/sameLetter.png)

![Error Handling - entering invalid value eg number or symbol](/assets/images/valueError.png)

![Error Handling - adding more then one letter or not the amount that match the word](/assets/images/moreLetters.png)

- No errors showing on gitpod terminal after installing pycodestyle due to PEP8 website being down.

- One set of warnings showing as i have used a global variable for my scoreboard. Is a known problem as advised by Student Tutoring and shown on web searches such as [HERE](https://stackoverflow.com/questions/14503973/python-global-keyword-vs-pylint-w0603/14505529#14505529)

![Warnings on Gitpod](/assets/images/gitpodErrors.png)

### Bugs encountered
- Once i had gotten the word from the googlespread sheet and a random word had been chosen, i had trouble iterating through it. i googled for possible solutions and watched several youtube videos but ended up contacting student support for help as couldnot figure it ou myself. I then learned abouts string.punctuation method to remove the square brackets and qoutes that were coming from my googlesheet.

- Had trouble figuring out why my game was not recognising once the word had been completed and did not display the 'You win' message but my mentor helped my figure it out by showing me how to use the debugger and realised i need to change the is keyword to == as they were the same but just not in the same place stored in memory.

- As seen in the testing section, can not remove the warning due to using a global variable in my code. Advised by Student Tutoring this a programming decision and is not an error.

### Technologies and Languages, Frameworks & Libraries

- Python3

- Random is used to display a random choice from the list.

- Gspread (Googlesheets) is used  to link to an online spreadsheet app that lets you create and format spreadsheets that you can use work along side websites and programs.

- The Code Institute's GitHub full template for Python is used in order for the program to display properly in the deployed site on Heroku.

- Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- GitHub is used to store the projects code after being pushed from Git.

- Heroku is used to build, run and scale applications in a similar manner across most languages.

### Deployment

- Go to the Heroku Dashboard.
- Click New.
- Select to create a new app.
- Add Config Var's for Creds and Port
- Set the buildbacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy.
 
### Credits 

- Watched a few videos on how to implement desired functions on [Youtube](www.youtube.com)
- My Mentor for ideas and help when strugglng with parts of my code.
- Slack community esp the learn python channel.
- Student support and tutoring for helping me figure out an issue with bringing my word from googlesheets and iterating through it. Also my use of keyeords verses operators.

### Content 

- Code institute for the sample READ.md for layout
- W3 school online and stackoverflow for general ways to implament Navigation bar and style in css
- How to implement some functions or keywords correctly from [YouTube](https://www.youtube.com/watch?v=x0VcigW9kN0&ab_channel=OpenJavaScript)


### Media

 - [ASCII Art](http://patorjk.com/software/taag/) for title was created on this site.