# CosmoCompatibility

The Cosmic Compatibility test is a Python application that consists of a 10-question multiple-choice test, providing a personalized testing experience based on astrological signs. The program was designed to offer users a journey of knowledge and entertainment, allowing exploration of the distinctive characteristics associated with the zodiac signs.

![CosmoCompatibility shown on a range of devices](/assets/images/docs/)  

## Demo
The live demo is available [here]()!

## Contents

* [User Experience](#user-experience)
  * [Program Overview](#program-overview)
  * [User base](#user-base)
  * [Project Goals](#project-goals)
  * [Flowchart](#flowchart)

* [Features](#features)
  * [General Features](#features)
  * [Features and resources to be added in the future](#features-and-resources-to-be-added-in-the-future)

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Validator Testing](#validator-testing)
  * [Bugs](#bugs)

* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
  * [Python Packages](#python-packages)

* [Deployment](#deployment)

* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

### Program Overview 

CosmicCompatibility test is an original application that immerses users in the universe of zodiac signs and their personality traits. This experience provides an interactive view, encouraging participants to delve into the rich mythology underlying the zodiac signs.

![Solved bug - naming conflict](/assets/docs/mockup.png)

### User base

* Interested in Astrology: Individuals curious about astrology and zodiac signs.

* Seekers of Self-awareness: Individuals looking to better understand their characteristics in relation to zodiac signs.

* Personality Test Enthusiasts: Those who enjoy participating in interactive tests.


### Project Goals  

* Engagement in Interactive Exploration: Provide an interactive platform for users to have an enjoyable and enlightening understanding of the topic.

* Awaken Curiosity: Stimulate users' curiosity and interest in the universe of astrology and its influence on personality traits.

* Foster Self-Discovery: Encourage users to embark on a journey of self-discovery, unveiling the connections between their personalities and zodiac signs.

* Cultivate an Engaging User Experience: Ensure that the design and functionalities of the program offer an attractive experience, capturing users' attention during interaction.

* Prioritize User-Friendly Interface: Ensure intuitive navigation and ease of use, allowing users to access information and interact with the program's features effortlessly.


## Flowchart

In the planning stage, I drafted a basic structure that depicted the desired functionality and interaction for the program.This outline aimed to facilitate the visualization of goals and the definition of the desired execution method.

As development progressed, I identified elements that needed to be included and others that required a different order of operation. These changes were gradually incorporated into the initial outline. The outline was conceived using the Lucidchart tool.

![Flowchart](/assets/docs/flow.png)  

## Features

The "Cosmo Compatibility" begins with an introductory screen, providing an explanation about the nature of the compatibility test. It then presents a user-friendly menu, offering four distinct choices. Users have the opportunity to deepen their understanding of the zodiac signs. Alternatively, they can initiate a 10-question multiple-choice test, aiming to assess, through a percentage bar, how compatible their personality traits are with the descriptions associated with their zodiac sign. Additionally, users can view the compatibility percentages from previous tests. From the main menu, users also have the convenience of concluding the program in a simple and conclusive manner. Through this elaborate interface, users have the freedom to navigate intuitively, customizing the experience to their preferences.

### Introduction

The program utilizes a website to generate stylized text in ASCII art format, presenting the program's name in a way that grabs attention. Just below, a brief explanation is provided to contextualize the purpose of the test. On the same screen, the main menu offers four clear options: explore the zodiac signs, start the test, view compatibility percentages, or exit the program
![Introduction -  opening screen](/assets/docs/initial-screen.png)

### Learn more about Zodiac Signs

Given that many people who will take the test may not be familiar with the subject, the first menu option was designed to provide an introduction to the user about what zodiac signs are. This aims to facilitate the user's participation in the test. At this stage of the program, we provide a broader understanding of the meaning of zodiac signs.
![menu -  option 1](/assets/docs/about-screen.png)

### Start the Compatibility Test

When the user clicks on option 2, they will initiate the test. To do this, the program will first collect the month and day of the user's birth in order to determine their zodiac sign.

![collect data](/assets/docs/test-1.png)

After collecting the data, the person's zodiac sign will be displayed on the screen, followed by instructions for the test.

![zodiac sign and instructions](/assets/docs/test-2.png)

Right after, on the same screen, the test starts with the first question. A total of 10 questions will be presented, each with 4 answer choices. Both the questions and answers are randomized. However, out of the 4 options, one will always be the correct answer, namely, the one that best aligns with the personality described for the person's zodiac sign.

![progress bar](/assets/docs/test-3.png)

#### Progress bar

The progress bar is a visual tool that provides an indication of the test's progress. It is displayed on the screen, just above the question, and shows the progress in terms of questions answered according to the personality description of your zodiac sign. The bar is updated with each user response. If the answer is correct, the bar advances; otherwise, it remains in the same position. The percentage displayed on the bar represents the progress percentage relative to the total number of questions. This feature helps keep the user informed about the test's status and provides an interactive and dynamic experience.

![progress bar](/assets/docs/progress-b.png)

###· Result screen

In the beginning, it displays the compatibility percentage determined by the individual in relation to their zodiac sign, accompanied by a message providing some insights about this result.

![result](/assets/docs/test-4-1.png)

Following that, a brief description of the main characteristics associated with your zodiac sign is presented, with the menu located just below for you to choose your next step.

![description zodiac sign](/assets/docs/test-4-2.png)

### Update the spreadsheet

At the end of the test, the program proceeds to update the data with the user's responses. This involves several key updates in the spreadsheet:

Sign Row: The row corresponding to the user's zodiac sign is updated:
* Column 2 (Number of Participants): This column is updated to reflect the total number of individuals who have taken the test.
* Column 3 (Number of Correct Answers): The number of correct answers is updated in this column.
* Column 4 (Average Percentage of Correct Answers): This column is updated with the average percentage of correct answers from the tests that have been completed.

![spreadsheet](/assets/docs/spreadsheet.png)

### View Compatibility Percentages

The third option in the menu provides users with the opportunity to explore the averages of tests previously taken by other users, based on the updated data from the spreadsheet. This information is visually presented through progress bars, offering a clear view of the compatibility percentages associated with each zodiac sign.

![spreadsheet](/assets/docs/statistics.png)

### Exit Program

The final option (4) in the menu is 'Exit Program,' which allows users to conclude the program. Upon selecting this option, the program terminates gracefully, displaying a closing message.

![spreadsheet](/assets/docs/exit.png)

## Features and resources to be added in the future

* Implement synchronized audio feedback in line with the progress of the accuracy bar.

* Adding more questions: Increase the number of question options in the test to make it more comprehensive.

* Implement a feedback feature at the end of the test that displays the answers marked as incorrect by the user, along with providing the response that aligns with the person's zodiac sign

## Testing 

### Manual Testing

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| **`Initial screen`** |
|  |  |  |  |  |
| ASCII art initial screen |  The test name created with ASCII art should appear correctly without distorting the format| Pressing the 'Run Program' button | The test name displays correctly | Pass |
| **`Menu`** |
|  |  |  |  |  |
| Option 1 | When selecting option 1, the program should redirect the user to the 'Learn more about Zodiac Signs' screen | Entering 1 as an option | The screen 'Learn more about Zodiac Signs' is displayed correctly | Pass |
| Option 2 | When selecting option 2, the program should redirect the user to the 'Start the Compatibility Test' screen | Entering 2 as an option | The screen 'Start the Compatibility Test' is displayed correctly | Pass |
| Option 3 | When selecting option 3, the program should redirect the user to the 'View Compatibility Percentages' screen | Entering 3 as an option | The screen 'View Compatibility Percentages' is displayed correctly | Pass |
| Option 4 | When selecting option 4, the program should redirect the user to the 'Exit program' screen and terminate the program | Entering 4 as an option | The screen 'Exit program' is displayed and terminate the program correctly | Pass |
| Invalid option | When an invalid number or character is entered, a valid input is required | Entering an invalid number or character | A valid input is required | Pass |
| **`Compatibility Test`** |
|  |  |  |  |  |
| Day and month input | At the beginning of the test, the user is prompted to enter their month and day of birth. With this data, the program will display the user's zodiac sign | Entering valid days and months multiple times | The program correctly identifies the person's zodiac sign based on the provided dates and initiates the test | Pass |
| Valid answer options | When the questions start, the program should provide 4 answer options, with one of them being the correct answer| Conducting the test with various zodiac signs and ensuring that the provided options always include the correct answer by comparing them with the data in data.py | The correct answer always appears as an option | Pass |
| Invalid choice | When an invalid number or character is entered, a valid input is required | Entering an invalid number or character | A valid input is required | Pass |
| **`Progress Bar`** |
|  |  |  |  |  |
| Progress Bar Display | The progress bar should be visible throughout the entire test and at the end of the test displaying the result | Answering test questions until the end | The progress bar is visible throughout the entire test | Pass |
| Correct answer | When the user selects the correct answer, the percentage and the progress bar increase by 10% | Choosing the option with the correct answer and pressing Enter | The percentage and the progress bar increase by 10% | Pass |
| Inorrect answer | When the user selects the incorrect answer, the percentage and the progress bar remain at the same value | Choosing the option with the incorrect answer and pressing Enter | The percentage and the progress bar remain at the same value | Pass |
| **`Worksheet`** |
|  |  |  |  |  |
| Data update | When the test is completed, the spreadsheet should be updated with the number of participants who have completed it, the number of correct answers, and the average compatibility percentage | Finishing the test and checking the updates | The spreadsheet was updated correctly | Pass |

### Validator Testing  

* Python PEP8 Validation:  

In order to ensure code quality, the program's code was validated and corrected using PEP 8.

![PEP8 Validation - Index](/assets/docs/pep8ci-1.png) 

The corrections were implemented in accordance with the validator's suggestions.

### Bugs

#### Solved Bugs

#### Correct Numbering of Answer Options

  * Bug Description:

  Even though the range of options was adjusted from 1 to 4, initially the options were still displayed from 0 to 3. After fixing this issue, a new complication arose. Although the options were displayed correctly from 1 to 4, the program still internally associated them as values from 0 to 3. This caused confusion when checking if the user had selected the correct answer.

![bug - correct numbering](/assets/docs/bug1-solved.png)


  * Action Taken:

  Firstly, the section of the code responsible for generating the answer options was identified. Specific changes were made in three parts of the code by adding the number 1 to correctly identify the user's response and ensure that the options were numbered from 1 to 4.

![Solved bug - correct numbering](/assets)

#### Naming Conflict

  * Bug Description:

  Another issue encountered was related to the test result, which was not being updated correctly. After investigating the cause of the error, it was identified that the chosen variable name, "hits," was conflicting with an argument in the function that had the same name.

  * Action Taken:

  To address this problem, the variable was renamed to "hits_col," thereby avoiding the conflict with the existing argument in the function. With this change, the test result started updating correctly.


![Solved bug - naming conflict](/assets/docs/bug2.png)


#### Disruption of program name ASCII art

  * Bug Description:

The latest issue encountered was related to the artwork of the test name initially created with the pyfiglet library. This artwork was displaying incorrectly when executed in the terminal after deployment. I believe the size of the generated image was exceeding the appropriate limits.

![bug - ASCII art](/assets/docs/bug3-1.png)


  * Action Taken:

I replaced the use of the pyfiglet library with ASCII art fonts generated from an external website (fsymbols). This measure definitively resolved the display issue.

![Solved bug - ASCII art](/assets/docs/bug3-solved.png)

#### Unsolved Bugs

No unfixed bugs.


