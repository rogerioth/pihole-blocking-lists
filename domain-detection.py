#!/usr/bin/python3

import regex

def detect_domains(input):
    domain_regex = r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}'
    return regex.findall(domain_regex, input)

def read_text_file(filename):
    with open(filename, 'r', encoding="utf8") as f:
        return f.read()

def create_hosts_fromset(inputset):
    returnString = ''
    for domain in inputset:
        returnString += '0.0.0.0 ' + domain + '\n'
    return returnString      
    
if __name__ == '__main__':
    import sys
    text = read_text_file(sys.argv[1])
    domains = detect_domains(text)
    domainSet = set(domains)
    print(create_hosts_fromset(domainSet))
