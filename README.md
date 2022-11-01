# Hangman Game

A classic Hangman game written in Python and played on a terminal based window. 

![AmIResponsive](assets/images/)

This simple game has the standard rules of hangman, there is  secret word that only reveals the length of the word through underscores to represent a letter. You have 6 guesses to guess a letter or a word before you run out of lives.

The random word is choosen from a google spreadsheet that has over 850 nouns to choose from for multiple game plays before it would repeat any words. 

![Screenshot of Main PAge](/assets/images/)

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

  ![Introduction](/assets/images/)

- __The Game Play section__

This is the main section of the game, where is picks a random word from the spreadsheet of words and display the length of the word with underscores. It will display how many lives are left and any letters or words already guessed. It will also display clear error mesages for any incorrect or duplicate data entered to increase user friendly play.
It the then displays a winner or loser message depending on the outcome.

![Game Play Section](/assets/images/)

- __The Replay section__

  - This function asks the user at the end of the game if they would like to

![Main Image](/assets/images/imgshot.png)

- __The Form Area__

  - This section is where the user input their data and submit it so it will run the calculations just before being redirected to the results page.

![Form Section](/assets/images/formshot.png)

- __The Footer Area__

  - Basic Footer with a disclaimer to consult a doctor for any health decisions.

  ![Footer Section](/assets/images/footer.png)

- __The result page__

- The user will be redirected to the results page and using session storage, it will display the results of the calculations.

![Result Page](/assets/images/resultspage.png)

- __The Results explained Area__

  - A break down of what each result means and is explained so can action with the results.

  ![Result info Text](/assets/images/resultInfo.png)

## Testing 

- I Have added all Form fields as a requirement as all data is needed to make accurate calculations, I also have added a minimum length and a max length to certain fields to ensure it will validate that the correct data is entered inte right field.

- I had commented out the console log's in my code but i reguarly use the to double check the formula's are correct.

- The Screen is responsive as can be seen here in the AmIREsponsive screen shots on all tested devices.

![AmIResponsive](assets/images/responsiveshot.png)

- In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.



### Validator Testing 

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-maths%2F)

    ![HTML Validation](/assets/images/html-validator-screenshot.png)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-maths%252F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Validation](/assets/images/css-validator-screenshot.png)

- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)

![Javascript Validation](/assets/images/jshint-screenshot.png)

- Lighthouse Accessibility testing

![Lighthouse results](/assets/images/lighthouse-screenshot.png)

## Deployment

- Steps used to deploy on Github through Pages section

![Screen shot of the github pages to deploy page](/assets/images/deployone.png)
![Screen shot of the github once deployed](/assets/images/deploy-two.png)
 
## Credits 

### Content 

        * The text for the Home page was taken from [Steelfit](https://steelfitusa.com/blogs/health-and-wellness/calculate-tdee)
        * Text used in read me and result page from [Macro Article](https://www.womenshealthmag.com/uk/food/weight-loss/a706111/counting-calculate-macros/)
        * Code institute for the sample READ.md for layout
        * W3 school online and stackoverflow for general ways to implament Navigation bar and style in css
        * How to implement Session Storage from [YouTube](https://www.youtube.com/watch?v=x0VcigW9kN0&ab_channel=OpenJavaScript)


### Media

        * photos from [Pexels](https://www.pexels.com/)
        * font from [Googlefonts](https.//www.googlefonts.com)
        * favicon from [icons8](https://icons8.com/icons/set/html-favicon)