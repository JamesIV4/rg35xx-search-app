# rg35xx-search-app
This is a WIP search app for the RG53XX.  It's not running on-device yet.

# Screenshots
| ![Main app interface](https://i.imgur.com/cvfYW3x.png)  |  ![On-screen keyboard](https://i.imgur.com/Fqf2jnk.png) |
|---|---|

# Done
:heavy_check_mark: Search input field and button<br />
:heavy_check_mark: Search results list<br />
:heavy_check_mark: On-screen keyboard<br />
:heavy_check_mark: Keyboard support with navigation and key events<br />
:heavy_check_mark: Search functionaliy in place<br />
:heavy_check_mark: Removes file extensions and parentesis from game titles

# To Do
- [ ] Test with Python for RG35XX (https://github.com/hagibr/RG35XX)
- [ ] Implement controller support
- [ ] Store search results in 2nd array or object holding the full path of each result, to be used in launching
- [ ] Event handling for selecting a game from the list / launching a game
- [ ] Smart scrolling of results list when highlight nears the bottom of the list
- [ ] Button mapping guide at the bottom
- [ ] Ensure pygame is running on SDL 1.2 and not SDL 2 (Requires pygame 1.9.4; might be a show-stopper or require a Python UI replacement)
