# SmileLog
![smilelog](https://user-images.githubusercontent.com/227092/76993446-6e44ff00-697f-11ea-9aed-970b8fa0e126.png)
**SmileLog 3.1** is a brilliant version.
- tail -f access.log
- Separating log file by session key

It's going to change the traditional tracing in another way.\
What will it assist us:
 
1. Showing the colorized log by following the standard color
2. Ignoring any track by reading id in the list 
3. Each statement list down with a big span and symbols
4. Using a static file to output the content that will be easier
5. Disable the entire tracing in a second
6. 5 methods for 5 outputs
7. Backup file if log start a new date
8. Separating a new file with a new file name
This feature will cover to a specific tracking.
9. Group the log with specific key(series key)

It is available on **PyPi** store via https://pypi.org/project/SmileLog/ \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>
 
#### Installation
```
# pip3 install SmileLog
```

### 5 Methods
Use in the different situation, and show up in different color
1. track: track(title, content, id= None)
2. information: info(title, content, id= None)
3. success: success(title, content, id= None)
4. warning: warning(title, content, id= None)
5. error: error(title, content, id= None)
6. fail: fail(title, content, id= None)
```
- title is a string
- content can be a string or dict
Figure (version 2.0)
```
![smilelog-output](https://user-images.githubusercontent.com/227092/76993665-c845c480-697f-11ea-862d-8622cca09f14.png)

#### Start using in the simple way:

```
from smilelog import Logger


# first instant
log	= Logger(
            enableLog= True
	)

# try to print out
log.info(
	'My Info Title'
	, {'data':'My Dictionary Content'}
)

# success method
log.success(
	'My Success Title'
	, 'My String'
)

# setKeySeries is a new method to indicate to the token of a long message
log.setKeySeries('NbcseX32cDse')
```

### Logger
Logger is a tracing class library and write/output into a file.\
This will need generating a file and keep writing the content.
Let's Look at its configure would explain more:

```
log	= Logger(
            path: str, 
            filename: str, 
            extension: str,  
            enableLog: bool= True,
            enableConsole: bool= True,
            line: bool= True
            color: bool= True
	)
```
- **path**: is a directory
```
Ex:
/var/www/my-project/logs/

```
- **filename**: is the name of a new file log. 
```
# set name
filename= 'access'

Ex: 
/var/www/my-project/logs/access.log 
# some app move it into system log directory, it is an advantage of prefix

```
- **color**: is for showing the color on terminal with tail command or terminal editor.
```
# set color
color= True
or
color= False
```
- **enableLog**: allow an object to create the file.
	- True: To create a file and write content into log file
	- False: To disable the logging
```
# set enable
# enable to write log file
enableLog= True
```

- **enableConsole**: to bring something on the screen of log.
	- True: To print out on terminal
	- False: No action
```
# set enable
enableConsole= True
```

### Series
Just a series name of output
- **setKeySeries**: date
```
# set value
log.setKeySeries('Insert Data')
# stop
log.setKeySeries()
```

### Disable print out
The most feature developer guy needs.\
It will disable only the index that we set in disable list.
- **disableIds**: hide those ids.
  - parameter must be Array

```
# Logger instant
# Ex: Logger logged 10 times
# but we will show some id except 1,2,3,7,8,9
# do this
log.disableIds([1,2,3,7,8,9])
```

### Separate a session file 
Here is the method to separate normal log file to a specific.
Follow the setting: 
- **setKeySession**: must be a string and maximum length 32

```
log.setKeySession('cbc98494543823442425488df')
```
It will separate from the default log, and generate a new file as 'cbc98494543823442425488df.log'.
##### Note: 
To stop running a session, just set it the None.
```
log.setKeySession()
```

2022-05-12 21:40:20.345 <id: 4>\
_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
[FAIL] **My Title**\
{'data': 'my content'}  
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



2022-05-12 21:40:20.345 <id: 5> Insert Data\
_>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\
[WARNING] **Warning**\
{'data': 'my content'}\
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



2022-05-12 21:40:20.345 <id: 6> Delete Row\
[TRACK] My Title\
{'data': 'my content'}



2022-05-12 21:40:20.345 <id: 10>\
[SUCCESS] **Success**\
Hello String

## Pub/Sub
### Redis
- enableRedis:
- setRedis
  - enable: required
  - host: required
  - port: required
  - channel: the default is None, scribe and publish
  - db: by default is 0
  - password: by default is None
- 
