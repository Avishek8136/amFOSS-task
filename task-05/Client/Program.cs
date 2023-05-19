using System;
using System.Text;
// check whether all required namespaces are imported
using System.Net;
using System.Net.Sockets;
//mising namespaces

public class SynchronousSocketClient
{

    public static void StartClient()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];

        // Connect to a remote device.  
        try
        {
            // Establish the remote endpoint for the socket.  
            // check if the port is defined or not
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = ipHostInfo.AddressList[0];
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, 8080);

            // Check whether TCP Socket is created correctly
            Socket sender = new Socket(ipAddress.AddressFamily);

            // Connect the socket to the remote endpoint. Catch any errors.  
            try
            {
                sender.Connect(remoteEP);

                Console.WriteLine("Socket connected to {0}",
                    sender.RemoteEndPoint.ToString());

                // check if the variable is defined correctly or not
                Console.WriteLine("Enter the Person Name: ");
                string name = Console.ReadLine(); //data type name is not declared
                Console.WriteLine("Enter the Person Intrest: ");
                string intrests = Console.ReadLine(); //Datatype error
                Console.WriteLine("Enter the Person Email: ");
                string mail = Console.ReadLine(); //data type mail is not declared
                // Encode the data string into a byte array.  
                // check the data type of the data you are sending.
                bytes msg = Encoding.ASCII.GetBytes(name + "," + intrests + "," + mail);

                // Send the data through the socket.  
                int bytesSent = sender.Send(msg);

                // Close the socket.

            }
            catch (ArgumentNullException ane)
            {
                Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
            }
            catch (SocketException se)
            {
                Console.WriteLine("SocketException : {0}", se.ToString());
            }
            catch (Exception e)
            {
                Console.WriteLine("Unexpected exception : {0}", e.ToString());
            }

        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
    }

    // check the main function
    public static int Main(String[] args)
    {
        StartClient(); //There is no any start() function.
        return 0;
    }
}
