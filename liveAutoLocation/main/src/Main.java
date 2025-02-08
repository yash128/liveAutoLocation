import java.io.DataInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {
    public static void main(String[] args) throws Exception{
        System.out.println("Hello world!");
        ServerSocket s = new ServerSocket(8765);
        Socket a = s.accept();
        System.out.println(new DataInputStream(a.getInputStream()).readUTF());
    }
}