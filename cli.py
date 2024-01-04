"""
Author: masakokh
Version: 1.0.0
Note: library
"""
# built-in
import sys, getopt
from typing import Any
# external
from smileargs.SmileArgs import SmileArgs
# internal
from smilelog.Controller import Controller

def main(argv) -> None:
	#
	controller  = Controller()
	smile       = SmileArgs(
		allowNoValue    = False
		, duplicated    = False
		, console       = True
		, debug         = True
	)

	# path
	smile.addCommand(
		shortCommand    = 'p'
		, longCommand   = 'path'
		, description   = 'file path'
	)

	# delete
	smile.addCommand(
		shortCommand    = 'd'
		, longCommand   = 'delete'
		, description   = 'delete file'
	)

	# clean
	smile.addCommand(
		shortCommand    = 'c'
		, longCommand   = 'clean'
		, description   = 'clean file'
	)

	# run command
	smile.run()

	#
	cmdList = smile.catchCommand()
	path    = ''

	#
	for cmd in cmdList:
		# find only path
		# cmd.id
		if cmd.value == 1:
			path    = smile.getCommand()

	# found
	for cmd in cmdList:
		if cmd == 2:
			pass
		elif cmd == 4:
			pass


if __name__ == '__main__':
	"""
	"""
	#
	main(sys.argv[1:])
