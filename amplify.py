import struct
import sys

def amplify(ipfile, opfile, amplification):
 i = open(ipfile, "rb")
 o = open(opfile, "wb")
 
 header = i.read(44)
 o.write(header)

 
 sample = i.read(2)
 data = struct.unpack('h', sample)
 val = data[0]
 val *= amplification
 op = struct.pack('h', int(val)) 
  
 o.write(op)

 while sample: # As long as we read a valid sample, repeat this loop
      sample = i.read(2)  # Read out a sample
      if sample: # If we read something (once we reach the end of the file, sample will be '' and the if statement won't execute.
          # Unpack the sample into a python object that we can use.
          ip_data = struct.unpack('h', sample) 
          val = ip_data[0]
          # Alter the value and convert it into an integer
          val *= amplification
          val = int(val)
          # Convert it back into a file and write it out to the output file
          op_data = struct.pack('h', val)
          o.write(op_data)

 # Close files
 i.close()
 o.close()

def main():
    # sys.argv contains the command line arguments which were provided to the program. These. There's a basic introduction here https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    source = sys.argv[1] 
    target = sys.argv[2] 
    amplification = float(sys.argv[3])

    amplify(source, target, amplification)

main()
