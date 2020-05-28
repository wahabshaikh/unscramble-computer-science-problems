# Unscramble Computer Science Problems
Project 1 of the Data Structures &amp; Algorithms Nanodegree Program from Udacity.

<hr>

## Investigating Texts and Calls

In this project, I have completed five tasks based on a fabricated set of calls and texts exchanged during September 2016. I have used Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, I performed run time analysis of my solution and determined its efficiency.

### About the data

The text and call data are provided in csv files.

The text data (<code>text.csv</code>) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (<code>call.csv</code>) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

<ul>
<li>Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".</li>
<li>Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".</li>
<li>Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".</li>
</ul>
