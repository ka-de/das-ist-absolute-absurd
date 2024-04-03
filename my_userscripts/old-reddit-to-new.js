// ==UserScript==
// @name               Old Reddit to New
// @namespace    https://cringe.live
// @description        Always redirects to new-Reddit, avoiding Reddit's old design.
// @include            *://old.reddit.com/*
// @version            1.0
// @run-at             document-start
// @author             _ka_de
// @grant              none
// @icon               https://www.redditstatic.com/desktop2x/img/favicon/apple-icon-76x76.png
// ==/UserScript==

window.location.replace("https://reddit.com" + window.location.pathname + window.location.search);