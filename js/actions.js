var AppDispatcher = require("./app-dispatcher.js");

var Actions = {
    requestTemp: function() {
        fetch("/api/current_temp")
            .then((response) => response.json())
            .then((data) => {
                Actions.updateTemp(data.temp);
            });
    },

    requestHeatActive: function() {
        fetch("/api/heater_on")
            .then((response) => response.json())
            .then((data) => {
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

module.exports = Actions;
