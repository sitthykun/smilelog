"""
Author: masakokh
Version: 3.1.0
"""
import datetime
import os
from datetime import datetime, timedelta
from typing import Any


class Logger:
	"""

	"""
	# hide all numbers that added
	hide    = []
	# index of output
	id      = 0

	def __init__(self, path: str, name: str, extension: str, formatFileName: str, enableLog: bool= True, enableConsole: bool= True, line: bool= True, color: bool= True):
		"""

		:param path:
		:param name:
		:param extension:
		:param formatFileName:
		:param enableLog:
		:param enableConsole:
		:param line:
		:param color:
		"""
		# default datetime format
		# 2022-05-12 21:40:20.345
		self.__dateTimeFormat   = '%Y-%m-%d %H:%M:%S.%f'
		# set color
		self.__color            = color
		self.__line             = line
		# config
		self.__enableLog        = enableLog
		self.__enableConsole    = enableConsole
		self.__extension        = extension
		# 2020-05-18
		self.__formatFileName   = formatFileName    or ''
		# path + /
		self.__name             = name
		self.__path             = path

		# compute
		self.__filename         = f'{self.__path}{self.__name}{self.__extension}'
		#
		self.__keySeries        = ''
		self.__datetime         = datetime.now().strftime(self.__dateTimeFormat)
		# inner class
		self.__style            = self.__StyleModifier()
		# session as uuid or md5
		self.__sessionKey       = ''

	def __backupFileName(self) -> str:
		"""

		:return:
		"""
		# generate a filename
		return f'{self.__path}{(datetime.now() - timedelta(1)).strftime(self.__formatFileName)}{self.__extension}'

	def __createNewBackupFile(self) -> None:
		"""

		:return:
		"""
		# backup the yesterday content and use the yesterday as name of the backup file
		yesterdayFileName       = self.__backupFileName()

		# check yesterday file with len of current file
		if not os.path.exists(yesterdayFileName) and len(self.__getContentFile(self.__filename)) > 0:
			# rename current file to do backup
			# that will move content too
			os.rename(
				self.__filename
				, yesterdayFileName
			)

	def __getContentFile(self, fileName: str) -> str:
		"""

		:param fileName:
		:return:
		"""
		try:
			# init
			content = ''

			# read file
			with open(fileName) as f:
				content = f.read()

			# final
			return content

		except IOError:
			return ''

		except Exception:
			return ''

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

	def __setNewId(self, id: int) -> None:
		"""

		:param id:
		:return:
		"""
		if id > Logger.id:
			Logger.id   = id

	def __write(self, typeName: str = '', title: str = '', color: str = '', content: dict = None, logId: int = None) -> None:
		"""

		:param typeName:
		:param title:
		:param content:
		:param color:
		:param logId:
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
			contentBody = self.__getContentBody(typeName= typeName, title=title, content= self.__getStr(content= content), color= color)
			contentHead = self.__getContentHead(logId= Logger.id)

			# enable file log
			if bool(self.__enableLog):
				# write to file
				self.__writeFile(content= f'{contentHead}{contentBody}')

				# verify first
				if self.__sessionKey:
					# output content to specific file via session's
					self.__writeSessionFile(content= f'{contentHead}{contentBody}')

			# enable console
			if bool(self.__enableConsole):
				# console
				print(f'{contentHead}{contentBody}')

	def __getContentBody(self, typeName: str, title: str, content: str, color: str) -> str:
		"""

		:param typeName:
		:param title:
		:param content:
		:param color:
		:return:
		"""
		lineStart   = ''
		lineEnd     = ''
		cHead       = ''
		cBody       = f'[{typeName}] '
		cFoot       = ''

		# add line to content
		if bool(self.__line):
			lineStart   = '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
			lineEnd     = '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
			# update
			cHead       = lineStart
			cFoot       = lineEnd

		# add color, style
		if bool(self.__color):
			# update
			cHead       = f'{color}{cHead}{self.__style.ENDC}'
			cFoot       = f'{color}{cFoot}{self.__style.ENDC}'
			cBody       = f'{color}{cBody}{self.__style.ENDC}{self.__style.TEXT_BOLD}{title}{self.__style.ENDC}'

		else:
			cBody       = f'{cBody}{title}'

		# final content
		# f"{cBody}{self.__getStr(content)} \n{datetime.now().strftime(self.__dateTimeFormat)}" \
		return f'\n{cHead}\n{cBody}{self.__getStr(content)} \n{cFoot}\n\n' if bool(self.__line) else f'\n{cBody}\n'

	def __getContentHead(self, logId: int) -> str:
		"""

		:return:
		"""
		# final data
		return f'{self.__datetime} <{self.__keySeries}> <id: {logId}>\n'

	def __writeFile(self, content: str) -> None:
		"""
		@note: final written file
		:param content:
		:return:
		"""
		try:
			# open log file, if not exist will create
			with open(self.__filename, 'a+', encoding= 'utf-8') as f:
				f.write(content)

		except FileNotFoundError as e:
			print(f'Logger.__writeFile output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

		except IOError as e:
			print(f'Logger.__writeFile output file IOError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

		except Exception as e:
			print(f'Logger.__writeFile output file Exception: open file({self.__filename}), {str(e)}')

	def __writeSessionFile(self, content: Any) -> None:
		"""

		:param content:
		:return:
		"""
		try:
			# open log file, if not exist will create
			with open(f'{self.__path}{self.__sessionKey}{self.__extension}', 'a+', encoding= 'utf-8') as fs:
				fs.write(content)

		except FileNotFoundError as e:
			print(f'Logger.__writeSessionFile output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__path}{self.__sessionKey}{self.__extension}), {str(e)}')

		except IOError as e:
			print(f'Logger.__writeSessionFile output file IOError: open file {e.errno} {e.strerror}({self.__path}{self.__sessionKey}{self.__extension}), {str(e)}')

		except Exception as e:
			print(f'Logger.__writeSessionFile output file Exception: open file ({self.__path}{self.__sessionKey}{self.__extension}), {str(e)}')

	def disableIds(self, numbers: list = None) -> None:
		"""

		:param numbers:
		:return:
		"""
		if numbers:
			Logger.hide     = numbers

	def error(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:return:
		"""
		self.__write(
			typeName    = 'ERROR'
			, title     = title
			, content   = content if content else {}
			, color     = self.__style.RED
			, logId     = id
		)

	def fail(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:return:
		"""

		self.__write(
			typeName    = 'FAIL'
			, title     = title
			, content   = content if content else {}
			, color     = self.__style.MAGENTA
			, logId     = id
		)

	def info(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""

		:param title:
		:param content:
		:param id:
		:return:
		"""
		self.__write(
			typeName    = 'INFO'
			, title     = title
			, content   = content if content else {}
			, color     = self.__style.BLUE
			, logId     = id
		)

	def setKeySeries(self, series: str = None) -> None:
		"""
		:param series:
		:return:
		"""
		if series:
			self.__keySeries    = series

		else:
			self.__keySeries    = ''

	def setSessionKey(self, sessionKey: str) -> None:
		"""

		:param sessionKey:
		:return:
		"""
		self.__sessionKey       = sessionKey

	def success(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""
		:param title:
		:param content:
		:param id:
		:return:
		"""
		self.__write(
			typeName    = 'SUCCESS'
			, title     = title
			, content   = content if content else {}
			, color     = self.__style.GREEN
			, logId     = id
		)

	def track(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""
		:param title:
		:param content:
		:param id:
		:return:
		"""
		self.__write(
			typeName    = 'TRACK'
			, title     = title
			, content   = content
			, logId     = id
		)

	def warning(self, title: str = '', content: dict = None, id: int = None) -> None:
		"""
		:param title:
		:param content:
		:param id:
		:return:
		"""
		self.__write(
			typeName    = 'WARNING'
			, title     = title
			, content   = content if content else {}
			, color     = self.__style.YELLOW
			, logId     = id
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
		ENDC            = '\033[0m'
