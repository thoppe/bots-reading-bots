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

## Machines are people too!
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

### Data collection
Top 100 books from last month from [project Gutenberg](https://www.gutenberg.org/)
%and [goodreads](https://www.goodreads.com/)
Manually cleaned headers, footers, and forwards (unsexy data science)

### Model
Used `tensorflow` and `tflearn` to build a LSTM-RNN
128 wide two-layer network, length 15, max 500K input samples, 100K test
bot2bot similarity calculated by as the average cross-entropy loss
of one model reading the others test set

====

## Bots get *confused* when they see new text.

## We use confusion to measure *author similarity*.

====

# Books like me

Pride and Prejudice by Jane Austen 
	 1.391 Pride and Prejudice by Jane Austen 
	 1.581 Sense and Sensibility by Jane Austen 
	 1.588 Emma by Jane Austen 
	 1.704 Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft

Second Treatise of Government by John Locke 
	 1.432 Second Treatise of Government by John Locke
	 1.693 Democracy in America -- Volume 1 by Alexis de Tocqueville 
	 1.708 Leviathan by Thomas Hobbes 
	 1.721 On Liberty by John Stuart Mill 
	 1.728 Utopia by Saint Thomas More 
	 1.729 The Republic by Plato 
  
====

# More books like me

Manifest der Kommunistischen Partei. Friedrich Engels and Karl Marx
	 1.903 Manifest der Kommunistischen Partei.
	 1.918 Democracy and Education: An Introduction to the Philosophy 
	 1.920 Democracy in America -- Volume 1 by Alexis de Tocqueville
	 1.987 On Liberty by John Stuart Mill 
	 1.995 Walden, and On The Duty Of Civil Disobedience by Henry David
  
Anna Karenina by Leo Tolstoy 
	 1.507 Anna Karenina by Leo Tolstoy 
	 1.659 The Brothers Karamazov by Fyodor Dostoyevsky 
	 1.675 Crime and Punishment by Fyodor Dostoyevsky 
	 1.683 War and Peace by Leo Tolstoy

==== 

### Similarity map
!(images/author_sim.png) <<height:750px;>>

====

### Similarity map
!(images/author_sim_annotate.png) <<height:750px;>>

====

# Where to go from here?

### More data! Collect more books, sort from [goodreads](https://www.goodreads.com/).

### Correlate measure with same author / same time period.

### What is being measured? Style, syntax, word choice, ...?

====

#  Thanks, you.
## Say hello! [@metasemantic](https://twitter.com/metasemantic)