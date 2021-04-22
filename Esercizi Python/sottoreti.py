import math

bitTot=32
#chiede in input ip - maschera - nsott

def dec2bin(indIp):
    ipBinario=""
    for gruppo in indIp.split("."):
        x=bin(int(gruppo))[2:].zfill(8)
        ipBinario = ipBinario + x
    return ipBinario

def bin2dec(ipBinario):
    ipDec=""
    for i in range(0,32,8):
        x=str(int(ipBinario[i:i+8],2))
        ipDec=ipDec + x + "."
    return ipDec[:-1]

def main():
    ipBase=input("Inserire l'ip base: ")                    #ip che definisce la rete    
    mask=int(input("Inserire maschera: /"))                 #numeri di bit riservati alla rete (es /22 --> 22 bit riservati alla rete e non cambiano mai)
    nSr=int(input("Inserire il numero di sottoreti: "))     #numero sottreti 

    nBitSr=math.ceil(math.log2(nSr))    #faccio logaritmo e arrotondo il numero (sempre) per eccesso

    nBitHost=(bitTot-mask)-nBitSr
    bitHostNW=str(bin(0)[2:].zfill(nBitHost))

    bitHostBC=""
    for _ in range(nBitHost): 
        bitHostBC+="1"

    for i in range(0,nSr,1):
        bitSr=bin(i)[2:].zfill(nBitSr)
        netWork=bin2dec(dec2bin(ipBase)[:-(nBitHost+nBitSr)]+str(bitSr)+bitHostNW)
        broadCast=bin2dec(dec2bin(ipBase)[:-(nBitHost+nBitSr)]+str(bitSr)+bitHostBC)
        print(netWork,broadCast)


if __name__=="__main__":
    main()