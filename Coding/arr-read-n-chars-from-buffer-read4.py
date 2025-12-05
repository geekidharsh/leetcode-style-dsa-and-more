"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file

Question is basically asking to simulate DDR ram: ram fetches 4 bytes at a time (32-bit)
Please describe how DDR memory works.

"""



class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # needs revision
        # question is confusing, need to read 4 at a time from 'buf', copy it to buf4
        # keep a counter of total lines read
        # if curr count is 0, end of file
        # update curr_count to be min(curr_count, lines remaining to be read)
        total_reads = 0
        buf4 = [''] * 4
        while total_reads < n:
            curr_count = read4(buf4)
            if not curr_count:
                break #eof

            curr_count = min(curr_count, n - total_reads)
            buf[total_reads:] = buf4[:curr_count]
            total_reads += curr_count
        return total_reads
        