var EventEmitter = require("events").EventEmitter;
var assign = require("object-assign");

var CHANGE_EVENT = "change";

var baseExtension = {
    addChangeListener: function(func) {
        this.on(CHANGE_EVENT, func);
    },

    removeChangeListener: function(func) {
        this.removeListener(CHANGE_EVENT, func);
    },

    emitChange: function() {
        this.emit(CHANGE_EVENT);
    }
};

function createStore(extension) {
    return assign({}, EventEmitter.prototype, baseExtension, extension);
};

module.exports = createStore;
