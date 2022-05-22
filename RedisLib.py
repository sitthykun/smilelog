"""
Author: masakokh
Note: redis
Version: 1.0.1
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
		self.__channel		= None
		self.__pool			= None
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
			#
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
				# set current channel
				self.__channel	= channel

				# subscribe new channel
				self.__pubsub.subscribe(self.__channel)

		except Exception as e:
			print(str(e))

	def config(self, host: str, port: int, db: int = 0, password: str = None) -> None:
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
				# pool
				self.__pool		= redis.ConnectionPool(
					host				= host
					, port				= port
					, db				= db
					, decode_responses	= True
					, charset			= 'utf-8'
					, password			= password
				)

				#
				self.__redis	= redis.Redis(
					connection_pool		= self.__pool
				)

				#
				self.__pubsub	= self.__redis.pubsub()

			else:
				#
				self.__redis	= redis.ConnectionPool(
					host				= host
					, port				= port
					, db				= db
					, decode_responses	= True
					, charset			= 'utf-8'
				)

				#
				self.__redis	= redis.Redis(
					connection_pool		= self.__pool
				)

				#
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

	def messageGet(self, channel: str= None) -> Any:
		"""

		:param channel:
		:return:
		"""
		try:
			#
			if channel:
				pass
			#
			self.__pubsub.get_message()

		except Exception as e:
			print(str(e))

	def messagePush(self, title: str, body: str, channel: str = None) -> None:
		"""

		:param title:
		:param body:
		:param channel:
		:return:
		"""
		try:
			#
			message	= f'{title}:::{body}'

			#
			if channel:
				#
				self.__redis.publish(
					channel
					, message
				)

			elif self.__channel:
				#
				self.__redis.publish(
					self.__channel
					, message
				)

		except Exception as e:
			print(str(e))
