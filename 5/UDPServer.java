//5b
public class UDPServer {
    public static void main(String[] args) throws IOException {
    DatagramSocket socket = new DatagramSocket(3000);
    byte[] buffer = new byte[1024];
    DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
    while (true) {
    socket.receive(packet);
    System.out.println("Received: " + new String(packet.getData()));
    socket.send(packet); // echo back
    }
    }
    }