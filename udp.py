# Imports
import socket
import threading

# Defaults
networkAddress   = "127.0.0.1"   
broadcastPort    = 7500
localIP          = "0.0.0.0"  
localPort        = 7501
bufferSize       = 1024

# Runtime control
running = False

# Socket references
UDPClientSocket = None
UDPServerSocket = None
receiverThread  = None

# Creates sockets and starts receiver thread
def startUDP():
    global running, UDPClientSocket, UDPServerSocket, receiverThread

    if running:
        return

    # Socket 1: Client socket (port 7500)
    # Used only for sending UDP packets
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Enable broadcast permission on socket
    UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    UDPClientSocket.bind((localIP, broadcastPort))

    # Socket 2: Server socket (port 7501)
    # Used only for receiving UDP packets
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind socket to IP + port
    UDPServerSocket.bind((localIP, localPort))

    # Startup status messages
    print("UDP receive socket up and listening on {}:{}".format(localIP, localPort))
    print("UDP broadcast socket ready to send to {}:{}".format(networkAddress, broadcastPort))

    running = True

    # Runs receiveLoop() concurrently with main program
    receiverThread = threading.Thread(target=receiveLoop, daemon=True)

    # Start background listener thread
    receiverThread.start()

# Recieve loop
# Runs continuously in background thread and waits for packets and prints sender info
def receiveLoop():
    while running:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message.decode(errors="replace"))
        clientIP  = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

# Change network address option
def setNetworkAddress(newNetwork):
    global networkAddress
    if newNetwork != "":
        networkAddress = newNetwork
        print("Network changed to:", networkAddress)

# Broadcast equipment code after each player addition
def broadcastEquipmentID(equipmentID):
    if not running:
        print("UDP not started. Call startUDP() first.")
        return

    # Convert integer to bytes for transmission
    bytesToSend = str(int(equipmentID)).encode()

    # Send UDP packet to selected network + broadcast port
    UDPClientSocket.sendto(bytesToSend, (networkAddress, broadcastPort))

    # Confirmation output
    print("Broadcasted equipment id:", equipmentID, "to", networkAddress, "port", broadcastPort)
