# Bots reading Bots

!(images/book.mp4) <<height:250px;transparent>> 
!(images/baby.mp4) <<height:250px;transparent>> 
!(images/book.mp4) <<height:250px;transparent>> 

[https://github.com/thoppe/bots-reading-bots](https://github.com/thoppe/bots-reading-bots)
----------
[travis.hoppe](http://thoppe.github.io/), [@metasemantic](https://twitter.com/metasemantic)

====

## Most people use ML/DL to solve problems ...
_classification, unsupervised learning, regression, ... _

!(images/ML2.png) <<height:400px;transparent>>
!(images/ML3.png) <<height:400px;transparent>>

====

## Machine are people too!
not really...
but what happens if you start treating them as such?

## Garbage-in garbage-out
Let's get more nuanced, what if the input data shapes their *personality*...

====

## My people
Each bot is a book...

!(images/dorthy_glitch.mp4) <<height:300px;transparent>> Frank Baum bot
!(images/wuthering_heights.mp4) <<height:300px;transparent>> Emily Brontë bot
!(images/poe_head.mp4) <<height:300px;transparent>> Edgar Allen Poe bot

What happens when one bot reads the book of the other?

====
## Methodology

Top 250 books cross-referenced from [project Gutenberg](https://www.gutenberg.org/) and [goodreads](https://www.goodreads.com/)

Manually cleaned headers, footers, and forwards (unsexy data science)

Used `tensorflow` and `tflearn` to build a LSTM-RNN

128 wide two-layer network, length 15, max 500K input samples, 100K test

Bot2bot similarity calculated by the cross-entropy loss
normalized against the internal test loss. 

====

#  Thanks, you.
## Say hello! [@metasemantic](https://twitter.com/metasemantic)