import sys


class Bar(object):
    def __init__(self, width, n):
        """A little (simple) progress bar.
        
        Parameters
        ---------
        width : int
            The width of the progress bar on screen.
        n : int
            The number of total number of interations expected.
        """

        self.width = int(width)
        self.n = int(n)
        self.increment = int(self.n / self.width)

        # setup progress bar
        sys.stdout.write("[{0}]".format(" " * self.width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (self.width + 1)) 
            ## return to start of line, after '['
    
    def update(self, i):
        """Update the progress bar for this iteration?"""
        if (i % self.increment) == 0:
            sys.stdout.write("-")
            sys.stdout.flush()

    def end(self):
        sys.stdout.write("\n")

