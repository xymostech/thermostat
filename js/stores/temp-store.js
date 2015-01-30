var AppDispatcher = require("../app-dispatcher.js");
var createStore = require("./create-store.js");

var _temp = null;
var _loaded = false;

var TempStore = createStore({
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

module.exports = TempStore;
