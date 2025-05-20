We have to do lots of queue logs instead making them manul we can do them with automatic with python 
you can track the issues or other things after 10 days later basically,

what is the problem statement for development team?

when they notice bug in the application they will create issue on the github repository 
developer or QE people they created Issue on the github repository and definitly you know this issue whoever creates
that issue that should not be considered an issue they can have some configuration issue or they dont understan application work flow properly 
there will be development team in your organization of the developers one a week or this developer goes to the repository there bugs now it s up to me if they are genuly issues or not that is, if the issue is valid they have to work particular issue 
they have to track amount of work that is required they have to show organization these are the issues that we are working on what they need to go the jira dashboard and create ticket on the jira dashboard so this is so much work for development team. They will come devops team say can you make it automated for me please 

and automation will be between Jira and Github

so what ı do firstly ı'will ask github whenever someone writes that comment clalled like jira , hey github ı have created python application  and ı have hosted it EC2 instance why dont you send to me a webhook ı will configure a webhook in Github and ı will tell Github through webhook send me all the ınformation about this comment or this issue who has created when created everything will be converting JSON formatted and now we will take the JSON information and we will make API cak to JIRA 


1_JIRA SETUP
2_JIRA API CALLS
3_PYTHON SCRIPTS
4_EXECUTION

you can go find all things JİRA API GROUPS....


how to convert to python program to API so ıf you ask why ı should write an API, Github through webhook trying to talk to the python application that you have Webhook will take PAYLOAD URL That ı had created with my python application.

commet ==> GITHUB ==>webhook ==> EC2(PYTHON APPLICATION) ==>API ==> JIRA

1= we need to understand what exactly API,
2= Convert to Python Script to API 
3= Deploy to Server
4= How to setup Github Webhook
5= conditionale Handling
