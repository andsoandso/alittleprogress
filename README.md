`alittleprogress` is a python package/class that creates a little simple progress bar for long running terminal applications. 

Usage is simple.

        from alittleprogress import Bar

        N = 10000 	## Number of iterations

        bar = Bar(N) ## Instantiates and draws bar edges

        for i in range(N):
            # Do something here!
            bar.update(i) ## Adds a dash if (i % N/width) == 0
        
        bar.end() ## Cleans up

Here is what the above progress bar looks like when it is 50% done:

        [-------------------------                        ]

And 100%:

        [-------------------------------------------------]


There are many powerful, neat, progress bar packages. I wanted a super simply one for my simple needs. Besides, I prefer this ascetic aesthetic.
