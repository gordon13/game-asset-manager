from P4 import P4,P4Exception    # Import the module
import ConfigParser
import io
import os

def PerforceSingleton(klass):

    if not klass._instance:

        klass._instance = klass()

    return klass._instance

# Never access this Class directly
class _Perforce():
    
    _instance = None

    def __init__(self):


        fname = "%s/PerforceConnector.config"%os.path.dirname(os.path.realpath(__file__))
        config_str = ''
        with open(fname) as f:
            config = f.readlines()
            config_str = ''.join(config)

        config = ConfigParser.RawConfigParser(allow_no_value=True)
        config.readfp(io.BytesIO(config_str))

        opened = None

        self.p4 = P4() 
        self.p4.port = config.get("perforce", "port")
        self.p4.user = config.get("perforce", "user")
        self.p4.password = config.get("perforce", "password")
        self.p4.client = config.get("perforce", "client")

        try:

            self.p4.connect()                   # Connect to the Perforce server
            print("connected")
            self.p4.run_login()
            opened = self.p4.run_opened()
            info = self.p4.run( "info" )        # Run "p4 info" (returns a dict)
            for key in info[0]:            # and display all key-value pairs
                print key, "=", info[0][key]

            # set global vars
            self.server_root = info[0]['serverRoot']
            self.client_root = info[0]['clientRoot']

            # Display the vars
            print("=======================")
            print("===   global vars   ===")
            print("=======================")
            print("serverRoot: %s"%self.server_root)
            print("clientRoot: %s"%self.client_root)
            print("=======================")

        except P4Exception, e:

            print "Error : ", e


    """
    Gets the latest changes
    """
    def get_changes(self):
        try:
            print("get_changes")
            changes = self.p4.run_changes('%s/...@2016/01/01,@now'%self.client_root)
            # p4.run("change","//server/folder/...@yyyy/mm/dd,@now") works as well
            for c in changes:
              print c['desc']
              # or whatever you want, including: status, client, user, changelist...
            
            return changes

        except P4Exception:
            for e in self.p4.errors:
                print e


    """
    Disconnect from server
    """
    def disconnect(self):
        self.p4.disconnect()                # Disconnect from the server




# Call this singleton to access perforce. This ensures only one perforce class is active
ConnectPerforce = PerforceSingleton(_Perforce)
