# oneTimePad
A python program that encrypts and decrypts messages using OTP.

This program takes text written or pasted into the console and converts it into ciphertext using a one-time-pad method. It then outputs a ciphertext file and key file to the current directory. A corresponding decrypton program will decrypt the files. A way to communicate with this would be to distribute both files to the recipient(s) through different mediums, preferably with one medium being in person, such as on a USB stick. This eliminates the possibility that an intercepted communication could be read - both cipher and key must be posessed in order to decrypt the plaintext.

Encryption scheme:

1. Take character, convert to ASCII

2. Since ASCII decimal numbers 0-32 are unused, subtract 33. This shifts ASCII 33-126 to 0-93, which is 94 numbers.

3. Add together the trimmed ASCII decimal numbers (possible sums 0-186)

4. Take trimmed sum (mod 94), just like in normal one-time-pads but with a longer list of available characters. (possible results -93)

5. Untrim the resulting number by adding 33, to put it back in the range of desired characters (33-126).
