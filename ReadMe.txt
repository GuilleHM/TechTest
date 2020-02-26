Answers to Technical Test questions 2 to 4:

2.- 

First option would be to resize the photo on the server side before sending it so that it has the
right size (and no more) required by the website. Another improvement would be to use an optimized
lighter format for the image (i.e. webP). On the other hand, employing a strategy of "responsive
images", would help to improve downloading times into mobile devices. Finally, in a real production 
environment, optimizing a CDN would be a factor to consider (evaluating the cost / benefit ratio).

3.-

In an early-stage development environment, using a SAST methodology (running the antivirus library
manually or programatically against each module in the application) would be appropiate. For a QA
environment, a DAST methodology, running the antivirus library in a separate process and testing 
application´s security from the outside, would be more suitable. Lastly, in a production environment 
(or even in a CD/CI one, that employs a tool like Jenkins) the use of a Web Application Scanning 
(WAS) tool should be mandatory.

P.S.: The answer to this question is based on what I´ve been able to find out on the web regarding
with this topic. I have not enought security-related knowledge as to consider myself able to decide 
what specific (commercial or open source) tools should be selected in order to protect a real 
production system.

4.- 

Each time a user accesses the url where the photo is located (i.e. "/image/blue") the same function
that renders the web page (i.e. image()), could increase a counter and update it in a file. For real
cases, however, in web pages with high traffic, we would have to use threads pool strategies to work 
concurrently in order to provide a suitable service to users (in this case the routine responsible 
for updating the counter should run on a separate process and it would be better to store counter 
changes into a table -SQL- or document -noSQL- with web's usage metrics in the corresponding database).
