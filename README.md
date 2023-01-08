This add-on allows redirecting of media references (e.g. `<img src="foo.png">`) to existing files with the same names in `user_files/media` subfolder in the add-on's folder.

I have thousands of screenshots used in my vocabulary cards (generated using [hoarder](https://github.com/abdnh/hoarder)) that I use for context and don't want to sync to AnkiWeb and waste bandwidth, so I wrote this add-on to allow me to put the screenshots in the add-on's folder but still be able to see them in the cards.

Using this add-on combined with [symbolic links](https://en.wikipedia.org/wiki/Symbolic_link), you can make any folder on your computer accessible inside cards by symlinking `user_files/media` to the folder.

## Known Issues

-   [ ] Check Media is not aware of your extra media folder, so it'll report any files only existing there and used in cards as missing. This may be fixed in the future.
