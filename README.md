    # Simple-port-scanner
This is a simple port scanner. 

    ##Disclaimer
-Only scan systems you own or have explicit permission to scan. Unauthorized scanning is illegal and could get you in trouble. Scanning most URLs without permission is often treated as 'probing' for vulnerabilities. No matter the intentions, be safe and be sure of the site or IP address you are scanning. I do explicitly state the test site I used, which is safe, there are more sites and services that are safe to scan as well. 

This Python script scans a range of ports on a target host and shows which ports are open along with common service names.

    ## REQUIREMENTS:
Python -To install Python, I recommend using Visual Studio Code and Searching for a Python installment. You do not need any more libraries.

    ##To run the script:
1.Open Visual Studio Code(This will be referred to as VSC) 
2.Click the elipsis at the top -select terminal 
3.In Github: select Simple-port-scanner, then click on code, and copy the HTTPS link 
4.In VSC terminal type git clone (then paste the https link) 
5.After cloning the repo, click file, then open folder, find the folder with Simple Port Scanner, select it 
6.Once you see all of the code click the play icon located at the top right of the viewing 
7.In the terminal, it will have Enter a host to scan (e.g., '127.0.0.1' or 'scanme.nmpa.org):

    ## Port scanner   
-To use the port scanner, after the colon symbol(in the terminal) 
   -enter the url or IP address you wish to scan, (for testing purposes I used scanme.nmap.org)
  -After the address, it will prompt you for the start port and end port
    -these can be any number you want, but I stuck with the port numbers for FTP and Kerberos(20 and 88)
-It will then tell you what Port is open along with the service it provides (if the service was defined in the common_port section)
  
  
    ## Future improvements
-Auto fill ports that are frequently checked, bypassing the prompt to enter a start and end port. This eliminates user input errors in the terminal.

    ## Contributing
For any contributions, please open an issue first to discuss what you would like to change and how you would do it.

