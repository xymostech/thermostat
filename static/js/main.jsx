define(function(require) {
    var React = require("react");
    var TempViewer = require("jsx!temp-viewer");
    var StatusViewer = require("jsx!status-viewer");

    var Main = React.createClass({
        render: function() {
            return <div>
                <TempViewer />
                <StatusViewer />
            </div>;
        }
    });

    React.render(<Main />, document.body);
});
