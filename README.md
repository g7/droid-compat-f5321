Sailfish OS Compatibility Layer for Sony Xperia X Compact (kugo/f5321)
======================================================================

This project aims to enable booting the official Sailfish X images for
Sony Xperia X (suzu/f5121) on the X Compact (kugo/f5321).

The two phones share the same underlying platform (loire) and the differences
between them are minimal (screen, USB Type-C, camera sensor, battery capacity)
so that being able to run the official Sailfish X images is desirable.

Of course, although the hardware is pretty much the same, the Sailfish X
images as coming from Jolla aren't ready to be flashed on the X Compact,
so they need to be patched.

The goal of this project is to easily add compatibility to the X Compact
to suzu adaptations (also surviving OTA updates) and to also enable patching
the official Sailfish X images.

But... why?
-----------

I've been running a custom-built Sailfish OS image as my daily driver
since October. I love this little phone but I don't want to have to re-build
things every time a new Sailfish OS release happens.

This compatibility layer allows me to just use the adaptation as provided
by Jolla.

How does this work?
-------------------

Needless to say - this thing is pretty hacky. But one might argue that this
is just another hack over a bunch of other hacks, so who cares? :)

Custom builds are of course way cleaner than this.

The compatibility layer is distributed as .rpms that can be installed along the
official HW adaptation.
These packages install a bunch of hooks and settings ovverrides that allow
Sailfish to boot and work correctly on the X Compact.

These packages are designed to co-exist with the original suzu/X adaptation,
so that we can do OTAs safely.

