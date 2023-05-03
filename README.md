# rg35xx-search-app
This is a WIP search app for the RG53XX.  It's not running on-device yet.

# Done
- [x] Search input field and button
- [x] Search results list
- [x] On-screen keyboard
- [x] Keyboard support with navigation and key events
- [x] Search functionaliy in place
- [x] Removes file extensions and parentesis from game titles

# To Do
- [ ] Test with Python for RG35XX (https://github.com/hagibr/RG35XX)
- [ ] Implement controller support
- [ ] Store search results in 2nd array or object holding the full path of each result, to be used in launching
- [ ] Event handling for selecting a game from the list / launching a game
- [ ] Ensure pygame is running on SDL 1.2 and not SDL 2 (might be a show-stopper or require a Python UI replacement)
