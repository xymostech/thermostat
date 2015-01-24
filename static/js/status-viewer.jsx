define(function(require) {
    var React = require("react");
    var StatusStore = require("stores/status-store");
    var StateFromStore = require("jsx!lib/react-components/state-from-store-mixin");
    var Actions = require("actions");

    var StatusViewer = React.createClass({
        mixins: [StateFromStore({
            heatOn: {
                store: StatusStore,
                fetch: function(store) {
                    return store.getHeatStatus();
                }
            }
        })],

        render: function() {
            if (!StatusStore.hasLoaded()) {
                return <p>Loading status...</p>;
            }

            var heatStatus = this.state.heatOn ? "on" : "off";

            return <p>The heater is currently {heatStatus}.</p>;
        },

        componentDidMount: function() {
            Actions.requestHeatActive();
        }
    });

    return StatusViewer;
});
