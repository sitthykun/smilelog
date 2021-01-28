"""
Author: masakokh
Version: 3.0.2
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

    def __init__(self, path: str, name: str, extension: str, formatFileName: str, enableLog: bool= True, enableConsole: bool= True, color: bool = True):
        """

        :param path:
        :param name:
        :param extension:
        :param formatFileName:
        :param enableLog:
        :param enableConsole:
        :param color:
        """
        # default datetime format
        self.__dateTimeFormat   = '%H:%M:%S'
        # set color
        self.__color            = color
        # config
        self.__enableLog        = enableLog
        self.__enableConsole    = enableConsole
        self.__extension        = extension
        # 2020-05-18
        self.__formatFileName   = formatFileName
        # path + /
        self.__name             = name
        self.__path             = path

        # compute
        self.__filename         = self.__path + self.__name + self.__extension
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
        # create a new file
        return self.__path \
                + datetime.strftime(datetime.now() - timedelta(1), self.__formatFileName) \
                + self.__extension

    def __createNewBackupFile(self) -> None:
        """

        :return:
        """
        # yesterday
        yesterdayFileName       = self.__backupFileName()

        # check yesterday file with len of current file
        if not os.path.exists(yesterdayFileName) and len(self.__getContentFile(self.__getFileName())) > 0:
            # rename current file to backup file
            # that will move content too
            os.rename(self.__getFileName(), yesterdayFileName)

    def __dataFormat(self, content: Any) -> Any:
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

    def __getContentFile(self, fileName: str) -> str:
        """

        :param fileName:
        :return:
        """
        try:
            with open(fileName) as f:
                return f.readlines()

        except IOError:
            return ''

    def __setNewId(self, id: int) -> None:
        """

        :param id:
        :return:
        """
        if id > Logger.id:
            Logger.id   = id

    def __write(self, typeName: str = '', title: str = '', content: dict = {}, color: str = '', logId: int = None) -> None:
        """

        :param typeName:
        :param title:
        :param content:
        :param color:
        :param logId:
        :return:
        """
        # write log
        if bool(self.__enableLog):
            # create file
            self.__createNewBackupFile()

            try:
                # open log file, if not exist will create
                with open(self.__filename, 'a+', encoding= 'utf-8') as f:

                    # validate log Id
                    if logId:
                        # Reset log id
                        self.__setNewId(logId)
                    else:
                        # increase index first
                        Logger.id += 1

                    # do filter
                    if Logger.id not in Logger.hide:
                        # check color
                        if self.__color:
                            # generate content format with color
                            tempContent = f"{self.__datetime} <{self.__keySeries}> <id: {Logger.id}>"\
                                          f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"\
                                          f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{datetime.now().strftime(self.__dateTimeFormat)}"\
                                          f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"

                            # output
                            f.write(tempContent)

                            # verify first
                            if self.__sessionKey:
                                # output content to session's file
                                self.__writeSession(tempContent)

                            # clean
                            tempContent = None

                        else:
                            # generate content format without color
                            tempContent = f"{self.__datetime} <{self.__keySeries}> <id: {Logger.id}>"\
                                          f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"\
                                          f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{datetime.now().strftime(self.__dateTimeFormat)} "\
                                          f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"

                            # output
                            f.write(tempContent)

                            # verify first and write if it attends
                            if self.__sessionKey:
                                # output content to session's file
                                self.__writeSession(tempContent)

                            # clean
                            tempContent = None

            except IOError as e:
                print(f'Logger.__write output file IOError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

            except FileNotFoundError as e:
                print(f'Logger.__write output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

            except Exception as e:
                print(f'Logger.__write output file Exception: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

            # block redundancy
            # print out
            if bool(self.__enableConsole):
                try:
                    # do filter
                    if Logger.id not in Logger.hide:
                        if self.__color:
                            # generate content format with color
                            print(
                                f"{self.__datetime} <{self.__keySeries}> <id: {Logger.id}>"
                                f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{datetime.now().strftime(self.__dateTimeFormat)}"
                                f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"
                            )

                        else:
                            # generate content format without color
                            print(
                                f"{self.__datetime} <{self.__keySeries}> <id: {Logger.id}>"
                                f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{datetime.now().strftime(self.__dateTimeFormat)} "
                                f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                            )

                except Exception as e:
                    print(f'Logger.__write print Exception: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

    def __writeSession(self, content: Any) -> None:
        """

        :param content:
        :return:
        """
        try:
            # open log file, if not exist will create
            with open(self.__sessionKey + self.__extension, 'a+', encoding= 'utf-8') as fs:
                fs.write(content)

        except IOError as e:
            print(f'Logger.__writeSession output file IOError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

        except FileNotFoundError as e:
            print(f'Logger.__writeSession output file FileNotFoundError: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

        except Exception as e:
            print(f'Logger.__writeSession output file Exception: open file {e.errno} {e.strerror}({self.__filename}), {str(e)}')

    def disable(self, numbers: list = []) -> None:
        """

        :param numbers:
        :return:
        """
        Logger.hide     = numbers

    def error(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """

        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= f'{self.__style.RED}ERROR{self.__style.ENDC}'
                , title= f'{self.__style.RED}{title}{self.__style.ENDC}'
                , content= content
                , color= self.__style.RED
                , logId= id
            )

        else:
            self.__write(
                typeName= 'ERROR'
                , title= title
                , content= content
                , color= self.__style.RED
                , logId= id
            )

    def fail(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """

        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= f'{self.__style.MAGENTA}FAIL{self.__style.ENDC}'
                , title= f'{self.__style.MAGENTA}{title}{self.__style.ENDC}'
                , content= content
                , color= self.__style.MAGENTA
                , logId= id
            )

        else:
            self.__write(
                typeName= 'FAIL'
                , title= title
                , content= content
                , color= self.__style.MAGENTA
                , logId= id
            )

    def info(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """

        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= f'{self.__style.BLUE}INFO{self.__style.ENDC}'
                , title= f'{self.__style.BLUE}{title}{self.__style.ENDC}'
                , content= content
                , color= self.__style.BLUE
                , logId= id
            )

        else:
            self.__write(
                typeName= 'INFO'
                , title= title
                , content= content
                , color= self.__style.BLUE
                , logId= id
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

    def success(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """
        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= f'{self.__style.GREEN}SUCCESS{self.__style.ENDC}'
                , title= f'{self.__style.GREEN}{title}{self.__style.ENDC}'
                , content= content
                , color= self.__style.GREEN
                , logId= id
            )

        else:
            self.__write(
                typeName= 'INFO'
                , title= title
                , content= content
                , color= self.__style.GREEN
                , logId= id
            )

    def track(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """
        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= 'TRACK'
                , title= title
                , content= content
                , logId= id
            )

        else:
            self.__write(
                typeName= 'TRACK'
                , title= title
                , content= content
                , logId= id
            )

    def warning(self, title: str = '', content: dict = {}, id: int = None) -> None:
        """
        :param title:
        :param content:
        :param id:
        :return:
        """
        if self.__color:
            self.__write(
                typeName= f'{self.__style.YELLOW}WARNING{self.__style.ENDC}'
                , title= f'{self.__style.YELLOW}{title}{self.__style.ENDC}'
                , content= content
                , color= self.__style.YELLOW
                , logId= id
            )

        else:
            self.__write(
                typeName= 'WARNING'
                , title= title
                , content= content
                , color= self.__style.YELLOW
                , logId= id
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
