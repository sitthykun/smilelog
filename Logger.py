"""
Author: masakokh
Version: 2.0.0
"""
import datetime, os, os.path
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

        """
        # set color
        self.__color            = color
        # config
        self.__enableLog        = enableLog
        self.__enableConsole    = enableConsole
        self.__extension        = extension
        # 2020-05-18
        self.__formatFileName   = formatFileName
        # path + /
        self.__path             = path
        self.__name             = name

        # compute
        self.__filename         = self.__getFileName()
        self.__logId            = datetime.now().strftime('%H:%M:%S')
        self.__prefixBackupFile = self.__name + '-'
        # inner class
        self.__style            = self.__StyleModifier()

    def __backupFileName(self) -> str:
        """

        """
        # create a new file
        return self.__path \
                + self.__prefixBackupFile \
                + datetime.strftime(datetime.now() - timedelta(1), self.__formatFileName) \
                + self.__extension

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

    def __createNewBackupFile(self) -> None:
        """

        """
        # yesterday
        yesterdayFileName       = self.__backupFileName()

        # check yesterday file with len of current file
        if not os.path.exists(yesterdayFileName) and len(self.__getContentFile(self.__getFileName())) > 0:
            # rename current file to backup file
            # that will move content too
            os.rename(self.__getFileName(), yesterdayFileName)

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

    def __getFileName(self) -> str:
        """

        :return:
        """
        return self.__path \
               + self.__name \
               + self.__extension

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
                            f.write(
                                f"{self.__logId} <id: {Logger.id}>"
                                f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n"
                                f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"
                            )

                        else:
                            # generate content format without color
                            f.write(
                                f"{self.__logId} <id: {Logger.id}>"
                                f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{self.__logId} "
                                f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                            )

            except IOError as e:
                print(f"IOError open file {e.errno} {e.strerror}({self.__filename})")
            except FileNotFoundError as e:
                print(f"FileNotFoundError open file {e.errno} {e.strerror}({self.__filename})")
            except Exception as e:
                print(f"Exception open file {e.errno} {e.strerror}({self.__filename})")

            # block redundancy
            # print out
            if bool(self.__enableConsole):
                try:
                    # do filter
                    if Logger.id not in Logger.hide:
                        if self.__color:
                            # generate content format with color
                            print(
                                f"{self.__logId} <id: {Logger.id}>"
                                f"{color}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{self.__style.ENDC}\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n"
                                f"{color}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{self.__style.ENDC}\n\n\n"
                            )

                        else:
                            # generate content format without color
                            print(
                                f"{self.__logId} <id: {Logger.id}>"
                                f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
                                f"[{typeName}] {self.__style.TEXT_BOLD}{title}{self.__style.ENDC} \n{self.__dataFormat(content)} \n{self.__logId} "
                                f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n\n"
                            )

                except Exception as e:
                    print(f"Exception open file {e.errno} {e.strerror}({self.__filename})")

    def disable(self, numbers: list = []) -> None:
        """

        :return:
        """
        Logger.hide     = numbers

    def error(self, title: str = '', content: dict = {}, id: int= None) -> None:
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
                , logId=id
            )

    def info(self, title: str = '', content: dict = {}, id: int= None) -> None:
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
        BLUE            = '\033[94m'
        GREEN           = '\033[92m'
        RED             = '\033[91m'
        YELLOW          = '\033[93m'

        TEXT_BOLD       = '\033[1m'
        TEXT_UNDERLINE  = '\033[4m'

        ENDC            = '\033[0m'
