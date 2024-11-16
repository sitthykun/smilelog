"""
Author: masakokh
Version: 4.4.0
Note: library
"""
# built-in
import os
from datetime import datetime, timedelta
from typing import Any
# internal
# from smilelog.FCMLib import FCMLib
from RedisLib import RedisLib


class Logger:
	"""

	"""
	# hide all numbers that added
	hide    = []
	# index of output
	id      = 0

	def __init__(self, path: str= 'log', filename: str= 'access', extension: str= 'log', enableLog: bool= True, enableConsole: bool= True, line: bool= True, charInLine: int= 55, lineCharStart: str= '>', lineCharEnd: str= '<', color: bool = True, autoClean: bool= False, maxMb: int= 100):
		"""

		:param path:
		:param filename:
		:param extension:
		:param enableLog:
		:param enableConsole:
		:param line:
		:param charInLine:
		:param lineCharStart:
		:param lineCharEnd:
		:param color:
		:param autoClean:
		:param maxMb:
		"""
		# private
		## auto clean file, self-clean
		self.__autoClean            = autoClean
		## datetime format
		## ex: 2020-05-18
		self.__dateFormat   	    = '%Y-%m-%d'
		## full datetime format
		### ex: 2022-05-12 21:40:20.345
		self.__dateTimeFormat   	= f'{self.__dateFormat} %H:%M:%S'
		## set color
		self.__color            	= color
		self.__line             	= line
		self.__lineCharStart        = f'{lineCharStart}' * charInLine
		self.__lineCharEnd          = f'{lineCharEnd}' * charInLine
		# config
		self.__enableConsole    	= enableConsole
		self.__enableLog        	= enableLog
		# redis
		self.__enableRedis			= False
		self.__enableRedisError		= False
		self.__enableRedisFail		= False
		self.__enableRedisInfo		= False
		self.__enableRedisSuccess	= False
		self.__enableRedisTrack		= False
		self.__enableRedisWarning	= False
		##
		self.__extension        	= f'.{extension}'
		## path + /
		self.__path            		= path
		## by default size of each file is 100 mb, if greater than it will reset itself to 0mb
		## to continue the new line in the file log
		self.__sizeMaxMb            = maxMb
		## compute
		self.__filename         	= os.path.join(self.__path, f'{filename}{self.__extension}')
		# static datetime
		self.__datetime         	= datetime.now().strftime(self.__dateTimeFormat)
		# pub/sub
		# self.__fcm				= FCMLib()
		self.__redis				= RedisLib()
		#
		self.__titleError           = 'ERROR'
		self.__titleFail            = 'FAIL'
		self.__titleInfo            = 'INFO'
		self.__titleSuccess         = 'SUCCESS'
		self.__titleTrack           = 'TRACK'
		self.__titleWarn            = 'WARN'

	def __createNewBackupFile(self) -> None:
		"""

		:return:
		"""
		# backup the yesterday content and use the yesterday as name of the backup file
		yesterdayFileName       = self.__getBackupFileName()

		# check yesterday file with len of current file
		if not os.path.exists(yesterdayFileName) and len(self.__getContentFile(self.__filename)) > 0:
			# rename current file to do backup
			# that will move content too
			os.rename(
				self.__filename
				, yesterdayFileName
			)

	def __getBackupFileName(self) -> str:
		"""

		:return:
		"""
		# generate a filename
		return os.path.join(self.__path, f'{(datetime.now() - timedelta(1)).strftime(self.__dateFormat)}{self.__extension}')

	def __checkRedisByType(self, typeName: str) -> bool:
		"""

		:param typeName:
		:return:
		"""
		if typeName == self.__titleError:
			return self.__redis.enableError
		elif typeName == self.__titleFail:
			return self.__redis.enableFail
		elif typeName == self.__titleInfo:
			return self.__redis.enableInfo
		elif typeName == self.__titleTrack:
			return self.__redis.enableTrack
		elif typeName == self.__titleSuccess:
			return self.__redis.enableSuccess
		elif typeName == self.__titleWarn:
			return self.__redis.enableWarn

	def __getContentBody(self, typeName: str, title: str, content: Any, color: str) -> str:
		"""

		:param typeName:
		:param title:
		:param content:
		:param color:
		:return:
		"""
		cBody       = f'[{typeName}] '
		cFoot       = ''
		cHead       = ''

		# add line to content
		if bool(self.__line):
			# update
			cHead       = self.__lineCharStart
			cFoot       = self.__lineCharEnd

		# add color, style
		if bool(self.__color):
			# update
			cHead       = f'{color}{cHead}{self.__StyleModifier.END_C}'
			cFoot       = f'{color}{cFoot}{self.__StyleModifier.END_C}'
			cBody       = f'{color}{cBody}{self.__StyleModifier.END_C}{self.__StyleModifier.TEXT_BOLD}{title}{self.__StyleModifier.END_C}'

		else:
			cBody       = f'{cBody}{title}'

		cBody       = f'{cBody}\n{self.__getStr(content)}'

		# final content
		return f'{cHead}\n{cBody} \n{cFoot}' if bool(self.__line) else f'{cBody}'

	def __getContentFile(self, fileName: str) -> str:
		"""

		:param fileName:
		:return:
		"""
		# init
		content = ''

		try:
			# read file
			with open(fileName) as f:
				content = f.read()

			# final
			return content

		except IOError:
			return content

		except Exception:
			return content

	def __getContentHead(self, logId: int, idLabel: str= '', keySeries: str= '', keySession: str = '') -> str:
		"""

		:param logId:
		:param idLabel:
		:return:
		"""
		if keySeries and keySeries != '':
			keySeries = f' <{keySeries}> '

		# final data
		if keySession:
			return f'{self.__datetime}{keySeries}<{idLabel}{logId}> {keySession}'

		else:
			return f'{self.__datetime}<{keySeries}><{idLabel}{logId}>'

	def __getStr(self, content: Any) -> str:
		"""

		:param content:
		:return:
		"""
		if isinstance(content, dict):
			return str(content)

		elif isinstance(content, str) or type(content) == str:
			return content

		else:
			return ''

	def __isEnabledRedis(self, enabledLevel: bool) -> bool:
		"""

		:param enabledLevel:
		:return:
		"""
		return self.__enableRedis and enabledLevel

	def __msgRedis(self, channel: str= None) -> None:
		"""

		:param channel:
		:return:
		"""
		self.__redis.messageGet(channel)

	# def __pushFCM(self, title: str, body: str) -> None:
	# 	"""
	#
	# 	:param title:
	# 	:param body:
	# 	:return:
	# 	"""
	# 	pass

	def __pushRedis(self, isEnabled: bool, title: str, content: str, channel: str = None, keySeries: str = None) -> None:
		"""

		:param isEnabled:
		:param title:
		:param content:
		:param channel:
		:param keySeries:
		:return:
		"""
		if self.__isEnabledRedis(enabledLevel= isEnabled):
			#
			self.__redis.messagePush(
				title		= title
				, body		= content
				, channel	= channel
				# , keySeries = keySeries
			)

	def __setNewId(self, id: int) -> None:
		"""

		:param id:
		:return:
		"""
		if id > Logger.id:
			Logger.id   = id

	def __write(self, typeName: str = '', title: str = '', color: str = '', content: Any = None, logId: int = None, keySeries: str = None, keySession: str = None, channel: str = None) -> None:
		"""

		:param typeName:
		:param title:
		:param color:
		:param content:
		:param logId:
		:param keySeries:
		:param keySession:
		:return:
		"""
		#
		self.__writeFinal(typeName, title, color, content, logId, keySeries, keySession)

		#
		self.__pushRedis(
			isEnabled	= self.__checkRedisByType(typeName= typeName)
			, title		= title
			, content	= content
			, channel	= channel
			, keySeries = keySeries
		)

	def __writeFinal(self, typeName: str = '', title: str = '', color: str = '', content: Any = None, logId: int = None, keySeries: str= None, keySession: str = None) -> None:
		"""

		:param typeName:
		:param title:
		:param color:
		:param content:
		:param logId:
		:param keySeries:
		:param keySession:
		:return:
		"""
		# create file
		self.__createNewBackupFile()

		# validate log Id
		if logId:
			# Reset log id
			self.__setNewId(logId)

		else:
			# increase index first
			Logger.id += 1

		# do filter
		if Logger.id not in Logger.hide:
			# update content
			contentBody = self.__getContentBody(typeName= typeName.upper(), title= title, content= self.__getStr(content= content), color= color)
			contentHead = self.__getContentHead(logId= Logger.id, idLabel= 'id: ', keySeries= keySeries)

			# enable file log
			if bool(self.__enableLog):
				# write to file
				self.__writeFile(content= f'{contentHead}\n{contentBody}\n\n')

				# verify first
				if keySession:
					# output content to specific file via session's
					self.__writeSessionFile(sessionKey= keySession, content= f'{contentHead}\n{contentBody}\n\n')

			# enable console
			if bool(self.__enableConsole):
				# console
				print(f'{contentHead}\n{contentBody}')

	def __writeFile(self, content: Any) -> None:
		"""

		:note: final written file
		:param content:
		:return:
		"""
		try:
			# covert Mb to byte
			if self.__autoClean and os.stat(self.__filename).st_size > (self.__sizeMaxMb * 1024 * 1024):
				# override file
				with open(self.__filename, 'w') as fo:
					fo.write(content)

			else:
				# open log file, if not exist will create
				with open(self.__filename, 'a+', encoding= 'utf-8') as fo:
					fo.write(content)

		except FileNotFoundError as e:
			print(f'Logger.__writeFile output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

		except IOError as e:
			print(f'Logger.__writeFile output file IOError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

		except Exception as e:
			print(f'Logger.__writeFile output file Exception: open file({self.__filename}), {str(e)}')

	def __writeSessionFile(self, sessionKey: str, content: Any) -> None:
		"""

		:param content:
		:return:
		"""
		try:
			# open log file, if not exist will create
			with open(f'{self.__path}{sessionKey}{self.__extension}', 'a+', encoding= 'utf-8') as fs:
				fs.write(content)

		except FileNotFoundError as e:
			print(f'Logger.__writeSessionFile output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__path}{sessionKey}{self.__extension}), {str(e)}')

		except IOError as e:
			print(f'Logger.__writeSessionFile output file IOError: open file {e.errno} {e.strerror}({self.__path}{sessionKey}{self.__extension}), {str(e)}')

		except Exception as e:
			print(f'Logger.__writeSessionFile output file Exception: open file ({self.__path}{sessionKey}{self.__extension}), {str(e)}')

	def disableIds(self, numbers: list = None) -> None:
		"""

		:param numbers:
		:return:
		"""
		if numbers:
			Logger.hide     = numbers

	def error(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:param channel:
		:param keySeries:
		:return:
		"""
		self.__write(
			typeName    = self.__titleError
			, title     = title
			, content   = content
			, color     = self.__StyleModifier.RED
			, logId     = id
			, keySeries = keySeries
			, keySession= keySession
			, channel   = channel
		)

	def fail(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:param channel:
		:param keySeries:
		:return:
		"""
		self.__write(
			typeName    = self.__titleFail
			, title     = title
			, content   = content
			, color     = self.__StyleModifier.MAGENTA
			, logId     = id
			, keySeries = keySeries
			, keySession= keySession
			, channel   = channel
		)

	def info(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:param channel:
		:param keySeries:
		:return:
		"""

		self.__write(
			typeName    = self.__titleInfo
			, title     = title
			, content   = content
			, color     = self.__StyleModifier.BLUE
			, logId     = id
			, keySeries = keySeries
			, keySession= keySession
			, channel   = channel
		)

	# def setFCM(self, config: dict) -> None:
	# 	"""
	#
	# 	:param config:
	# 	:return:
	# 	"""
	# 	self.__fcm.setConfig(config)

	def setRedis(self, enable: bool, host: str, port: int, db: int = 0, password: str = None, enableError: bool = False, enableFail: bool = False, enableInfo: bool = False, enableTrack: bool = False, enableSuccess: bool = False, enableWarning: bool = False, channel: str = None) -> None:
		"""

		:param enable:
		:param host:
		:param port:
		:param db:
		:param password:
		:param enableError:
		:param enableFail:
		:param enableInfo:
		:param enableTrack:
		:param enableSuccess:
		:param enableWarning:
		:param channel:
		:return:
		"""
		# assign value
		self.__enableRedis		= enable

		# config the redis property to connect to the server
		self.__redis.config(
			host		= host
			, port		= port
			, db		= db
			, password	= password
		)

		# enable level of pub/sub
		self.__redis.enableError	= enableError
		self.__redis.enableFail		= enableFail
		self.__redis.enableInfo		= enableInfo
		self.__redis.enableTrack	= enableTrack
		self.__redis.enableSuccess	= enableSuccess
		self.__redis.enableWarning	= enableWarning

		# set channel name
		self.__redis.channelSet(channel= channel)

	def success(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:param channel:
		:return:
		"""
		self.__write(
			typeName    = self.__titleSuccess
			, title     = title
			, content   = content
			, color     = self.__StyleModifier.GREEN
			, logId     = id
			, keySeries = keySeries
			, keySession= keySession
			, channel   = channel
		)

	def trace(self, content: Any = None) -> None:
		"""

		:param content:
		:return:
		"""
		self.__writeFile(content= f'{content}\n')

	def warning(self, title: str = '', content: Any = None, id: int = None, channel: str = None, keySeries: str = None, keySession: str= None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:param channel:
		:return:
		"""
		self.__write(
			typeName    = self.__titleWarn
			, title     = title
			, content   = content
			, color     = self.__StyleModifier.YELLOW
			, logId     = id
			, keySeries = keySeries
			, keySession= keySession
			, channel   = channel
		)

	class __StyleModifier:
		# Foreground
		BLUE            = '\033[94m'
		BLACK           = '\033[90m'
		CYAN            = '\033[96m'
		GREEN           = '\033[92m'
		GREY            = '\033[90m'
		MAGENTA         = '\033[95m'
		RED             = '\033[91m'
		WHITE           = '\033[97m'
		YELLOW          = '\033[93m'
		# Text style
		TEXT_BOLD       = '\033[1m'
		TEXT_UNDERLINE  = '\033[4m'
		# End up color
		END_C           = '\033[0m'
