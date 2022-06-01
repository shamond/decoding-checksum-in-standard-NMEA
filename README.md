# decoding-checksum-in-standard-NMEA

Detection of data transmission errors by checking the checksum
The checksum consists of two hexadecimal numbers, located
at the end of each NMEA sentence
$ GPGSA, A, 2,29,19,28 ,,,,,,,,,,, 23.4,12.1,20.0 * 0F
On all characters (bytes) between the dollar sign ($) and the asterisk
(*) an XOR operation is performed

