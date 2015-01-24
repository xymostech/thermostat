define(function(require) {
    var AppDispatcher = require("app-dispatcher");
    var $ = require("jquery");

    var Actions = {
        requestTemp: function() {
            $.getJSON("/api/current_temp", function(data) {
                Actions.updateTemp(data.temp);
            });
        },

        requestHeatActive: function() {
            $.getJSON("/api/heater_on", function(data) {
                Actions.updateHeatActive(data.heat);
            });
        },

        updateTemp: function(temp) {
            AppDispatcher.dispatch({
                actionType: "UPDATE_TEMP",
                temp: temp
            });
        },

        updateHeatActive: function(heatActive) {
            AppDispatcher.dispatch({
                actionType: "UPDATE_HEAT_ACTIVE",
                heatActive: heatActive
            });
        }
    };

    return Actions;
});
