This is my submission for the  MongoDB Summer 2023 Software Engineer Internship take home assessment.

For this assessment, developers had to write an algorithm which takes as input a JSON object and outputs a flattened JSON object. I solved this coding challenge using Python3.


## Python Version
To merge two flattened dictionaries together, I used the union operator. This is a new feature that was discussed in [PEP 584](https://peps.python.org/pep-0584/) and officially released with Python 3.9.0 in October 2020. Please keep in mind that the code will most probably throw an error when interpreted with a version of Python that was released prior to October 2020.


## How to run my solution
In the ```root``` directory, run the following command:
``` Bash
python3 flatten.py '<path to JSON object>' '<path to other JSON object>' '<path to other JSON object>'
```

It's possible to flatten multiple objects with one command by providing multiple paths to JSON objects separated by spaces. Keep in mind that the paths need to be encased in 'quotation marks'.

The results of the script are outputted as JSON files to the ```output``` folder. The outputted files will have the same name as the inputted file. For convenience, I have also added a few JSON objects to the ```data``` folder to test my solution against. These were inspired by the ones found [here](https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html#Example2).


## How to run the tests to my solution
In the ```tests``` directory, run the following command:
``` Bash
python3 -m unittest discover
```

## Assumptions
1. Any given input file contains at most one JSON object (this object can be empty).
2. The JSON objects have a maximum depth of 999 (my solution uses recursion, which is by default limited to 1,000 in Python).
3. The input is a valid JSON object.
4. The input does not contain any arrays.

## Dependencies
• Python 3.9.0+

This was a very fun problem to solve! Please don't hesitate to contact me should you have any questions or comments regarding my solution. Thank you for your time and consideration. :-)
