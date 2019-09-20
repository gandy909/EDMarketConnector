1. Get coriolis.py working with latest coriolis-data/ release.

1. Revert the update cooldown to 60s.  companion.py 'holdoff' 93c4f85b3c4c25216ec5f5f62754671b9d8d04e2
1. Revert the appname et al changes: 58f9f790a817fff95df239a3ae1f677c59e10ebd
1. Revert update_feed change: 7258e3882cd1d6368aa81a67581ec1ab3f0d590f cf7d7f77de7ec53cb79faffd35e5aac9d9e862fe
1. Revert forcing bad CLIENT_ID: 3a8e317f09b390d5dee5602011f1567692bef225
1. Test all data senders:
	1. EDDN
		1. Revert forcing "is_beta = True" in plugins/eddn.py e54226cbabf68d9e18e2d70b241ce667a788c00e - DONE
		1. Station Data
			1. Commodity - WORKS
			1. Outfitting - WORKS
			1. Shipyard - WORKS
		1. System and Scan data
	1. EDSM
		1. Flight log - WORKS
		1. Current ship - WORKS
		1. Scans
		1. Lookups
			1. System - WORKS
			1. Station - WORKS
	1. Inara
		A quick test had credits balance and current ship update correctly.  Note that Inara won't accept API use as-is (I'm being cagey about why in case there are still bugs, I don't want any 'helpful' tester to spam his API with bad data).
		1. Scans
		1. Lookups
			1. System - WORKS
			1. Station - WORKS
	1. EDDB
		1. Only receives EDDN data
		1. Used for lookups
			1. System - WORKS
			1. Station - WORKS
	1. Coriolis
		1. Load current ship build on click - WORKS
	1. ED shipyard
		1. Load current ship build on click - WORKS
		1. Look into this from taleden:
			feel free to also at some point switch to POSTing to edsy.org/import with the build in a 'loadout' field; that'd avoid some ugly URLs that are sometimes too long for some browsers :)

1. Settings
	1. Output
		1. Market data in CSV format file - WORKS
		1. Market data in Trade Dangerous format file - WORKS
		1. Ship loadout - WORKS.  NB: EDMC won't export if it finds it's the same as the previously exported latest ship file.
		1. Automatically update on docking - WORKS
	1. EDDN
		1. Send station data to the Elite Dangerous Data Network - WORKS
		1. Send system and scan data to the Elite Dangerous Data Network - WORKS
		1. Delay sending until docked - WORKS
	1. EDSM - WORKS
		1. Send flight log and Cmdr status to EDSM - WORKS
	1. Inara
		1. Send flight log and Cmdr status to Inara
	1. Configuration
		1. Hotkey - WORKS
		1. Only when Elite Dangerous is the active app - Works for 'Off'.  'On' without game running does block correctly.
		1. Play sound - WORKS
		1. Preferred websites - WORKS
			1. Shipyard - WORKS
			1. System - WORKS
			1. Station - WORKS
	1. Appearance
		1. Language - WORKS (French tested)
		1. Theme - WORKS
			1. Default - WORKS
			1. Dark - WORKS
			1. Transparent - WORKS
		1. Always On top - WORKS
	1. Plugins
		1. Plugins folder

1. EDMC.py - command-line interface
1. Produce a windows executable with py2exe
1. Investigate installer options
1. Perhaps find all instances of 'EDMarketConnector' in code and replace with a global variable?  This would mean using different Windows Registry key, changing github URLs etc, all more easily than code edits all over the place.

1. Full code reviews done:

	commodity.py
	companion.py
	config.py
	coriolis.py
	dashboard.py
	EDMarketConnector.py
	EDMC.py
	edshipyard.py
	hotkey.py
	loadout.py
	monitor.py
	myNotebook.py
		May need to test full plugin functionality in a test plugin to be sure
	outfitting.py
	plug.py
	protocol.py
	setup.py
		Leaving for now, this is for .exe packaging
	shipyard.py
	stats.py
	td.py
	theme.py
	ttkHyperlinkLabel.py
	update.py

1. Any gotchas in Languages other than English and French?  i.e. theme.py

1. In general:
	1. print "..." -> print("...")
	1. x / y, when expecting an Integer result might need int(x/y)
	1. cPickle -> pickle
	1. plain <dict> isn't comparable to <dict>, so simple sorted() won't work.  Need to specify a key:
			plugins/eddn.py:                message['economies'] = sorted(list([x for x in (data['lastStarport']['economies'] or {}).values()]), key=lambda x: x['name'])
	1. Tkinter -> tkinter
		-import Tkinter as tk
		-import ttk
		-import tkFileDialog
		-import tkFont
		-import tkMessageBox
		+import tkinter as tk
		+import tkinter.ttk
		+import tkinter.filedialog
		+import tkinter.font
		+import tkinter.messagebox
	1. unicode(s) -> str(s)
	1. unichr(s) -> str(s)
	1. import urlparse -> urllib.parse
	1. .iteritems() -> .items()
	1. Don't need to .encode('utf-8') if we already had strings and need strings.
	1. If trying to .replace() we need <str> so may need to .decode() first.
	1. Need to explictly list() some things.
