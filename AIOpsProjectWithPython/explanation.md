we will create python script we will use machine learning algorithm which helps us perform anonomaly detection althoug 

AIOps ==> Artıficiel intelligence for operations using AI to analysis to data and predict any strange pattern in the data we called as anomalies and if possible avoid happaning that event it can be by sending notifications to right people taking required action using AI now all this needs data in devops engineering most important implication of AIops where Aıops majorly used is in the space of observability you have huge amount of data comes from metrics logs and traces, Aıops is anticipate the future orders packed and if the orders packed lets say with Logs ELK, Loky

a point to be noted AI performs better when there is huge amount data and there is historical data 

we will do today isolationforest For Machiene Learning (its one the best option for anomaly detection) 

if we talk about history metrics as a devops engineer as SR engineers why logs analysis is important , people are more insterested on micro services architecture because of the advantages of that progress when it comes to micro services is dealing with hundres  services emit the logs if its single service its very easy to for devops engineer you can easily write a cronjob for just single one when there are hundred resources how will you do that ? When you implement services you integrate your logs  to platforms like ELK or Loky

logs ==> logstash ==> ELastik Logs ==> Kibana (Log visualization) when you go to kibana dashboard you are searching for the error so you will get error from all logs from all services you can still do that 

however when you have so many applications how will you identify the a strange pattern and these starange patterns called as anomalies so how will you identify them  ? okay there are warnings or Errors or memory errors and they repeat 60 times in a minutes and maybe they repeat 100 times in minute and you dont notice them and after 1 day your applicatin might go down state,

for this you might create Alerts you might say for a particular error type if there error occurs 10 times one hour of time just send a notification SR engineers however there is some warning or alerts and you event noticed it you can do this for known patterns so this is kind of reactive approach you do for the things you already now however how will you go to a proactive approach so we can take help AIops in this case

we can train AI through Machine learning algorithms one of the popular maachine learning algorithms is isolationforest is unsupervised machine learning algorithm you dont to provide label data you can just provide it with data it will process data it will identify anomlies in data you dont have tell that these are strange patterns in data it will start understanding by itself you can train the algorithm for make perform better it can help detect it, if you configure notifications you can avoid the future issue using the AI


For ELK  -- this is traditional approach 

1-Read the file 
2-Serialized the data(expected format)
   --you can use panda like time | logs level | log Message 
3- you analize the data with for loop 
   4--you will count the errors 
   5--if count of errors == threshold
     6-- you will say print the error 
      -- you can send email or smthing else 
    

