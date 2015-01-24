define(function(require) {
    var AppDispatcher = require("app-dispatcher");
    var EventEmitter = require("lib/event/event-emitter");
    var $ = require("jquery");

    var _heatOn = null;
    var _loaded = false;

    var StatusStore = EventEmitter.create({
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

    return StatusStore;
});
