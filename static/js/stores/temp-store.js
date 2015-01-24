define(function(require) {
    var AppDispatcher = require("app-dispatcher");
    var EventEmitter = require("lib/event/event-emitter");
    var $ = require("jquery");

    var _temp = null;
    var _loaded = false;

    var TempStore = EventEmitter.create({
        getTemp: function() {
            return _temp;
        },

        hasLoaded: function() {
            return _loaded;
        }
    });

    AppDispatcher.register(function(action) {
        switch(action.actionType) {
            case "UPDATE_TEMP":
                _temp = action.temp;
                _loaded = true;
                TempStore.emitChange();
                break;

            default:
                break;
        }
    });

    return TempStore;
});
