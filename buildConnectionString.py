#!/usr/bin/python
#Filename:buildConnectSTring
def buildConnectString(params):
    """Build a connection string from a dictionary of parameters
    Returns string"""
    return ";".join(["%s=%s" %(k,v) for k,v in params.items()])

if __name__=="__main__":
    myParams = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}

    print buildConnectString(myParams)
    #server=mpilgrim;database=master;uid=sa;pwd=secert
    testparam = "2"
    if(testparam):
        print 'in the if is not give value'