Initial scraping of restaurants on the website [OpenRice Singapore](https://sg.openrice.com) was done using the [Wayback Machine Downloader](https://github.com/hartator/wayback-machine-downloader). This downloaded archived copies of the web pages from the [Internet Archive](https://archive.org), rather than directly interacting with SG Openrice's servers. We chose this method because SG OpenRice's servers dropped our connections when we attempted to download HTML pages via GET requests, or browse it programmatically using a headless browser; we figured out how to circumvent this and imitate a real user, but decided it was best not to. Downloading from the Internet Archive, we did not have to worry about any such issues.

To install the package, first install the Ruby programming language. Then run `gem install wayback_machine_downloader`.

The command then used to scrape SG Openrice was as follows.

`wayback_machine_downloader https://sg.openrice.com/en/singapore/r-* --only "/index\.html$/i" --from 2020`

We added the `--from` condition so that only page captures after the most recent redesign of the website would be included, so that our files would have a common HTML structure. After doing so, we obtained 4,438 pages. About 400 didn't match our desired format, leaving 4,004 restaurants. 

The 7zip-compressed folder in this directory labelled `websites` contains the results of our scraping. The pages in this folder follow the format of `websites/sg.openrice.com/en/singapore/r-{restaurant name}/index.html`, substituting the name of the restaurant for `{restaurant name}`.

We then used the Beautiful Soup Python package to parse the HTML in these files and produced a CSV containing the features we managed to extract, creating our initial dataset. The features we managed to extract were restaurant name, rating, # of reviews, price, cuisines, and street address.

This can be done by running the provided script `extract.py`. It produces 3998 rows of data in `features_no_gps.csv`; a few pages are excluded for not being valid UTF-8 text or not following the HTML format we use.

Lastly, we augmented this dataset by using the API at [PositionStack](https://positionstack.com/) to convert our street addresses into GPS coordinates. At this point we were ready to go into the next stage of data cleaning.