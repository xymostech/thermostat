var AppDispatcher = require("../app-dispatcher.js");
var createStore = require("./create-store.js");

var _heatOn = null;
var _loaded = false;

var StatusStore = createStore({
    getHeatStatus: function() {
        return _heatOn;
    },

    hasLoaded: function() {
        return _loaded;
    }
});

AppDispatcher.register(function(action) {
    switch(action.actionType) {
        case "UPDATE_HEAT_ACTIVE":
            _heatOn = action.heatActive;
            _loaded = true;
            StatusStore.emitChange();
            break;

        default:
            break;
    }
});

module.exports = StatusStore;
