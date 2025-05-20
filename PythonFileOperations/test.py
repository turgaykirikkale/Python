#task:  update the server.conf file when "max_connections" - 200 reached point you can make it 500 hundred
# ı need too operations update the server.config

#1 read the file
#2 variable list from reading file
#3 again open the fike this time write mode 
#4 update the maxiumum connections when connections wents ups.

#def update_server_config(file_path, key, value):

def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines() #everything thats is available in that server.config file
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_server_config("server.conf", "MAX_CONNECTIONS", "1200")