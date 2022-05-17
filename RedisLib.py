"""
Author: masakokh
Note: redis
Version: 1.0.0
"""
#
import redis
#
from typing import Any


class RedisLib:
	"""

	"""
	def __init__(self):
		"""

		"""
		# private
		self.__pubsub		= None
		self.__redis		= None
		# public
		self.enableError	= False
		self.enableFail		= False
		self.enableInfo		= False
		self.enableTrack	= False
		self.enableSuccess	= False
		self.enableWarning	= False

	def channelDelete(self, channel: str) -> None:
		"""

		:param channel:
		:return:
		"""
		try:
			self.__pubsub.unsubscribe(channel)

		except Exception as e:
			print(str(e))

	def channelSet(self, channel: str) -> None:
		"""

		:param channel:
		:return:
		"""
		try:
			# verify data
			if channel:
				self.__pubsub.subscribe(channel)

		except Exception as e:
			print(str(e))

	def config(self, host: str, port: int, db: int= 0, password: str= None) -> None:
		"""

		:param host:
		:param port:
		:param db:
		:param password:
		:return:
		"""
		#
		try:
			if password:
				#
				self.__redis	= redis.Redis(
					host				= host
					, port				= port
					, db				= db
					, decode_responses	= True
					, encoding			= 'utf-8'
					, password			= password
				)

			else:
				#
				self.__redis	= redis.Redis(
					host				= host
					, port				= port
					, db				= db
					, decode_responses	= True
					, encoding			= 'utf-8'
				)

			# set pubsub
			self.__pubsub	= self.__redis.pubsub()

		except Exception as e:
			print(f'{str(e)}')

	def itemDelete(self, key: str) -> None:
		"""

		:param key:
		:return:
		"""
		try:
			self.__redis.delete(key)

		except Exception as e:
			print(str(e))

	def itemSet(self, key: str, value: Any) -> None:
		"""

		:return:
		"""
		try:
			self.__redis.set(
				key
				, value
			)

		except Exception as e:
			print(str(e))

	def messageGet(self) -> Any:
		"""

		:return:
		"""
		try:
			self.__pubsub.get_message()

		except Exception as e:
			print(str(e))

	async def messagePush(self, title: str, body: str, channel: str) -> bool:
		"""

		:param title:
		:param body:
		:param channel:
		:return:
		"""
		try:
			self.__pubsub.publish(
				channel
				, f'{title}:::{body}'
			)
			#
			return True

		except Exception as e:
			print(str(e))
			#
			return False
