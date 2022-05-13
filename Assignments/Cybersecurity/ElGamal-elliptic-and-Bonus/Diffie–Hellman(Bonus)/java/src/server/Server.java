package server;

/**
 *
 * @author ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * */

// import Libs
import java.net.*;
import java.io.*;


public class Server {

    int b = 3; /* Server Key */

    /* Client p, g, and key */
    double clientP, clientG, clientA, B, bDash;
    String BToString;

    /* initialize socket and input/output streams */
    private Socket          serverSocket   = null;
    private ServerSocket    server   = null;
    private DataInputStream receive       =  null;
    private DataOutputStream send     = null;

    /* the passed Parameter is Port Number */
    public Server(int port)
    {
        /* starts server and waits for a connection */
        try
        {
            server = new ServerSocket(port);
            System.out.println("Server started");

            System.out.println("Waiting for client on port ...");

            serverSocket = server.accept();
            System.out.println("Connected With : " + serverSocket.getRemoteSocketAddress());

            /* Server's Private Key */
            System.out.println("Server : Private Key = " + b);

            /* takes input from the client socket */
            receive = new DataInputStream(new BufferedInputStream(serverSocket.getInputStream()));

            /* sends output to the socket */
            send = new DataOutputStream(serverSocket.getOutputStream());

            /* accept p */
            clientP = Integer.parseInt(receive.readUTF());
            System.out.println("Client : P = " + clientP);

            /* accept g */
            clientG = Integer.parseInt(receive.readUTF());
            System.out.println("Client : G = " + clientG);

            /* accept A */
            clientA = Double.parseDouble(receive.readUTF());
            System.out.println("Client : Public Key = " + clientA);

            /* calculation of B */
            B = ((Math.pow(clientG, b)) % clientP);
            BToString = Double.toString(B);

            /* Sending B */
            send.writeUTF(BToString);

            /* calculation of bDash */
            bDash = ((Math.pow(clientA, b)) % clientP);

            System.out.println("Secret Key to perform Symmetric Encryption = " + bDash);

            System.out.println("\n**************************");
            System.out.println("* Server/Client Chatting *");
            System.out.println("**************************");

            String command = "";

            /* reads message from client until "stop" is sent*/
            while (!command.equals("stop"))
            {
                try
                {
                    command = receive.readUTF();
                    System.out.println("Command $ " + command);

                } catch(IOException i) {
                    System.out.println(i);
                }
            }

            /* close connection */
            System.out.println("\nClosing connection");
            serverSocket.close();
            receive.close();
        } catch(IOException i) {
            System.out.println(i);
        }
    }

}
