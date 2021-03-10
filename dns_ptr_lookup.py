from IPy import IP
import sys, getopt, socket

def get_reverse(val):
    val = IP(val)
    try:
        print("\tThe IP entered is: "+str(IP(val)))
        print("\tThis IP is of the \""+str(val.iptype())+"\" type and is a \"IPv"+str(val.version())+"\".")
        print("\tThe reverse (PTR) lookup of the IP address entered is: "+str(val.reverseNames()[0]))
        try:
            print("\tThe hostname for the IP entered is: "+ str(socket.gethostbyaddr(str(val))[0]))
        except:
            print("\tThe hostname for the IP entered is: Not found/applicable")
    except:
        print("\tThe IP entered is not a valid IP address")

def get_forward(val):
    print("\tThe hostname entered is: "+str(val))
    # print("The forward lookup of the hostname entered is: "+str(val.reverseNames()[0]))
    try:
        print("\tThe IP address resolution for the hostname entered is: "+ str(socket.gethostbyname(str(val))))
    except:
        print("\tThe IP address for the hostname entered is not found")

def sec_resolve(val):
    if(val.replace(".","").isnumeric()):
        try:
            str(IP(val).int()).isnumeric()
            get_reverse(val)
        except:
            print("Invalid IP address")
    elif(val.replace(".","").isalnum()):
        get_forward(val)
    else:
        print("Invalid hostname")

def resolve_input(val):
    if(not val):
        val = input("Enter an IP address or a host name to resolve: ")
        sec_resolve(val)
    else:
        sec_resolve(val)

def main(argv):
    ipf = ""
    opf = ""
    fqdn = ""
    opts = ""
    inpt = ""
    
    print('Project_CS521.py -i <ipaddress> -m <typeoflookup: A or PTR> -f <FQDN>')
    
    try:
        opts, arg = getopt.getopt(argv,"hi:m:f:")
#         print("opts: "+str(opts))
#         print("arg: "+str(arg))
    except:
        print('Project_CS521.py -i <ipaddress> -m <typeoflookup: A or PTR> -f <FQDN>')
    try:
#         if(not arg):
#             print('Project_CS521.py -i <ipaddress> -m <typeoflookup: A or PTR> -f <FQDN>')
#             print("arg:"+str(arg))
        if(not opts and not arg):
            resolve_input("")
        elif(not opts and arg):
            inpt = arg
#             print("Hello there: "+str(inpt))
            resolve_input(inpt[0])
        else:
            for opt, arg in opts:
                if opt == '-h':
                    print('Project_CS521.py -i <ipaddress> -m <typeoflookup: A or PTR> -f <FQDN>')
                    sys.exit()
                elif opt in ["-i", "--ipaddress"]:
                    ipf = arg
                    print("The IP Address entered is : "+str(ipf))
                    sec_resolve(ipf)
                
#                 elif opt in ["-m", "--typeoflookup"]:
#                     opf = arg
#                     print("The type of lookup requested is : "+str(opf))
#                     sec_resolve(opf)
                
                elif opt in ["-f", "--FQDN"]:
                    fqdn = arg
                    print("The FQDN entered is : "+str(fqdn))
                    sec_resolve(fqdn)
    except:
        sys.exit(2)
            
if __name__ == "__main__":
    main(sys.argv[1:]) 
