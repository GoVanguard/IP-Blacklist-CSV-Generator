# IP Blacklist CSV Generator
Short multiprocessed Python 3 script that generates CSV files containing blacklisted IPs, using the firehol/blocklist-ipsets repo as the source for blacklists. The purpose of this is for use with Microsoft Excel, to compare a list of IPs to these blacklists, looking to see if for example any of these blacklisted IPs are present in your network traffic logs/pcap files.

## Installation
```
git clone https://github.com/GoVanguard/IP-Blacklist-CSV-Generator.git
```

## Recommended Python Version
legion supports Python 3.5+.

## Dependencies
* Requires git to be installed and set up with an environment path

## Usage
Simply execute the script, it takes no arguments.
```
python3.6 ipblacklist.py
```

It will output the CSV files to the directory it is in.

## License
This script is licensed under the GNU Affero General Public License v3.0.

## Credits
FireHOL (for creating and maintaining the blacklists)
