for connect to AWS andget the list of S3 Buckets we use the very simple syntax

---> AWS S3 ls = passing arguments this way is called command line arguments 

so command line arguments used for passing to arguments to your program. Your program can take 
command line arguments as an input.

how to do that ? there are modules for this you dont do it by yourself you are searching for modules 
there are lots of modules these are coming with the installation before installing them from PyPi lets
bundle them in the python installation itself

there is module its called "sys" it will help you to command line arguments for entrying

if you wanna read the arguments =  sys.argv[1], sys.arg[2] this is how you can read.

==ENVIRONMENT VARIABLES

when you write python program you have deal with a lot of sensitive information what if you want to pass password 
what if ıf you want to pass some API Key Token, Some informations
or for reaching AWS you need to pass some secure way for your account like credentials, 