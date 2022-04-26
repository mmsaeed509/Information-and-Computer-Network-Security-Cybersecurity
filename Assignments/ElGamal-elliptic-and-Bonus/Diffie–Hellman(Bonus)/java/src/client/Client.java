package client;

/**
 *
 * @author ozil
 * GitHub : https://github.com/mmsaeed509
 *
 * */

// import Libs
import java.net.*;
import java.io.*;

public class Client {

    /* Declare p, g, and Key of client */
    int p = 23;
    int g = 9;
    int a = 4;
    double aDash, serverB;

    String pToString, gToString, aToString; /* to send Client's Keys with toString() */

    /* initialize socket and input/output streams */
    private Socket clientSocket            = null;
    private DataInputStream  receive   = null;
    private DataOutputStream send     = null;
    private DataInputStream  input   = null;

    /*
    * the passed Parameters to the constructor are to initialize :-
    *  - IP Address
    *  - Port Number
    * */
    public Client(String ipAddress, int port)
    {
        /* establish a connection */
        try
        {
            clientSocket = new Socket(ipAddress, port);
            System.out.println("Connecting to : " + clientSocket.getRemoteSocketAddress());
            System.out.println("Connected to  : " + clientSocket.getRemoteSocketAddress());

            /* receive output to the socket */
            receive = new DataInputStream(new BufferedInputStream(clientSocket.getInputStream()));

            /* sends output to the socket */
            send = new DataOutputStream(clientSocket.getOutputStream());

            // takes input from terminal
            input  = new DataInputStream(System.in);

            /* Sending p */
            pToString = Integer.toString(p);
            send.writeUTF(pToString);

            /* Sending g */
            gToString = Integer.toString(g);
            send.writeUTF(gToString);

            /* calculation of A */
            double A = ((Math.pow(g, a)) % p);
            aToString = Double.toString(A);

            /* Sending A */
            send.writeUTF(aToString);

            /* Client's Private Key */
            System.out.println("Client : Private Key = " + a);

            /* accept B */
            serverB = Double.parseDouble(receive.readUTF());
            System.out.println("Server : Public Key = " + serverB);

            /* calculation of aDash */
            aDash = ((Math.pow(serverB, a)) % p);

            System.out.println("Secret Key to perform Symmetric Encryption = " + aDash);

        }
        catch(UnknownHostException u)
        {
            System.out.println(u);
        }
        catch(IOException i)
        {
            System.out.println(i);
        }

        System.out.println("\n**************************");
        System.out.println("* Server/Client Chatting *");
        System.out.println("**************************");

        /* string to read message from input */
        String command = "";

        /* keep reading until "stop" is input */
        while (!command.equals("stop"))
        {
            try
            {
                System.out.print("Command $ ");
                command = input.readLine();
                send.writeUTF(command);
            } catch(IOException i) {
                System.out.println(i);
            }
        }

        /* close the connection */
        try
        {
            System.out.println("\nClosing connection");
            receive.close();
            send.close();
            clientSocket.close();
        } catch(IOException i) {
            System.out.println(i);
        }
    }


}
