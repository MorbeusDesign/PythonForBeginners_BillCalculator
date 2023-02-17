# Introduction
<img src = 'https://github.com/MorbeusDesign/PythonForBeginners/blob/master/friendsAtRestaurant.jpg' alt = 'Welcome to our Restaurant' />
This Python project is designed to help beginner developers practice their skills by building a simple program that calculates the cost of a lunch at a restaurant, including tip and dividing the total cost by the number of people in a group. The project includes a step-by-step guide to building the program, as well as sample code to help you get started.

# Step-by-Step Guide

- Step 1: __Ask the User for Input__
To begin, we need to ask the user for some input to use in our calculations. Specifically, we need to ask how many people are in the group, what the total cost of the lunch was, and what percentage tip they would like to leave. Here's some sample code to get you started:

```python
num_people = int(input("How many people are in your group? "))
total_cost = float(input("What was the total cost of the lunch? "))
tip_percent = float(input("What percentage tip would you like to leave? "))
```

This code uses the input() function to prompt the user for input, and the int() and float() functions to convert the user's input to the appropriate data types (integer or float). We store the user's input in variables for later use.

- Step 2: __Calculate the Tip and Total Cost__
Next, we need to calculate the tip and add it to the total cost of the lunch. Here's some sample code to get you started:

```python
tip_amount = total_cost * tip_percent / 100
total_cost += tip_amount
```

This code calculates the tip amount by multiplying the total cost by the tip percentage (converted to a decimal), and then adds the tip amount to the total cost.


- Step 3: __Divide the Cost by the Number of People__
Finally, we need to divide the remaining cost (after the tip is added) by the number of people in the group to get the cost per person. Here's some sample code to get you started:

```python
cost_per_person = total_cost / num_people
This code divides the total cost by the number of people in the group to get the cost per person.
```

- Step 4: Display the Results
The last step is to display the results to the user. Here's some sample code to get you started:

```python
print(f"The total cost of the lunch is {total_cost:.2f}")
print(f"The tip amount is {tip_amount:.2f}")
print(f"The cost per person is {cost_per_person:.2f}")
```

This code uses string formatting to display the results to the user with two decimal places. The f-string syntax (the f before the opening quote) allows us to insert variables and expressions directly into the string.

<a><img src="https://github.com/MorbeusDesign/PythonForBeginners/blob/master/restaurantBillCalc.gif"></a>&nbsp;

# Conclusion
This project is a simple but effective way for beginner Python developers to practice their skills and build a useful program. By following the step-by-step guide and experimenting with the sample code, you'll learn how to prompt the user for input, perform calculations, and display results. Good luck, and happy coding!
__Drop a ⭐ if you find it useful!👍__

<a href="https://www.buymeacoffee.com/Morbeus"><img src="https://media.giphy.com/media/FoAQVAmLEsOz8DV2HS/giphy.gif" align="right" width="250" /></a>&nbsp;
<img src="https://github.com/MorbeusDesign/MorbeusDesign/blob/main/Developer.png" align="center" width="350" /> 


<p >

<a href="https://linkedin.com/in/morbeusdesign"><img align="left" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/linkedin.svg" alt="MorbeusDesign" height="30" width="30" /></a>&nbsp;
<a href="https://www.facebook.com/TheMorbeusZone"><img align="left" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/facebook.svg" alt="MorbeusDesign" height="30" width="30" /></a>&nbsp;
<a href="https://www.instagram.com/themorbeuszone"><img align="left" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/instagram.svg" alt="MorbeusDesign" height="30" width="30" /></a>&nbsp;
<a href="https://www.pinterest.de/MorbeusDesignCom/"><img align="left" alt="MorbeusDesignCom" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/pinterest.svg" /></a>&nbsp;
<a href="https://twitter.com/morbeusdesign"><img align="left" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/twitter.svg" alt="MorbeusDesign" height="30" width="30" /></a>&nbsp;
<a href="https://codepen.io/MorbeusDesign"><img align="left" alt="MorbeusDesign" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/codepen.svg" /></a>&nbsp;
<a href="https://www.freecodecamp.org/Morbeus"><img align="left" alt="FreeCodeCamp" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/freecodecamp.svg" /></a>&nbsp;
<a href="https://www.buymeacoffee.com/Morbeus"><img align="left" alt="Buy me a Coffee" height="30" width="30px" src="https://cdn.jsdelivr.net/npm/simple-icons@7.15.0/icons/buymeacoffee.svg" /></a>&nbsp;
      
</p>