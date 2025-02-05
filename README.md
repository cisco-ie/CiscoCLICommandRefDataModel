# CiscoCLICommandRefDataModel
Optimizing Cisco Command References for Azure Integration

Description:

This Python script scrapes data from Cisco Command Reference web pages, processes it, and stores it in a JSON file. The user is prompted to enter the URL of a website from which they want to scrape data. They  also provide a name for the data being scraped. The script extracts relevant information such as commands, descriptions, and examples from the HTML structure of the webpage.

Packages Required:
- requests: Allows sending HTTP requests to the provided URL.
- BeautifulSoup (from bs4): A Python library for parsing HTML and XML documents.
- json: A built-in Python library for encoding and decoding JSON data.

Functions:

1. scrape_website(url, key_value):
    - Parameters:
        - url: The URL of the website to scrape data from.
        - key_value: The name for the data being scraped (e.g., "BGP Show Commands").
    - Returns:
        - A dictionary containing the scraped data formatted as JSON.

Main Code:

Input:
- URL of the website to scrape data e.g  https://www.cisco.com/c/en/us/td/docs/iosxr/ncs5500/routing/b-ncs5500-routing-cli-reference/b-ncs5500-routing-cli-reference_chapter_010.html
- Name for the data being scraped.  e.g  IS-IS Commands

Output:
- JSON file ('output.json') containing the scraped data in a structured json format.
- [
    {
        "IS-IS Commands": [
            {
                "command": "show isis  [instance instance-id]",
                "parameters": [
                    "instance instance-id: (Optional) Displays the IS-IS adjacencies for the specified IS-IS instance only. Note The instance-id argument is the instance identifier (alphanumeric) defined by the router isis command.",
                    "Note: The instance-id argument is the instance identifier (alphanumeric) defined by the router isis command."
                ],
                "description": "show isis [instance instance-id]",
                "example": "Router# show isis\n  Wed Aug 20 23:54:55.043 PST DST\n  \n  IS-IS Router: lab\n    System Id: 0000.0000.0002 \n    IS Levels: level-2-only\n    Manual area address(es):\n      49.1122\n    Routing for area address(es):\n      49.1122\n    Non-stop forwarding: Disabled\n    Most recent startup mode: Cold Restart\n    Topologies supported by IS-IS:\n      IPv4 Unicast\n        Level-2\n          Metric style (generate/accept): Narrow/Narrow\n          Metric: 10\n        No protocols redistributed\n        Distance: 115\n    Interfaces supported by IS-IS:\n      Loopback0 is running passively (passive in configuration)\n      POS0/1/0/2 is running actively (active in configuration)\n      POS0/1/0/3 is running actively (active in configuration"
            }
           }
  ]
  }
  ] 


