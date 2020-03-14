# SmileLog

It's gonna change the tranditional tracking in another way.\
What will it assist us.
 
1. Colorise output
2. Be able to stop any output via its public id
3. Split each output with a big span
4. Generate a new dynamic log filename
5. Disable the entire tracking in a second
6. 5 methods for 5 outputs

### 5 Methods
Use in different situation, and show up different color too
1. track: track(title, content)
2. information: info(title, content)
3. success: success(title, content)
4. warning: warning(title, content)
5. error: error(title, content)
```
- title is a string
- content can be a string or dict
```

#### Start using in the simple way:

```
from pylog import Logger, Consoler


# first instant
console	= Consoler(
		enable= True
		)

# try to print out
console.info(
		'My Info Title'
		, {'data':'My Dictionary Content'}
		)

# success method
console.success(
		'My Success Title'
        , 'My String'
        )
```

### Logger Vs. Consoler

##### 1. Logger:
Logger is a tracking class library and write/output into a file.\
This will need generating a file and keep writing the content.
Let's Look at its configure would explain more:

```
log	= Logger(
            path: str, 
            prefix: str, 
            extension: str, 
            formatFileName: str, 
            enable: bool, 
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
# make all above working
enable= True
```

##### 2. Consoler
Consolder is a tracking class library and show in terminal as just in time.
The class is simpler that Logger by just needing a couple parameters and no storage requirement.

As the first sample above:
```

```

### Disable print out
The most feature developer guy needs.\
It will disable only the index that we set in the disable list.
##### Note: 
console and log object are not related each other.

```
# Logger instant
# it shows all except 1,2,3
log.disable([1,2,3])

# Consolder instant
# it shows all except 3, 6, 7
console.disable([3, 6, 7, 89])
```

### Output
It's gonna show like this:
```
02:48:29 <id: 6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[SUCCESS] Success 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <id: 8>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[WARNING] Warning 
{'data': 'my content'} 
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



02:48:29 <id: 9>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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
