// ==UserScript==
// @name         Fix that dingus navigation thing on civit 🐺
// @namespace    https://cringe.live
// @version      1.0
// @description  Changes the flex-wrap properties of .mantine-Group-root class on civitai.com
// @author       _ka_de
// @match        https://civitai.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Function to add custom CSS
    function addGlobalStyle(css) {
        var head, style;
        head = document.getElementsByTagName('head')[0];
        if (!head) { return; }
        style = document.createElement('style');
        style.type = 'text/css';
        style.innerHTML = css;
        head.appendChild(style);
    }

    // Custom CSS to change .mantine-Group-root properties under .mantine-ScrollArea-root
    var customCSS = `
        .mantine-ScrollArea-root .mantine-Group-root {
            flex-wrap: wrap !important;
            -ms-flex-wrap: wrap !important;
            -webkit-flex-wrap: wrap !important;
            -webkit-box-flex-wrap: wrap !important;
        }
    `;

    // Add the custom CSS
    addGlobalStyle(customCSS);
})();
