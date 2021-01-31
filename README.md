# SmileLog
![smilelog](https://user-images.githubusercontent.com/227092/76993446-6e44ff00-697f-11ea-9aed-970b8fa0e126.png)
**SmileLog 3.0** is a brilliant version.
- tail -f my-log.log
- Separating log file by session key

**SmileLog 2.0** is a big change for the backup file feature. This feature will make log easy to tail with the same name, and backup a yesterday log file.
- tail -f my-log.log
- Backup file: my-log-2020-05-25.log

It's gonna change the traditional tracing in another way.\
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
```
![smilelog-output](https://user-images.githubusercontent.com/227092/76993665-c845c480-697f-11ea-862d-8622cca09f14.png)

#### Start using in the simple way:

```
from smilelog import Logger, Consoler


# first instant
log	= Logger(
            enable= True
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
            name: str, 
            extension: str, 
            formatFileName: str, 
            enableLog: bool= True,
            enableConsole: bool= True,
            color: bool = True
	)
```
- path: is a directory
```
Ex:
/var/www/my-project/logs/
```
- formatFileName: is suffix name of log file
```
# set filename
formatFileName = 'my-logger'
Ex:
/var/www/my-project/logs/my-logger

# in dynamic way
formatFileName = '%Y-%m-%d'
Ex:
/var/www/my-project/logs/2020-01-19
```
- extension: is an extension of log file. The standard extension is '.log'
```
# set extension
extension = '.log'
Ex:
/var/www/my-project/logs/2020-01-19.log
```
- name: is the name of a new file log. 
```
# set name
name= 'my-log'

Ex: 
/var/www/my-project/logs/my-log-2020-01-19.log 
# some app move it into system log directory, it is an advantage of prefix

Ex:
/var/log/my-project-2020-01-19.log
```
- color: is for showing the color on terminal with tail command or terminal editor.
```
# set color
color= True
or
color= False
```
- enableLog: allow an object to create the file.
	- True: To create a file and write content into log file
	- False: To disable the logging
```
# set enable
# enable to write log file
enableLog= True
```

- enableConsole: to bring something on the screen of log.
	- True: To print out on terminal
	- False: No action
```
# set enable
enableConsole= True
```

### Disable print out
The most feature developer guy needs.\
It will disable only the index that we set in disable list.
##### Note: 
console and log object are not related each other.

```
# Logger instant
# Ex: Logger logged 10 times
# but we will show some id except 1,2,3,7,8,9
# do this
log.disable([1,2,3,7,8,9])

```

### Separate a session file 
Here is the method to separate normal log file to a specific.
Follow the setting:  

```
log.setSessionKey('cbc98494543823442425488df')
```
It will separate from the default log, and generate a new file as 'cbc98494543823442425488df.log'.
##### Note: 
To stop running a session, just set it the None.
```
log.setSessionKey(None)
```

02:48:29 <NbcseX32cDse> <id: 4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <NbcseX32cDse> <id: 5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[WARNING] Warning 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <NbcseX32cDse> <id: 6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <NbcseX32cDse> <id: 10>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
Hello String 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

```
