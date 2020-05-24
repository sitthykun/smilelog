# SmileLog
![smilelog](https://user-images.githubusercontent.com/227092/76993446-6e44ff00-697f-11ea-9aed-970b8fa0e126.png)

It's gonna change the traditional tracing in another way.\
What will it assist us:
 
1. Colorise output
2. Be able to stop any output via its public id
3. Split each output with a big span and symbols
4. Generate a new dynamic log filename
5. Disable the entire tracing in a second
6. 5 methods for 5 outputs

It is available on **PyPi** store via https://pypi.org/project/SmileLog/ \
To Support my work, please donate me via <style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#79D6B5 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 22px !important;letter-spacing: 0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Pizza</span></a>
 
#### Installation
```
# pip3 install SmileLog
```


### 5 Methods
Use in different situation, and show up in different color
1. track: track(title, content, id= None)
2. information: info(title, content, id= None)
3. success: success(title, content, id= None)
4. warning: warning(title, content, id= None)
5. error: error(title, content, id= None)
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
```

### Logger
Logger is a tracing class library and write/output into a file.\
This will need generating a file and keep writing the content.
Let's Look at its configure would explain more:

```
log	= Logger(
            path: str, 
            prefix: str, 
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
- prefix: is prefix name of a new file log. 
```
# set prefix
prefix= 'my-log-'

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
- enable: is a main parameter that determines above features. It has two value only.
	- True: To enable the logging
	- False: To disable the logging
```
# set enable
# enable to write log file
enableLog= True
# enable to print out
enableConsole= True
```

### Disable print out
The most feature developer guy needs.\
It will disable only the index that we set in the disable list.
##### Note: 
console and log object are not related each other.

```
# Logger instant
# Ex: Logger logged 10 times
# but we will show some id except 1,2,3,7,8,9
# do this
log.disable([1,2,3,7,8,9])

```

### Output
It's gonna show like this:
```
02:48:29 <id: 4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <id: 5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[WARNING] Warning 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <id: 6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <id: 10>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
Hello String 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

```
##### My unique slogan is:
a little developer in the big world \o/
