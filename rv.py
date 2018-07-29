import argparse          
import binascii

p=argparse.ArgumentParser()
p.add_argument("-o","--file",required=True) 
args = p.parse_args()

def bind(x):
    return(x[b:b+4] for b in range (0,len(x),4))

def xxd():
    try:
        file=open(args.file,"r")

    except IOError:
        print('An error occured trying to read the file.')
        quit()

    noline=0
    line=0
    leng=0
    c=0
    fread=file.read()
    repls=fread.replace(" ",".")
    repls=fread.replace("\n",".")
    hexa=binascii.hexlify(fread.encode("utf-8")).decode("utf-8")

    
    leng=int(len(fread))
    if leng <16:
        line=1

    else:
        line=leng/16 + 1

    for y in range(int(line)):
        div=hexa[c:c+32]
        stri=repls[c:c+16]
        
        wri="{:#08x}".format(noline)+ " : "
        wri+=" ".join(bind(div))
        wri+="   " + stri  
        noline=noline+16
        c=c+16

        print(wri)

xxd()

        
        
        
    
            
