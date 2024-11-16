# SmileLog
![smilelog](https://user-images.githubusercontent.com/227092/76993446-6e44ff00-697f-11ea-9aed-970b8fa0e126.png)
**SmileLog 4.4.0**\
- Implement trace(content= 'content') for tracking without title
- Remove begin() and end() method
- Remove track() method

Ex:
```
trace(content= 'miss mom')
```

**SmileLog 4.3.0**\
Implement begin() and end() method. These will keep the content in sequence of text and set only one title as TRACE.

Ex:
```
begin()

warning(title= 'Hello Title Warning', content= 'Warning content')
info(title= 'Hello Info', content= 'Info content')
error(title= 'Hello Error', content= 'Error content')

end()
```

Output:
```
[TRACE] Hello Title Warning
Warning content
Info content
Error content
```

**SmileLog 4.2.0**\
Change logical business of the keySession by adding to those methods rather than setKeySession to make it dynamic on the run time.
Ex:
Before
```
warning(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None)
```

After
```
warning(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
```

Every writing a log, it will check this value.

The features since version 4.1.x:
- Log to a static file
- Backup file everyday
- Enable series of log session
- Parallel log between static log and session log
- Push any log to redis via pubsub method
- Dynamic line separation
  - on or off
  - editable line character
  - editable number of line character
- Fix bugs
- Improve performance
- Clean up code
- Auto clean up teh file when it set by maxMb

Traditional tracing will undergo a change in a different way.\
What will it assist us:
 
1. Displaying the colored log by adhering to the standard colors.
2. Identifying a track by reading its ID in the list.
3. Each statement lists down with a big span and symbols
4. Using a static file to output the content that will be easier
5. Disable the entire tracing in a second
6. 5 methods for 5 outputs
7. Backup file if log start a new date
8. Separating a new file with a new file name.
This feature will cover to a specific tracking.
9. Group the log with specific key(series key)
10. Able to set maxSize log
11. Implementing some commands with CLI
12. Change business log for KeySession

It is available on **PyPi** store via https://pypi.org/project/SmileLog/ \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>
 
#### Installation
```
# pip3 install SmileLog
```

### 6 Methods
Use in the different situation, and show up in different color
1. error: error(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
2. fail: fail(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
3. information: info(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
4. success: success(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
5. track: track(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
6. warning: warning(title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None)
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
	title	 	= 'My Success Title'
	, content	= 'My String'
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
           path:                str	= 'log'
           , filename: 			str = 'access'
           , extension: 		str = 'log'  
            , enableLog: 		bool= True
            , enableConsole:    bool= True
            , line: 			bool= True
            , charInLine: 		int	= 55
            , lineCharStart:    str = '>'
            , lineCharEnd: 		str = '<',
            , color: 			bool= True
            , autoClean:        bool= False
            , maxMb:            int=100
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
- **enableLog**: To allows an object to create the file.
	- True: To create a file and write content into log file
	- False: To disable the logging
```
# set enable
# enable to write log file
enableLog= True
```

- **enableConsole**: To shows something on the screen of log.
	- True: To print out on terminal
	- False: No action
```
# set enable
enableConsole= True
```

### Series
Just a series name of output
- **setKeySeries**: data
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
Here is the method to separate normal log file to a specific session.
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
#### initializes redis requirement
- setRedis
  - host: required
  - port: required
  - channel: the default is None, subscribe and publish
  - db: by default is 0
  - password: by default is None
### enable Redis Engine
- enableRedis: bool
#### enable any functional alert
- enableError: bool
- enableFail: bool
- enableInfo: bool
- enableTrack: bool
- enableSuccess: bool
- enableWarning: bool
