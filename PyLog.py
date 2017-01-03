import datetime


class Severity:
    Info = "[INFO]"
    Warning = "[WARNING]"
    Critical = "[CRITICAL]"
    Error = "[ERROR]"
    Exception = "[EXCEPTION]"


logPrefix = "Log"
currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
fileExt = ".log"


def WriteLog(text, severity):
    fileName = logPrefix + "_" + currentDate + fileExt

    with open(fileName, "a") as file:
        file.write(ParseText(text, severity))

def ParseText(text, severity):
    return (datetime.datetime.today().strftime("%Y-%m-%d") + " -- " +
            datetime.datetime.today().strftime("%H:%M:%S:%f") + "\t| " + severity + " |\t" + text + "\n")

"""
WriteLog("Test Test Test INFO", Severity.Info)
WriteLog("Test Test Test WARNING", Severity.Warning)
WriteLog("Test Test Test ERROR", Severity.Error)
"""