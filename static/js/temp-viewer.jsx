define(function(require) {
    var React = require("react");
    var TempStore = require("stores/temp-store");
    var StateFromStore = require("jsx!lib/react-components/state-from-store-mixin");
    var Actions = require("actions");

    var TempViewer = React.createClass({
        mixins: [StateFromStore({
            temp: {
                store: TempStore,
                fetch: function(store) {
                    return store.getTemp();
                }
            }
        })],

        render: function() {
            if (!TempStore.hasLoaded()) {
                return <p>Loading temp...</p>;
            }

            return <p>The temperature is currently {this.state.temp}&deg; C.</p>;
        },

        componentDidMount: function() {
            Actions.requestTemp();
        }
    });

    return TempViewer;
});
