# Application_Sender_O_Matic
Email Applications out with copy of resume and list of projects to a given list of company emails

First, I would like to say I mean absolutely no disrespect in automating this task and chose all companies on my personal list due to my interest in working with them and the fact I think I could do really good work with them, but email a large chain of people can be extremely repetitive. It just feels inefficient. I probably also could have found a program that does exactly what I'm trying to do but it would been a lot less interesting and less customization. Not that we got that out of the way, let's start.


First thing to install a version of python
  Refer to python documentation, for help with this.
  (I recommend miniconda on windows, and standard linux python install)

All packages should be included by default with a normal install of python.

# A couple of things you will have to do before we can automatically send all of your emails  
## First - Write out a template email  
  - Include in the folder is a file, called template.text  
  - You can write your email out here normally.  
  - All standard characters are included in the result. All new-lines and tabs will show up. (Bold and Italics  are currently not available. Likely added in next update.)
  - In place of wherever you would refer to the name of company write CompanyName.
## Second - Write the list of companies
  - Refer to the file companies list to find a list of companies_list
  - As formatted write the Company Name and Company Email on each line  
## Third Add your Resume PDF and Projects PDF
  - Refer to the PDF's in the project file respectively named, "resume.pdf" and "project.pdf"
  - Replace these files keeping the naming convention
  - *In our alpha, we are mandating both files be included, but we hope to be able to make that more dynamic it future releases*  
## Fourth **Required**
  - We assume you are using g-mail to email these request out if not, refer to [https://myaccount.google.com/u/0/lesssecureapps]
  - Navigate to the right account, and flip the switch
  - **Essential that you switch this off after you finish emailing, it leaves your email unprotected against a lot of attacks, fine for temporary use but just don't forget.**  


That's it now you're ready to send some emails.
Just run the files
  python3 emailer.py
and follow the instructions

***Happy Job Hunting!***
