var locations = ko.observableArray();

function ViewModel() {
    this.showNav = ko.observable(true);
    this.clickMenu = function () {
        if (this.showNav() == true) this.showNav(false);
        else this.showNav(true);
    };

    this.keyword = ko.observable('');
    /*
     * @description The watcher for the search bar changes that
     * will filter the displayed locations in the list and the map
     */
    this.keyword.subscribe((function (keyword) {
        locations.removeAll();
        for (var p in markers) {
            if (markers[p].title.toLowerCase().includes(keyword.toLowerCase())) {
                locations.push({index:p, title:markers[p].title});
                markers[p].setVisible(true);
            }
            else markers[p].setVisible(false);
        }
    }));
    /*
     * @description Handel the list locations clicks
     */
    this.clickLocation = function (location) {
        markerClicked(markers[location.index]);
    }
}

ko.applyBindings(ViewModel);