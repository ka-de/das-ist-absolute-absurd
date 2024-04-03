// ==UserScript==
// @name         Discord Color Fix
// @namespace    https://cringe.live
// @version      1.0
// @description  Replace bad username colors on a very specific Discord channel.
// @author       _ka_de
// @match        https://discord.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Define the original and replacement colors
    const originalColors = [
        { original: '0, 255, 255', replacement: '255, 0, 128'},   // Cyan -> Raspberry
        { original: '233, 204, 88', replacement: '51, 153, 255'}, // Mustard -> Sky Blue
        { original: '241, 196, 15', replacement: '255, 153, 51'}, // Sunflower -> Orange
        { original: '250, 247, 220', replacement: '0, 128, 128'}, // Platinum -> Teal
    ];

    // Function to replace color styles
    function replaceColorStyles() {
        const elements = document.querySelectorAll('[style*="color: rgb"]');
        elements.forEach(element => {
            originalColors.forEach(color => {
                const originalRGB = color.original;
                const replacementRGB = color.replacement;
                const style = element.getAttribute('style');
                if (style.includes(originalRGB)) {
                    const newStyle = style.replace(`color: rgb(${originalRGB})`, `color: rgb(${replacementRGB})`);
                    element.setAttribute('style', newStyle);
                }
            });
        });
    }

    // Observe changes in the DOM and apply the replacement
    const observer = new MutationObserver(replaceColorStyles);
    observer.observe(document.body, { subtree: true, childList: true });

    // Run the replacement initially
    replaceColorStyles();
})();
