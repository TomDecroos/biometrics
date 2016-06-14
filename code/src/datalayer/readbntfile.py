
# This module reads a *.bnt file from the Bosphorus face database

import struct

def read_bntfile(bntfilename):

    f = open(bntfilename,"rb")
    nrows = struct.unpack("H",f.read(2))[0]
    ncols = struct.unpack("H",f.read(2))[0]
    zmin = struct.unpack("d",f.read(8))[0]
    lent = struct.unpack("H",f.read(2))[0]
    imfile = []
    for i in range(lent):
        imfile.append(struct.unpack("c",f.read(1))[0])
    st = ""
    imfile = st.join(imfile)
    
    #% size of data must be N*5, with N = nrows*ncols
    size = struct.unpack("I",f.read(4))[0]/5
    if (size != nrows*ncols):
        print("Uncoherent header: The size f the matrix is incorrect");
        
    data = {"x":[],"y":[],"z":[],"a":[],"b":[],"flag":[]}
    for key in ["x","y","z","a","b"]:
        for i in range(nrows):
            # the range image is stored upsidedown in the .bnt file
            # |LL LR|         |UL UR|
            # |UL UR| instead |LL LR|
            # Since we don't want to use the insert function or 
            # compute the destination of each value, we reverse the lines
            # |LR LL|
            # |UR UL|
            # and then reverse the whole list
            # |UL UR|
            # |LL LR|
            row = [];
            for i in range(ncols):
                row.append(struct.unpack("d",f.read(8))[0])
                row.reverse()
            data[key].extend(row)
    f.close()
    
# reverse list
    data["x"].reverse()
    data["y"].reverse()
    data["z"].reverse()
    data["a"].reverse()
    data["b"].reverse()

#we determine the flag for each pixel
# In the matrix, values that are equal to zmin denotes the background
    for i in range(size):
        if data["z"][i] == zmin:
            data["x"][i] == -999999.000000
            data["y"][i] == -999999.000000
            data["z"][i] == -999999.000000
            data["flag"].append(0)
        else:
            data["flag"].append(1)
            
    return [nrows,ncols,data,imfile]
            
            
if __name__ == '__main__':
    #read the *bnt file
    [nrows,ncols,data,imfile]=read_bntfile("../../data/bs002/bs002_E_ANGER_0.bnt"); #choose the file
    
        
        
        