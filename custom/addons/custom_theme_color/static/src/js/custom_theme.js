odoo.define('custom_theme_color.custom_theme', function (require) {
    "use strict";

    var rpc = require('web.rpc');
    var core = require('web.core');

    core.bus.on('web_client_ready', null, function () {
        rpc.query({
            model: 'ir.config_parameter',
            method: 'get_param',
            args: ['custom_theme_color.theme_color', '#190b68e5']
        }).then(function (theme_color) {
            document.documentElement.style.setProperty('--theme-color', theme_color);
        });
    });
});
