Coursesolve-THA
===============

Work for Coursolve Twitter Healthcare Analysis within Coursera Introduction to DataScience

## Purpose

Classify tweets in the categories listed below

- news
- opinions
- deals
- events
- private

Analysis based on principes explained in this document

[SHORT TEXT CLASSIFICATION IN TWITTER TO 
IMPROVE INFORMATION FILTERING)](
https://etd.ohiolink.edu/!etd.send_file?accession=osu1275406094&disposition=inline)

## document extraction

Pre-process the document to add some counters (number of words denoting opinions, deals or events, number of hastags or at signs, ...). 
This step keeps the tweet uri (as an id), the author, the content and add 8 tags and last column always set to UNKNOW which will be replaced by a tweet category in training samples.
Though tags hold numeric values they represent category levels. 
 
<pre><code>
cd extract-tags
bash process_files.bash 
</code></pre>

This bash script grab all the data files and run a python program against each file (extract_factors.py). When its done run the line below to merge all the samples in a single dataset.

The python program use three data source

- AFINN file for sentiments
- deals for the list of woard denoting deals
- events for the list of words denoting events

<pre><code>
cat processed/* > processed_data.csv
</code></pre>

There are 1 475 793 lines. Some the source samples items were not parsed due to carriage return in messages, thus there are less lines than the total amount of tweets but should be enough to validate the process.




