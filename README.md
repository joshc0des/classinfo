# Fall 2022 MIS Programming Bowl Project
Hi, I'm Joshua Hooper, and for my MIS Programming Bowl project, I created a program that scrapes HTML tables from ClassNav at the University of Oklahoma's class catalogue website ClassNav using Node.js and Puppeteer. The program then stores the scraped data into a JSON file for further analysis.

## Introduction
As a student majoring in Management Information Systems with an interest in web development, I wanted to explore how to automate the process of extracting data from websites that do not offer a convenient API. I found ClassNav to be a great source of information for course schedules, but the website doesn't offer an easy way to export the data. That's why I decided to create a program that could extract the data for me.

## Approach
I used Node.js, a popular server-side JavaScript runtime, and Puppeteer, a Node.js library that provides a high-level API for controlling headless Chrome or Chromium browsers. With Puppeteer, I was able to automate the process of opening ClassNav, selecting the relevant search criteria, and extracting the HTML tables from the search results.

The program runs in headfull mode with a visually open Chrome window rather than running headless/in the background. Then, Puppeteer navigates to the ClassNav website, enters preset search criteria, and extracts the relevant HTML tables. The program then converts the HTML tables to JSON format and saves the data to a JSON file.

## Results
The program was successful in extracting the data from ClassNav and saving it in a usable format. The JSON file contains all of the relevant information from the HTML tables, including the Course Reference Number (CRN), Course Subject, Course Name, Course Section, Course Section Title, Primary Instructor, Course Dates, Seats Left, and Wait List.

## Conclusion
Overall, this project was a great learning experience for me. I gained experience using Node.js and Puppeteer to extract data from web pages. I also learned how to Puppeteer in different configurations to look more or less like a human to the website it visits. This project has given me a solid foundation for further exploration in web scraping and automation.
