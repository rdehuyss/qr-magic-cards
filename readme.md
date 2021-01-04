# Magic Cards using QR-codes

Some of you know that I have automated most of my home which is fun for me but not everybody in my household as we don't even have a plain old CD-player.

Magic Cards merges the physical world with the digital world. It lets you create cards with QR-codes that you can program to do anything.
- Start playing music
- Play a movie
- Tune to a TV channel
- Unlock your back door
Scan your card, music starts playing. Boom.

## Why
You might be wondering why you would want to bring back physical media after finally ridding ourselves of all of it.

Yes, physical media had its downsides. You had to store it, get up to play it, and it would get damaged. Digital media is transparent, accessible from almost anywhere, and never wears out.

Ridding our world of physical media ends up having quite a few drawbacks:
- Our kids get completely left out of the experience. They have no means to play some music.
- Browsing or picking music from 10m available albums creates a paradox of choice.
- Scrolling through huge libraries on a glass screen isn't really that fast and it definitely doesn't feel that great.
- Voice queuing is great, if you can remember or even KNOW what you want to listen to.

## How
- You create and print cards with some QR codes on it (I used the open-source software GLabels). The QR codes are nothing more than url's
- Using the M5Stack QR Code reader which contains an ESP-32 Pico, the QR code is read and an http request is made (in this case to the Sonos Http API)
- Eh voila!


