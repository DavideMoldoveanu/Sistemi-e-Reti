def main():
    ip = "192.52.32.0"
    mask = 26
    bit_di_host = 32 - mask
    ip_binario = ""
    for gruppo in ip.split("."):
        x = bin(int(gruppo))[2:]
        x = x.zfill(8)
        ip_binario = ip_binario + x
    print(f"Indirizzo ip di rete in binario: {ip_binario}")
    ip_broadcast_binario = ip_binario[:mask] + "1"*bit_di_host
    print(f"indirizzo ip di broadcast in binario: {ip_broadcast_binario}")
    ip_broadcast = ""
    for i in range(0,32,8):
        gruppo = ip_broadcast_binario[i:i+8]
        ip_broadcast = ip_broadcast + str(int(gruppo,2))+"."
    ip_broadcast = ip_broadcast[:-1]
    print(ip_broadcast)
if __name__ == "__main__":
    main()