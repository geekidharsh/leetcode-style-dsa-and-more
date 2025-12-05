# Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, 
# "IPv6" if IP is a valid IPv6 address or 
# "Neither" if IP is not a correct IP of any type.

# A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 
# and xi cannot contain leading zeros. 

queryIP = "172.16.254.1"
# queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
queryIP = 'len.0.1.1'
# queryIP = "1.4.5.6"
# queryIP = "1.0.1."


def validateIPAddress(queryIP):
    def ipv4Check(s):
        "to check ip v4 bit is valid"
        try:
            if (str(int(i)) == i) and (int(i) >= 0 or int(i) <= 255):
                return True
            else:
                return False
        except:
            return False

    def checkHex(s):   
        '''Iterate over string 
        check if charater is invalid'''

        hex_str = '0123456789abcdefABCDEF'
        for ch in s:
            # Check if the character count is invalid
            if len(ch) == 0 or len(ch) > '4':
                return False
            elif ch not in hex_str:
                return False
        return True

    if '.' in queryIP:
        ipv4 = queryIP.split('.')
        if len(ipv4) != 4:
            return 'Neither'
        # we need to do this for each chunk str.str.str.str
        for i in ipv4:
            if not ipv4Check(i):
                return 'Neither'
        return 'IPv4'


    # check for IPv6
    elif ':' in queryIP:
        colon_count = 0
        for i in queryIP:
            if i == ':':
                colon_count += 1
        if colon_count != 7:
            return 'Neither'

            ipv6 = queryIP.split(':')
        if len(ipv6) != 8:
            return 'Neither'
        else:
            for i in ipv6:
                if len(i) not in range(1,5) or checkHex(i) == False:
                    return 'Neither'
                else:
                    return 'IPv6'
 


     
print(validateIPAddress(queryIP))
