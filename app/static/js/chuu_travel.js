function initMap(){
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 23.901636, lng: -12.376276},
        zoom: 2,
        mapId: '73c503a2e680d60f'
    });
    setMarkers(map);
}

const chuuPlaces = [
    ["Orlando, Florida",28.525725,-81.377646],
    ["Sacramento, California",38.580186,-121.495384],
    ["Las Vegas, Nevada",36.177408,-115.145830],
    ["Honolulu, Hawaii",21.329183,-157.819671],
    ["Hanoi, Vietnam",21.023121,105.832351],
    ["Da Nang, Vietnam",16.049246,108.210840],
    ["Williamsburg, Virginia",37.267410,-76.708961],
    ["Atlanta, Georgia",33.754613,-84.392350],
    ["Charlotte, North Carolina",35.221027,-80.843154],
    ["Charleston, South Carolina",32.777253,-79.935139],
    ["Philidelphia, Pennsylvania",39.951531,-75.168042],
    ["Minneapolis, Minnesota",44.957381,-93.269671],
    ["Ho Chi Minh City, Vietnam",10.781780,106.690511]
]

function setMarkers(){
    for(let i=0;i<chuuPlaces.length;i++){
        new google.maps.Marker({
            position: {lat:chuuPlaces[i][1], lng:chuuPlaces[i][2]},
            map,
            title: chuuPlaces[i][0],
        });
    }
}