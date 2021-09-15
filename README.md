# VISTA APP

This project is my own implementation of the VISA Credit card checker. It was programmed following the Luhn's algorithm, which is the algorithm that determines whether or not a card is valid from its digits. Of course the process of checking an actual valid card is a lot more complex than just checking the digits (otherwise we would all be rich right now), but this project is a good way to apply data structures and algorithms, and realize how there are part of our daily lives.

# Instructions

1. [Download](https://github.com/pythonis-dan/VISTA-App/archive/refs/heads/master.zip) the Github Repository

2. Download and install [Python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) if necessary.

3. The Luhn's algorithm is fairly simple to implement. Here is how it checks if 4-5-1-0-1-5-6-0-2-0-1-8-9-7-5-4 is valid:
   
   -Given a 16-digit credit card number, each two digit starting from the second to last is doubled. We get 8-5-2-0-2-5-12-0-4-0-2-8-18-7-10-4

   -From the new string, each 2-digit number will be replaced by the sum of its 2 digits. In our case the 2-digit numbers are 12, 18 and 10. After adding those 2-digit numbers, we get the new string 8-5-2-0-2-5-3-0-4-0-2-8-9-7-1-4 (the single-digit number remaining intact)

   -From there we just add up all the digits in the string, we obtain 60.

   -Luhn's algorithm states that if the sum is divisible by 10 then the card is valid, which is the case for our example. [Learn more](https://en.wikipedia.org/wiki/Luhn_algorithm) about the Luhn's algorithm.

I hope you enjoy the Vista app :) This project welcomes contribution from anyone that's interested in improving it. If you have any questions regarding this project or anything about programming in general, feel free to reach out to me, I'll be glad to help. Have fun!
