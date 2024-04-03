// ==UserScript==
// @name         Customize arXiv Header
// @namespace    https://cringe.live
// @version      1.0
// @description  Customize the header on arXiv website
// @author       _ka_de
// @match        https://arxiv.org/html*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Hide .html-header-message
    var htmlHeaderMessage = document.querySelector('.html-header-message');
    if (htmlHeaderMessage) {
        htmlHeaderMessage.style.display = 'none';
    }

    // Hide .html-header-logo
    var htmlHeaderLogo = document.querySelector('.html-header-logo');
    if (htmlHeaderLogo) {
        htmlHeaderLogo.style.display = 'none';
    }

    // Modify the .desktop_header
    var desktopHeader = document.querySelector('.desktop_header');
    if (desktopHeader) {
        desktopHeader.style.fontSize = 'small';
        desktopHeader.style.height = '30px';
        desktopHeader.style.display = 'flex';
        desktopHeader.style.alignItems = 'center';
        desktopHeader.style.justifyContent = 'center';
    }

    // Hide buttons with text containing "Report Issue"
    var buttons = document.querySelectorAll('button');
    buttons.forEach(function(button) {
        if (button.textContent.includes('Report Issue')) {
            button.style.display = 'none';
        }
    });

    // Hide body::after by setting display to none
    var styleElement = document.createElement('style');
    styleElement.innerHTML = 'body::after { display: none; }';
    document.head.appendChild(styleElement);
})();