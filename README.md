<h2 align="left">Log4j RCE Scanner</h2>

###

<p align="left">Using this tool, you can scan for remote command execution vulnerability CVE-2021-44228 on Apache Log4j at multiple addresses.</p>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
</div>

###

<h3 align="left">Features:</h3>

###

<p align="left">It can scan according to the url list you provide.<br>It can scan all of them by finding the subdomains of the domain name you give.<br>It adds the source domain as a prefix to determine from which source the incoming dns queries are coming from.</p>

###

<h3 align="left">Requirements</h3>

###

<p align="left">httpx<br>curl<br><br>If you want to scan with a domain name, you must additionally install subfinder, assetfinder and amass.</p>

###

<h3 align="left">-h, --help - Display help<br>-l, --url-list - List of domain/subdomain/ip to be used for scanning.<br>-d, --domain - The domain name to which all subdomains and itself will be checked.<br>-b, --burpcollabid - Burp collabrator client id address or interactsh domain address.</h3>

###

<h3 align="left">Example uses:</h3>

###

<h3 align="left">./log4j-rce-scanner.py -l subdomains.txt -b 1bd6icqah2823eieuo5wdiw09rfi38rx.oastify.com<br><br>./log4j-rce-scanner.py -d evil.com -b 1bd6icqah2823eieuo5wdiw09rfi38rx.oastify.com</h3>

<br clear="both">

<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg" alt="Snake animation" />

###
