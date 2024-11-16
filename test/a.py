import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Logger import Logger


logger = Logger(
	enableConsole= False
	, color=False
	, line=False
)
# redis
logger.setRedis(
	enable= True
	, enableError= True
	, enableFail= True
	, enableInfo=True
	, enableTrack= True
	, enableSuccess= True
	, enableWarning= True
	, host= '0.0.0.0'
	, port= 6379
	, channel= 'duck'
)

logger.track(title='test track', content='content track')
logger.fail(title='test fail', content='content fail')
logger.success(title='test success', content='content success')
logger.error(title='test error', content='content error')


logger.begin()
logger.error()
logger.end()


