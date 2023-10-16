"""
Author: masakokh
Version: 1.0.0
Note: SDK
"""
# internal


class SDK:
	"""

	"""
	class __Author:
		"""

		"""
		def __init__(self):
			"""

			"""
			## server are required
			self.__key		= ''
			self.__password	= ''
			self.__url		= ''
			self.__username = ''

		def getKey(self) -> str:
			"""

			:return:
			"""
			return self.__key

		def getPassword(self) -> str:
			"""

			:return:
			"""
			return self.__password

		def getURL(self) -> str:
			"""

			:return:
			"""
			return self.__url

		def getUsername(self) -> str:
			"""

			:return:
			"""
			return self.__username

		def setKey(self, key: str) -> None:
			"""

			:param key:
			:return:
			"""
			self.__key		= key

		def setPassword(self, password: str) -> None:
			"""

			:param password:
			:return:
			"""
			self.__password	= password

		def setURL(self, url: str) -> None:
			"""

			:param url:
			:return:
			"""
			self.__url		= url

		def setUsername(self, username: str) -> None:
			"""

			:param username:
			:return:
			"""
			self.__username	= username

	class __Connection:
		"""

		"""
		def __init__(self):
			"""

			"""
			# private
			self.__connection		= None
			self.__isConnected		= False
			self.__isError			= False
			self.__token			= ''
			#
			self.__errorCode		= 0
			self.__errorMessage		= ''

		def __setConnectedNo(self) -> None:
			"""

			:return:
			"""
			self.__isConnected		= False

		def __setConnectedYes(self) -> None:
			"""

			:return:
			"""
			self.__isConnected		= True

		def __setErrorNo(self) -> None:
			"""

			:return:
			"""
			self.__errorCode		= 0
			self.__errorMessage		= ''
			self.__isError			= False

		def __setErrorYes(self, message: str, code: int) -> None:
			"""

			:param message:
			:param code:
			:return:
			"""
			self.__errorMessage		= message
			self.__errorCode		= code
			self.__isError			= True

		def __setToken(self, token: str) -> None:
			"""

			:param token:
			:return:
			"""
			self.__token			= token

		def getErrorMessage(self) -> str:
			"""

			:return:
			"""
			return self.__errorMessage

		def getErrorCode(self) -> int:
			"""

			:return:
			"""
			return self.__errorCode

		def getToken(self) -> str:
			"""

			:return:
			"""
			return self.__token

		def isConnected(self) -> bool:
			"""

			:return:
			"""
			return self.__isConnected

		def isError(self) -> bool:
			"""

			:return:
			"""
			return self.__isError

		def startService(self, url: str, username: str, password: str, key: str) -> None:
			"""

			:return:
			"""
			pass

		def stopService(self) -> None:
			"""

			:return:
			"""
			self.__setConnectedNo()
			self.__setErrorNo()
			self.__setToken('')
			#
			self.__connection	= None

	def __init__(self):
		"""

		"""
		# private
		self.__auth			= self.__Author()

		# public
		self.connection		= self.__Connection()

		# lazy loading
		self.__load()

	def __load(self) -> None:
		"""

		:return:
		"""
		self.connection.startService(
			key			= self.__auth.getKey()
			, password	= self.__auth.getPassword()
			, username	= self.__auth.getUsername()
			, url		= self.__auth.getURL()
		)

	def disposeToken(self) -> None:
		"""

		:return:
		"""
		self.connection.stopService()

	def getToken(self) -> str:
		"""

		:return:
		"""
		return self.connection.getToken() if not self.connection.isError() else ''
