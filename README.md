`alittleprogress` is a python package/class that creates a little simple progress bar for long running terminal applications. 

Usage is simple.

        from alittleprogress import Bar

        width = 50 	## Width of the bar on-screen
        N = 10000 	## Number of iterations

        bar = Bar(width, N) ## Instantiates and draws bar edges

        for i in range(N):
            # Do something here!
            bar.update(i) ## Adds a dash if (i % N/width) == 0
        
        bar.end() ## Cleans up


There are many powerful, neat progress bar packages. I wanted a really simply one for my really simple needs. Besides, I prefer this ascetic aesthetic.
