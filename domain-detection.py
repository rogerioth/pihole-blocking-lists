#!/usr/bin/python3

import regex
import os

def detect_domains(input_text: str) -> list:
    """
    Detects the domains present in the input text.
    :param input_text: The input text to be searched.
    :return: A list of domains found in the input text.
    """
    domain_regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
    return regex.findall(domain_regex, input_text)

def read_text_file(file_name: str) -> str:
    """
    Reads the text content of a file.
    :param file_name: The name of the file to be read.
    :return: The text content of the file.
    """
    with open(file_name, 'r', encoding="utf8") as f:
        return f.read()

def create_hosts_from_set(input_set: set) -> str:
    """
    Creates the host entries from a set of domains.
    :param input_set: The set of domains.
    :return: A string of host entries in the format '0.0.0.0 domain_name\n'.
    """
    return_string = ''
    newlist = list(input_set)
    newlist.sort()
    for domain in newlist:
        return_string += '0.0.0.0 ' + domain + '\n'
    return return_string

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Create a host file from a text file containing domains.')
    parser.add_argument('file', type=str, help='The name of the text file containing domains.')
    args = parser.parse_args()

    file_name = args.file

    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        sys.exit(1)

    try:
        text = read_text_file(file_name)
    except Exception as e:
        print(f"Error: An error occurred while reading the file '{file_name}'.")
        print(f"Error message: {str(e)}")
        sys.exit(1)

    domains = detect_domains(text)
    domain_set = set(domains)
    print(create_hosts_from_set(domain_set))
