from definitions import *


def read_muon_file(file_name: str) -> list[MuonEvent]:
    """
    Converts a valid file path to a text file of muon decay times into a
    list of MuonEvents
    :param file_name: pathname to a text file
    :return:list of Muon events
    """
    file = open(file_name, "r")
    contents = file.read()
    file.close()
    return convert_file_to_list(contents)


def convert_file_to_list(contents: str) -> list[MuonEvent]:
    """
    Converts the contents of the file as a string into a list of muonEvent objects

    :param contents: string output of text file
    :return: list of muonEvent objects
    """
    muon_list: list[MuonEvent] = []
    lines_list = contents.splitlines()[:-1]
    print(lines_list)

    for i in lines_list:
        line = i.split(" ")
        print(line, i)
        muon_list.append(MuonEvent(int(line[1]), int(line[0])))

    return muon_list
