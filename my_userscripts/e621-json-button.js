// ==UserScript==
// @name         e621 JSON Button
// @namespace    https://cringe.live
// @version      1.0
// @description  Adds a JSON button next to the download button on e621.net
// @author       _ka_de
// @match        https://e621.net/*
// @match        https://e6ai.net/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function constructJSONUrl() {
        // Get the current URL
        var currentUrl = window.location.href;
        // Extract the post ID from the URL
        var postId = currentUrl.match(/^https?:\/\/(?:e621\.net|e6ai\.net)\/posts\/(\d+)/)[1];
        // Check the hostname
        var hostname = window.location.hostname;
        // Construct the JSON URL based on the hostname
        var jsonUrl = 'https://' + hostname + '/posts/' + postId + '.json';
        return jsonUrl;
    }

    function createJSONButton() {
        // Create a new button element
        var jsonButton = document.createElement('a');
        // Set the attributes for the button
        jsonButton.setAttribute('class', 'button btn-info');
        var jsonUrl = constructJSONUrl();
        // Set the JSON URL as the button's href attribute
        jsonButton.setAttribute('href', jsonUrl);
        // Set the inner HTML for the button
        jsonButton.innerHTML = '<i class="fa-solid fa-angle-double-right"></i><span>JSON</span>';

        // Find the container where we want to insert the button
        var container = document.getElementById('image-extra-controls');
        // Insert the button after the download button
        container.insertBefore(jsonButton, container.children[0].nextSibling);
    }

    // Run the function to create the JSON button
    createJSONButton();
})();
