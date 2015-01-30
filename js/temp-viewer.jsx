var Actions = require("./actions.js");
var React = require("react");
var StateFromStore = require("react-components/state-from-store-mixin");
var TempStore = require("./stores/temp-store.js");

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

module.exports = TempViewer;
