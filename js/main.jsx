if (!global.Promise) {
    global.Promise = require("bluebird");
}
require("whatwg-fetch");

var React = require("react");
var TempViewer = require("./temp-viewer.jsx");
var StatusViewer = require("./status-viewer.jsx");

var Main = React.createClass({
    render: function() {
        return <div>
            <TempViewer />
            <StatusViewer />
        </div>;
    }
});

React.render(<Main />, document.body);
