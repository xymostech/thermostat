define(function(require) {
    function EventEmitter() {
        this.listeners = {};
    }

    EventEmitter.prototype.on = function(event, func) {
        this.listeners[event] = this.listeners[event] || [];

        if (this.listeners[event].indexOf(func) === -1) {
            this.listeners[event].push(func);
        }
    };

    EventEmitter.prototype.removeListener = function(event, func) {
        if (this.listeners[event]) {
            index = this.listeners[event].indexOf(func);

            if (index !== -1) {
                this.listeners[event].splice(index, 1);
            }
        }
    };

    EventEmitter.prototype.emit = function(event, data) {
        if (this.listeners[event]) {
            for (var i = 0; i < this.listeners[event].length; i++) {
                var func = this.listeners[event][i];

                func(data);
            }
        }
    };

    EventEmitter.prototype.addChangeListener = function(func) {
        this.on("change", func);
    };

    EventEmitter.prototype.removeChangeListener = function(func) {
        this.removeListener("change", func);
    };

    EventEmitter.prototype.emitChange = function() {
        this.emit("change");
    };

    EventEmitter.create = function(extension) {
        var emitter = new EventEmitter();

        for (var key in extension) {
            if (extension.hasOwnProperty(key)) {
                emitter[key] = extension[key];
            }
        }

        return emitter;
    };

    return EventEmitter;
});
